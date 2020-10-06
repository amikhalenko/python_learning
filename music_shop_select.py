import sqlalchemy as sqlalchemy

engine = sqlalchemy.create_engine('postgresql://music:music@127.0.0.1:5432/music_shop')
engine

connection = engine.connect()
print(engine.table_names())

sel = connection.execute("""SELECT Album_name, Album_year FROM Album
WHERE Album_year = 2018;""").fetchall()
print(sel)
sel = connection.execute("""SELECT Track_name, Duration FROM Track
ORDER BY Duration DESC
LIMIT 1;""").fetchall()
print(sel)
sel = connection.execute("""SELECT Track_name FROM Track
WHERE Duration >=3.30 
;""").fetchall()
print(sel)
sel = connection.execute("""SELECT Collection_Name FROM Collection
WHERE Collection_year BETWEEN 2018 AND 2020;""").fetchall()
print(sel)
sel = connection.execute("""SELECT Name_artist FROM Artist
WHERE Name_artist NOT LIKE '%% %%';""").fetchall()
print(sel)
sel = connection.execute("""SELECT Track_name FROM Track
WHERE Track_name LIKE '%% My %%';""").fetchall()
print(sel)