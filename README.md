# Udacity-Capstone-Project
My Udacity Data Engineering Nanodegree Capstone Project

# Step 1: Scope the Project and Gather Data

My Project is about gathering ATP (Mens) and WTA (Womens) Tennis data including a player list, matches played, and rankings to show various types of information. 

The end solution will provide a schema which allows users to extract data on players, matches, and tournaments including matches played in 2020, match performances in a given time period, and how a player's ranking has changed over time. 

I have gathered this data from https://github.com/awesomedata/awesome-public-datasets#sports using both the ATP and WTA links. I will combine the datasets together. These datasets which involve both the ATP and WTA include:

- A players dataset which gathers player information 
- A rankings dataset which gathers a player's ranking over time (2020 only but room for further scope to increase dataload)
- A matches dataset which gathers match data including, who won the match, the score, player stats and which tournament the match was played in. (2020 only but room for further scope to increase dataload)


# Step 2: Explore and Assess the Data

The ATP Ranking data file had some entries which we not formatted properly so I removed it from the file. In the players file, I have separated the birth date by gathering the year, month, and day.

# Step 3: Define the Data Model

I have decided to use Apache Airflow to run data pipelines for this project. Please see the DAG Graph below:

Here is an outline of my data schema:

- Matches Played Fact Table
- Matches Dimension Table
- Players Dimension Table
- Rankings Dimension Table
- Tournaments Dimension Table

Please see the data model on how these on connect together below:

![](Data%20Model.PNG)

# Step 4: Run ETL to Model the Data

Please see attached Data Dictionary for the meanings of the Data columns for each Table.

# Step 5: Complete Project Write Up


