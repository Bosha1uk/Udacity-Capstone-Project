# Do all imports and installs here
import os
import glob
import psycopg2
import pandas as pd
import boto3
from datetime import datetime, timedelta
import logging
import json
import base64
import requests
#from pyspark.sql import SparkSession
#from pyspark.sql.functions import udf, col
#from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format, dayofweek, monotonically_increasing_id
#from pyspark.sql import types as T
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator

from airflow.operators import (
    GithubToCSVOperator,
    StageToRedshiftOperator, 
    LoadFactOperator,
    LoadDimensionOperator, 
    DataQualityOperator
)

from helpers import CSSqlQueries
                
default_args = {
    'owner': 'udacity',
    'start_date': datetime(2019, 4, 1),
    'depends_on_past': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=3),
}

dag = DAG('capstone_dag',
          catchup=False,
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='0 * * * *'
        )

start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)

create_tables = PostgresOperator(
    task_id='Create_tables',
    sql='cs_create_tables.sql',
    dag=dag,
    postgres_conn_id="redshift"
)
                
#github_to_csv = GithubToCSVOperator(
#    task_id='Github_to_csv',
#    dag=dag,
#    redshift_conn_id="redshift",
#    aws_credentials_id="aws_credentials",
#    region="us-west-2"
#)

stage_players_to_redshift = StageToRedshiftOperator(
    task_id='Stage_players',
    dag=dag,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="bb-capstone-data",
    s3_key="players/",
    table="staging_players",
    region="us-west-2"
)

stage_matches_to_redshift = StageToRedshiftOperator(
    task_id='Stage_matches',
    dag=dag,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="bb-capstone-data",
    s3_key="matches/",
    table="staging_matches",
    region="us-west-2"
)

stage_rankings_to_redshift = StageToRedshiftOperator(
    task_id='Stage_rankings',
    dag=dag,
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="bb-capstone-data",
    s3_key="rankings/",
    table="staging_rankings",
    region="us-west-2"
)

load_matchplayed_table = LoadFactOperator(
    task_id='Load_matches_played_fact_table',
    dag=dag,
    redshift_conn_id="redshift",
    table="matchesplayed",
    sql=CSSqlQueries.matchesplayed_table_insert,
    region="us-west-2"
)

load_players_dimension_table = LoadDimensionOperator(
    task_id='Load_players_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    table="players",
    sql=CSSqlQueries.players_table_insert,
    region="us-west-2"
)

load_rankings_dimension_table = LoadDimensionOperator(
    task_id='Load_rankings_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    table="rankings",
    sql=CSSqlQueries.rankings_table_insert,
    region="us-west-2"
)

load_matches_dimension_table = LoadDimensionOperator(
    task_id='Load_matches_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    table="matches",
    sql=CSSqlQueries.matches_table_insert,
    region="us-west-2"
)

load_tournaments_dimension_table = LoadDimensionOperator(
    task_id='Load_tournaments_dim_table',
    dag=dag,
    redshift_conn_id="redshift",
    table="tournaments",
    sql=CSSqlQueries.tournaments_table_insert,
    region="us-west-2"
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    redshift_conn_id="redshift",
    tables_check=["staging_players", "staging_rankings", "staging_matches", "matchesplayed", "players", "rankings", "matches", "tournaments"]
)

end_operator = DummyOperator(task_id='Stop_execution',  dag=dag)

start_operator >> create_tables
#create_tables >> github_to_csv
create_tables >> stage_players_to_redshift
create_tables >> stage_matches_to_redshift
create_tables >> stage_rankings_to_redshift
stage_players_to_redshift >> load_matchplayed_table
stage_matches_to_redshift >> load_matchplayed_table
stage_rankings_to_redshift >> load_matchplayed_table
load_matchplayed_table >> load_players_dimension_table
load_matchplayed_table >> load_rankings_dimension_table
load_matchplayed_table >> load_matches_dimension_table
load_matchplayed_table >> load_tournaments_dimension_table
load_players_dimension_table >> run_quality_checks
load_rankings_dimension_table >> run_quality_checks
load_matches_dimension_table >> run_quality_checks
load_tournaments_dimension_table >> run_quality_checks
run_quality_checks >> end_operator
