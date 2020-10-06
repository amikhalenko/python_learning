import sqlalchemy as sqlalchemy

engine = sqlalchemy.create_engine('postgresql://music:music@127.0.0.1:5432/music_shop')
engine

connection = engine.connect()
print(engine.table_names())
insert = connection.execute("""INSERT INTO Artist (Name_artist)
VALUES ('Алиса'), ('Pink Floyd'), ('Michael Jackson'), ('Louis Armstrong'), ('Antonio Vivaldi'), ('Jean Michel Jarre'), ('Владимир Высоцкий'), ('Ennio Morricone');""")

insert = connection.execute("""INSERT INTO Genre (Name_genre)
VALUES ('Rock'), ('Pop'), ('Jazz'), ('Classic'), ('Electonic music'), ('Techno'), ('Bard'), ('Spagetti Vestern');""")

insert = connection.execute("""INSERT INTO Album (Album_name, Album_year)
VALUES ('Посолонь', 2019), ('The Division Bell', 1994), ('Dangerous', 1991), ('Hello, Dolly!', 1963), ('The Four Seasons', 2020 ), ('Equinox Infinity', 2018), ('Лирические песни', 2002), ('The Very Best Of', 1993);""")

insert = connection.execute("""INSERT INTO Track (Track_Name, Duration, Album_ID)
VALUES ('Пуля', 4.09, 1), ('Сверх', 5.44, 1), ('Раскол', 6.00, 1), ('High Hopes', 8.34, 2), ('Cluster One', 5.57, 2), ('What Do You Want From Me', 4.22, 2), ('Give In To Me', 5.29, 3), ('Gone Too Soon', 3.23, 3), ('Dangerous', 6.58, 3), ('Hello, Dolly!', 2.24, 4), ('Moon River', 3.00, 4), ('Someday', 3.41, 4), ('Concerto, in A Major, Allegro molto', 2.48, 5), ('Concerto, in A Major, Andante', 2.48, 5), ('Concerto, in A Major, Allegro', 2.48, 5), ('One & one', 3.54, 6), ('Bad Hair Day', 3.52, 6), ('A Fact', 4.12, 6), ('Дорога, дорога', 2.14, 7), ('Ноль семь', 2.30, 7), ('Городской романс', 2.55, 7), ('Allein gegen die Mafia: My Heart and I', 5.11, 8), ('Red Sonja', 2.44, 8), ('1900: Romanze', 3.57, 8);""")

insert = connection.execute("""INSERT INTO Collection (Collection_Name, Collection_year)
VALUES ('Легенды русского рока', 1997), ('Мы вместе ХХ лет', 2005), ('Pink Floyd - Greatest Hits', 2009), ('Louis Armstrong - Greatest hits', 2008), ('Michael Jackson - Collection', 2017), ('Антонио Вивальди (A. Vivaldi)-Лучшие произведения', 2005), ('Jean Michel Jarre - The Best Of', 2017), ('Владимир Высоцкий - Высоцкий 80', 2018), ('Ennio Morricone - Io, Ennio Morricone (Film Music)', 2020);""")

insert = connection.execute("""INSERT INTO Genre_Artist (Artist_ID, Genre_ID)
VALUES (1, 1), (2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (6, 6), (7, 7), (8, 8);""")

insert = connection.execute("""INSERT INTO Artist_Album (Artist_ID, Album_ID)
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8);""")

insert = connection.execute("""INSERT INTO Collection_Track (Collection_ID, Track_ID)
VALUES (3, 4), (8, 20), (4, 10), (9, 23);""")
