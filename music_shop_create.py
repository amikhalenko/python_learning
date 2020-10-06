import sqlalchemy as sqlalchemy

engine = sqlalchemy.create_engine('postgresql://music:music@127.0.0.1:5432/music_shop')
engine

connection = engine.connect()


create = connection.execute("""CREATE TABLE IF NOT EXISTS Genre (ID serial primary key, Name_genre varchar(20) not null unique);""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Artist (ID serial primary key, Name_artist varchar(40) not null unique);""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Album (ID serial primary key, Album_name varchar(50) not null, Album_year integer not null);""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Genre_Artist (Genre_ID integer references Genre(ID), Artist_ID integer references Artist(ID), constraint pk_genre_artist primary key (Genre_ID, Artist_ID));""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Artist_Album (Artist_ID integer references Artist(ID), Album_ID integer references Album(ID), constraint pk_artist_album primary key (Artist_ID, Album_ID));""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Collection (ID serial primary key, Collection_name varchar(50) not null, Collection_year integer not null);""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Track (ID serial primary key, Track_name varchar(100) not null, Duration numeric not null, Album_id integer references Album(ID));""")
create = connection.execute("""CREATE TABLE IF NOT EXISTS Collection_Track (Collection_ID integer references Collection(ID), Track_ID integer references Track(ID), constraint pk_collection_track primary key (Collection_ID, Track_ID));""")

print(engine.table_names())