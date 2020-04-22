DROP TABLE IF EXISTS public.matches;
DROP TABLE IF EXISTS public.matchesplayed;
DROP TABLE IF EXISTS public.staging_players;
DROP TABLE IF EXISTS public.staging_rankings;
DROP TABLE IF EXISTS public.staging_matches;
DROP TABLE IF EXISTS public.players;
DROP TABLE IF EXISTS public.rankings;
DROP TABLE IF EXISTS public.tournaments;

CREATE TABLE IF NOT EXISTS public.matches (
	tourney_id varchar(256),
	match_num varchar(256),
    winner_id varchar(256),
    winner_seed varchar(256),
    winner_entry varchar(256),
    loser_id varchar(256),
    loser_seed varchar(256),
    loser_entry varchar(256),
    score varchar(256),
    best_of varchar(256),
    round varchar(256),
    minutes varchar(256),
    w_ace varchar(256),
    w_df varchar(256),
    w_svpt varchar(256),
    w_1stIn varchar(256),
    w_1stWon varchar(256),
    w_2ndWon varchar(256),
    w_SvGms varchar(256),
    w_bpSaved varchar(256),
    w_bpFaced varchar(256),
    l_ace varchar(256),
    l_df varchar(256),
    l_svpt varchar(256),
    l_1stIn varchar(256),
    l_1stWon varchar(256),
    l_2ndWon varchar(256),
    l_SvGms varchar(256),
    l_bpSaved varchar(256),
    l_bpFaced varchar(256)
);

CREATE TABLE IF NOT EXISTS public.matchesplayed (
	match_id BIGINT IDENTITY(0, 1),
    tourney_id varchar(256) NOT NULL,
    tourney_name varchar(256),
    surface varchar(256),
    draw_size varchar(256),
    tourney_level varchar(256),
    tourney_date varchar(256),
    match_num varchar(256),
    winner_id varchar(256),
    winner_seed varchar(256),
    winner_entry varchar(256),
    winner_name varchar(256),
    winner_hand varchar(256),
    winner_ht varchar(256),
    winner_ioc varchar(256),
    winner_age varchar(256),
    loser_id varchar(256),
    loser_seed varchar(256),
    loser_entry varchar(256),
    loser_name varchar(256),
    loser_hand varchar(256),
    loser_ht varchar(256),
    loser_ioc varchar(256),
    loser_age varchar(256),
    score varchar(256),
    best_of varchar(256),
    round varchar(256),
    minutes varchar(256),
    w_ace varchar(256),
    w_df varchar(256),
    w_svpt varchar(256),
    w_1stIn varchar(256),
    w_1stWon varchar(256),
    w_2ndWon varchar(256),
    w_SvGms varchar(256),
    w_bpSaved varchar(256),
    w_bpFaced varchar(256),
    l_ace varchar(256),
    l_df varchar(256),
    l_svpt varchar(256),
    l_1stIn varchar(256),
    l_1stWon varchar(256),
    l_2ndWon varchar(256),
    l_SvGms varchar(256),
    l_bpSaved varchar(256),
    l_bpFaced varchar(256),
    winner_rank varchar(256),
    winner_rank_points varchar(256),
    loser_rank varchar(256),
    loser_rank_points varchar(256)
);

CREATE TABLE IF NOT EXISTS public.staging_players (
	player_id varchar(256),
    first_name varchar(256),
    last_name varchar(256),
    hand varchar(256),
    birth_date varchar(256),
    country_code varchar(256),
    year varchar(256),
    month varchar(256),
    day varchar(256),
    birthdate varchar(256)
);

CREATE TABLE IF NOT EXISTS public.staging_rankings (
	ranking_date varchar(256),
    ranking varchar(256),
    player_id varchar(256),
    ranking_points varchar(256)
);

CREATE TABLE IF NOT EXISTS public.staging_matches (
	tourney_id varchar(256),
    tourney_name varchar(256),
    surface varchar(256),
    draw_size varchar(256),
    tourney_level varchar(256),
    tourney_date varchar(256),
    match_num varchar(256),
    winner_id varchar(256),
    winner_seed varchar(256),
    winner_entry varchar(256),
    winner_name varchar(256),
    winner_hand varchar(256),
    winner_ht varchar(256),
    winner_ioc varchar(256),
    winner_age varchar(256),
    loser_id varchar(256),
    loser_seed varchar(256),
    loser_entry varchar(256),
    loser_name varchar(256),
    loser_hand varchar(256),
    loser_ht varchar(256),
    loser_ioc varchar(256),
    loser_age varchar(256),
    score varchar(256),
    best_of varchar(256),
    round varchar(256),
    minutes varchar(256),
    w_ace varchar(256),
    w_df varchar(256),
    w_svpt varchar(256),
    w_1stIn varchar(256),
    w_1stWon varchar(256),
    w_2ndWon varchar(256),
    w_SvGms varchar(256),
    w_bpSaved varchar(256),
    w_bpFaced varchar(256),
    l_ace varchar(256),
    l_df varchar(256),
    l_svpt varchar(256),
    l_1stIn varchar(256),
    l_1stWon varchar(256),
    l_2ndWon varchar(256),
    l_SvGms varchar(256),
    l_bpSaved varchar(256),
    l_bpFaced varchar(256),
    winner_rank varchar(256),
    winner_rank_points varchar(256),
    loser_rank varchar(256),
    loser_rank_points varchar(256)
);

CREATE TABLE IF NOT EXISTS public.players (
	player_id varchar(256),
    first_name varchar(256),
    last_name varchar(256),
    hand varchar(256),
    birth_date varchar(256),
    country_code varchar(256),
	CONSTRAINT players_pkey PRIMARY KEY (player_id)
);

CREATE TABLE IF NOT EXISTS public.rankings (
	ranking_date varchar(256),
    ranking varchar(256),
    player_id varchar(256),
    ranking_points varchar(256)
);

CREATE TABLE IF NOT EXISTS public.tournaments (
	tourney_id varchar(256),
    tourney_name varchar(256),
    surface varchar(256),
    draw_size varchar(256),
    tourney_level varchar(256),
    tourney_date varchar(256),
	CONSTRAINT tournament_pkey PRIMARY KEY (tourney_id)
);