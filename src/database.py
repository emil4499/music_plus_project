import os
import sqlite3
from pathlib import Path

DATABASE_PATH = os.path.join(str(Path(__file__).parents[1]), "music.db")

if os.path.exists(DATABASE_PATH):
    os.remove(DATABASE_PATH)

with sqlite3.connect(DATABASE_PATH, check_same_thread=False) as conn:
    c = conn.cursor()
    c.executescript(
        """
            CREATE TABLE artist (
            artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            website TEXT,
            is_group BOOLEAN CHECK (is_group IN (0, 1))
            );
            
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Баста', 'Василий', 'Вакуленко', '777-555-1234', 'basta.ru', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Мияги', 'Александр', 'Узенюк', '777-555-5678', 'miagi.ru', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Крид', 'Егор', 'Крид', '777-555-9012', 'egorkreed.com', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Филипп Киркоров', 'Филипп', 'Киркоров', NULL, 'kirkorov.ru', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Моргенштерн', NULL, NULL, '777-555-3456', 'morgenstern.ru', true);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Jah Khalib', 'Бахтияр', 'Мансуров', '777-555-7890', 'jahkhalib.com', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Rakhim', 'Рахим', 'Магомедов', '777-555-2345', 'rakhimmusic.com', false);
            INSERT INTO artist (name, first_name, last_name, phone, website, is_group)
            VALUES ('Динамит', NULL, NULL, '777-555-6789', 'dinamit.kz', true);
            
            CREATE TABLE album (
            album_id INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            FOREIGN KEY (artist_id) REFERENCES artist(artist_id) ON DELETE CASCADE ON UPDATE CASCADE
            );
            
            INSERT INTO album (artist_id, name) VALUES (1, 'Время и Стекло');
            INSERT INTO album (artist_id, name) VALUES (1, 'Баста 2.0');
            INSERT INTO album (artist_id, name) VALUES (1, 'Город дорог');
            INSERT INTO album (artist_id, name) VALUES (2, 'Пули');
            INSERT INTO album (artist_id, name) VALUES (3, 'Я Популярный');
            INSERT INTO album (artist_id, name) VALUES (4, 'Приключения');
            INSERT INTO album (artist_id, name) VALUES (5, 'Легенда Рэпа');
            INSERT INTO album (artist_id, name) VALUES (6, 'Медина');
            INSERT INTO album (artist_id, name) VALUES (6, 'Капкан');
            INSERT INTO album (artist_id, name) VALUES (7, 'Время пришло');
            INSERT INTO album (artist_id, name) VALUES (8, 'Сила народа');
            
            CREATE TABLE song (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            album_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            duration REAL,
            UNIQUE(album_id, name) ON CONFLICT ABORT,
            FOREIGN KEY (album_id) REFERENCES album(album_id) ON DELETE CASCADE ON UPDATE CASCADE
            );
            
            INSERT INTO song (album_id, name, duration) VALUES (1, 'Город дорог', 3.19);
            INSERT INTO song (album_id, name, duration) VALUES (3, 'Время', 3.08);
            INSERT INTO song (album_id, name, duration) VALUES (4, 'Пули', 3.31);
            INSERT INTO song (album_id, name, duration) VALUES (5, 'Я Популярный', 5.47);
            INSERT INTO song (album_id, name, duration) VALUES (6, 'Приключения', 3.40);
            INSERT INTO song (album_id, name, duration) VALUES (7, 'Легенда Рэпа', 4.02);
            INSERT INTO song (album_id, name, duration) VALUES (8, 'Медина', 1.42);
            INSERT INTO song (album_id, name, duration) VALUES (9, 'Капкан', 2.47);
            INSERT INTO song (album_id, name, duration) VALUES (10, 'Время пришло', 3.11);
            INSERT INTO song (album_id, name, duration) VALUES (11, 'Сила народа', 3.58);           
        """
    )