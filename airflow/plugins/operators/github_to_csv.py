#####################
### Project Scope ###
#####################

# My Project is about gathering ATP (Mens) and WTA (Womens) Tennis data including a player list, matches played, and rankings to show various types of information. 

# The end solution will provide a schema which allows users to extract data on players, matches, and tournaments including matches played in 2020, match performances in a given
# time period, and how a player's ranking has changed over time. 

# I have gathered this data from https://github.com/awesomedata/awesome-public-datasets#sports using both the ATP and WTA links. I will combine the datasets together. The datasets
# are a players dataset which gathers player information, a rankings dataset which gathers a player's ranking over time, and a matches dataset which gathers match data including
# who won the match, the score, player stats and which tournament the match was played in.

from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults



class GithubToCSVOperator(BaseOperator):
    
    #ui_color = '#333333'
    
    #template_fields = ("s3_key",)

    @apply_defaults
    def __init__(self,
                 redshift_conn_id="",
                 aws_credentials_id="",
                 region= "us-west-2",
                 *args, **kwargs):

        super(GithubToCSVOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.region = region
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        #aws_hook = AwsHook(self.aws_credentials_id)
        #credentials = aws_hook.get_credentials()
        #redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        redshift_hook = PostgresHook(self.redshift_conn_id)

        self.log.info("Gathering tables from github")
        
        #ATP player data
        url_atp_players ='https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_players.csv'
        df_atp_players = pd.read_csv(url_atp_players, error_bad_lines=False, header=None, encoding='ISO-8859-1')
        df_atp_players.columns = ['player_id', 'first_name', 'last_name', 'hand', 'birth_date', 'country_code']
        df_atp_players['tour'] = 'ATP'

        #WTA player data
        url_wta_players ='https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_players.csv'
        df_wta_players = pd.read_csv(url_wta_players, error_bad_lines=True, header=None, encoding='ISO-8859-1')
        df_wta_players.columns = ['player_id', 'first_name', 'last_name', 'hand', 'birth_date', 'country_code']
        df_wta_players['tour'] = 'WTA'

        #ATP 2020 rankings data
        #url_atp_rankings ='https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_rankings_current.csv'
        #df_atp_rankings = pd.read_csv(url_atp_rankings, error_bad_lines=False, header=None, encoding='ISO-8859-1')
        #df_atp_rankings.columns = ['ranking_date', 'ranking', 'player_id', 'ranking_points']
        #df_atp_rankings['tour'] = 'ATP'

        #WTA 2020 rankings data
        #url_wta_rankings ='https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_rankings_current.csv'
        #df_wta_rankings = pd.read_csv(url_wta_rankings, error_bad_lines=False, header=None, encoding='ISO-8859-1')
        #df_wta_rankings.columns = ['ranking_date', 'ranking', 'player_id', 'ranking_points', 'tours']
        #df_wta_rankings['tour'] = 'WTA'

        #ATP 2020 matches data
        #url_atp_matches ='https://raw.githubusercontent.com/JeffSackmann/tennis_atp/master/atp_matches_2020.csv'
        #df_atp_matches = pd.read_csv(url_atp_matches, error_bad_lines=False, encoding='ISO-8859-1')
        #df_atp_matches['tour'] = 'ATP'

        #WTA 2020 matches data
        #url_wta_matches ='https://raw.githubusercontent.com/JeffSackmann/tennis_wta/master/wta_matches_2020.csv'
        #df_wta_matches = pd.read_csv(url_wta_matches, error_bad_lines=False, encoding='ISO-8859-1')
        #df_wta_matches['tour'] = 'WTA'

        ##################################################
        ### Concatenate the ATP and WTA files together ###
        ##################################################
        
        self.log.info("Concatenating ATP and WTA files")
        
        df_players = pd.concat([df_atp_players, df_wta_players], sort=False)
        #df_rankings = pd.concat([df_atp_rankings, df_wta_rankings], sort=False)
        #df_matches = pd.concat([df_atp_matches, df_wta_matches], sort=False)

        self.log.info("Writing data to S3")
        
        df_players.to_csv('s3://bb-capstone-data/players/players.csv')
        #df_rankings.to_csv('s3://bb-capstone-data/rankings/rankings.csv')
        #df_matches.to_csv('s3://bb-capstone-data/matches/matches.csv')
        