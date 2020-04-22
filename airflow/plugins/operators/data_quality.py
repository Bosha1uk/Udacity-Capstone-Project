from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

import logging

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 tables_check=[],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.tables_check = tables_check
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        redshift_hook = PostgresHook(self.redshift_conn_id)
        
        for table in self.tables_check:
            records = redshift_hook.get_records("SELECT COUNT(*) FROM {}".format(table))
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError("Data quality check failed. {} returned no results.".format(table))
            num_records = records[0][0]
            if num_records < 1:
                raise ValueError("Data quality check failed. {} contained 0 rows".format(table))
            logging.info("Data quality on table {} check passed with {} records".format(table, num_records))
            
        
        
        #longest_song_duration = redshift_hook.get_records("SELECT duration FROM longest_songs ORDER BY duration DESC LIMIT 1")
        
        #logging.info(f"The longest song is {longest_song_duration[0][0]} seconds long")
        
        player_record_2020 = redshift_hook.run("""
            BEGIN;
            DROP TABLE IF EXISTS player_record_2020;
            CREATE TABLE player_record_2020 AS (
                select p.player_id, concat(p.first_name, concat(' ', p.last_name)) AS player_name
                , NVL(w_mp.wins, 0) + NVL(l_mp.losses, 0) AS played, NVL(w_mp.wins, 0) AS wins , NVL(l_mp.losses, 0) AS losses
                from players p
                left join (SELECT winner_id, NVL(count(winner_id), 0) AS wins
                      FROM matchesplayed 
                      GROUP BY winner_id) w_mp
                on p.player_id = w_mp.winner_id
                left join (SELECT loser_id, NVL(count(loser_id),0) AS losses
                      FROM matchesplayed 
                      GROUP BY loser_id) l_mp
                on p.player_id = l_mp.loser_id
                where played > 0
                order by NVL(w_mp.wins, 0) DESC
            );
            COMMIT;
        """)
        
        most_wins = redshift_hook.get_records("SELECT player_name, wins FROM player_record_2020 ORDER BY wins DESC LIMIT 1")
        
        logging.info(f"{most_wins[0][0]} has the most wins with {most_wins[0][1]}")
        
        #paid_subscriptions = redshift_hook.get_records("SELECT num_subscriptions FROM user_subscriptions WHERE level = 'paid'")
        
        #logging.info(f"There are {paid_subscriptions[0][0]} paid subscriptions")
        
        
        