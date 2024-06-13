import sqlite3
from lib.database.connection import create_connection

class Hotel:
    @classmethod
    def create(cls, name):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO hotels (name) VALUES (?)", (name,))
            hotel_id = cursor.lastrowid
        return hotel_id

    @classmethod
    def delete(cls, hotel_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hotels WHERE id=?", (hotel_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hotels")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, hotel_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM hotels WHERE id=?", (hotel_id,))
            return cursor.fetchone()
