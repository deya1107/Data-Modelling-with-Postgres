# DROP TABLES

songplay_table_drop = "Drop table if exists songplays"
user_table_drop = "Drop table if exists users"
song_table_drop = "Drop table if exists songs"
artist_table_drop = "Drop table if exists artists"
time_table_drop = "Drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""Create table if not exists songplays (songplay_id SERIAL PRIMARY KEY, start_time decimal, user_id integer, level text, song_id text, artist_id text, session_id integer, location text, user_agent text)
""")

user_table_create = ("""Create table if not exists users (user_id integer, first_name text, last_name text, gender text, level text)
""")

song_table_create = ("""Create table if not exists songs (song_id text, title text, artist_id text, year integer, duration decimal)
""")

artist_table_create = ("""Create table if not exists artists (artist_id text, name text, location text, latitude text, longitude text)
""")

time_table_create = ("""Create table if not exists time (start_time decimal, hour integer, day text, week text, month text, year integer, weekday text)
""")

# INSERT RECORDS

songplay_table_insert = ("""Insert into songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
""")

user_table_insert = ("""Insert into users (user_id, first_name, last_name, gender, level) values (%s, %s, %s, %s, %s) on conflict do nothing;
""")

song_table_insert = ("""Insert into songs (song_id, title, artist_id, year, duration) values (%s, %s, %s, %s, %s) on conflict do nothing;
""")

artist_table_insert = ("""Insert into artists (artist_id, name, location, latitude, longitude) values (%s, %s, %s, %s, %s) on conflict do nothing;
""")


time_table_insert = ("""Insert into time (start_time, hour, day, week, month, year, weekday) values (%s, %s, %s, %s, %s, %s, %s) on conflict do nothing;
""")

# FIND SONGS

song_select = ("""select s.song_id, ar.artist_id from songs s join artists ar on s.artist_id = ar.artist_id where s.title = (%s) and ar.name = (%s) and s.duration = (%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
