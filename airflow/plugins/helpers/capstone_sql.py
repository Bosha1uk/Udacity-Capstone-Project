class CSSqlQueries:
    matchesplayed_table_insert = ("""INSERT INTO {} (tourney_id, tourney_name, surface, draw_size, tourney_level, tourney_date \
    , match_num, winner_id, winner_seed, winner_entry, winner_name, winner_hand, winner_ht, winner_ioc, winner_age, loser_id, loser_seed \
    , loser_entry, loser_name, loser_hand, loser_ht, loser_ioc, loser_age, score, best_of, round, minutes, w_ace, w_df, w_svpt, w_1stIn \
    , w_1stWon, w_2ndWon, w_SvGms, w_bpSaved, w_bpFaced, l_ace, l_df, l_svpt, l_1stIn, l_1stWon, l_2ndWon, l_SvGms, l_bpSaved, l_bpFaced \
    , winner_rank, winner_rank_points, loser_rank, loser_rank_points)
    SELECT DISTINCT
    m.tourney_id,
    m.tourney_name,
    m.surface,
    m.draw_size,
    m.tourney_level,
    m.tourney_date,
    m.match_num,
    m.winner_id,
    m.winner_seed,
    m.winner_entry,
    m.winner_name,
    m.winner_hand,
    m.winner_ht,
    m.winner_ioc,
    m.winner_age,
    m.loser_id,
    m.loser_seed,
    m.loser_entry,
    m.loser_name,
    m.loser_hand,
    m.loser_ht,
    m.loser_ioc,
    m.loser_age,
    m.score,
    m.best_of,
    m.round,
    m.minutes,
    m.w_ace,
    m.w_df,
    m.w_svpt,
    m.w_1stIn,
    m.w_1stWon,
    m.w_2ndWon,
    m.w_SvGms,
    m.w_bpSaved,
    m.w_bpFaced,
    m.l_ace,
    m.l_df,
    m.l_svpt,
    m.l_1stIn,
    m.l_1stWon,
    m.l_2ndWon,
    m.l_SvGms,
    m.l_bpSaved,
    m.l_bpFaced,
    m.winner_rank,
    m.winner_rank_points,
    m.loser_rank,
    m.loser_rank_points
    FROM staging_matches m;
    """)

    matches_table_insert = ("""INSERT INTO {} (tourney_id, match_num, winner_id, winner_seed, winner_entry, loser_id, loser_seed \
    , loser_entry, score, best_of, round, minutes, w_ace, w_df, w_svpt, w_1stIn, w_1stWon, w_2ndWon, w_SvGms, w_bpSaved \
    , w_bpFaced, l_ace, l_df, l_svpt, l_1stIn, l_1stWon, l_2ndWon, l_SvGms, l_bpSaved, l_bpFaced) 
    SELECT DISTINCT
	tourney_id,
	match_num,
    winner_id,
    winner_seed,
    winner_entry,
    loser_id,
    loser_seed,
    loser_entry,
    score,
    best_of,
    round,
    minutes,
    w_ace,
    w_df,
    w_svpt,
    w_1stIn,
    w_1stWon,
    w_2ndWon,
    w_SvGms,
    w_bpSaved,
    w_bpFaced,
    l_ace,
    l_df,
    l_svpt,
    l_1stIn,
    l_1stWon,
    l_2ndWon,
    l_SvGms,
    l_bpSaved,
    l_bpFaced
    FROM staging_matches;
    """)

    rankings_table_insert = ("""INSERT INTO {} (ranking_date, ranking, player_id, ranking_points) 
                         SELECT DISTINCT
                         ranking_date,
                         ranking,
                         player_id,
                         ranking_points
                         FROM staging_rankings;
                         """)

    players_table_insert = ("""INSERT INTO {} (player_id, first_name, last_name, hand, birth_date, country_code)
                           SELECT DISTINCT
                           player_id,
                           first_name,
                           last_name,
                           hand,
                           birth_date,
                           country_code
                           FROM staging_players;
                           """)

    tournaments_table_insert = ("""INSERT INTO {} (tourney_id, tourney_name, surface, draw_size, tourney_level, tourney_date) 
                         SELECT DISTINCT
                         tourney_id,
                         tourney_name,
                         surface,
                         draw_size,
                         tourney_level,
                         tourney_date
                         FROM staging_matches;
                         """)