import sqlite3
from contextlib import closing

DB_PATH = 'lib/database/hotel.db'

def create_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    with create_connection() as conn:
        with closing(conn.cursor()) as cursor:
            # Create tables if they don't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY,
                    name TEXT
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rooms (
                    id INTEGER PRIMARY KEY,
                    room_number INTEGER,
                    hotel_id INTEGER,
                    FOREIGN KEY(hotel_id) REFERENCES hotels(id)
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS guests (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    nationality TEXT,
                    room_id INTEGER,
                    FOREIGN KEY(room_id) REFERENCES rooms(id)
                )
            ''')
            conn.commit()
