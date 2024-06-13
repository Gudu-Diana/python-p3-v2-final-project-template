# lib/models/room.py

from lib.database.connection import create_connection

class Room:
    @classmethod
    def create(cls, room_number, hotel_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO rooms (room_number, hotel_id) VALUES (?, ?)", (room_number, hotel_id))
            room_id = cursor.lastrowid
        return room_id

    @classmethod
    def delete(cls, room_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM rooms WHERE id=?", (room_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rooms")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, room_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM rooms WHERE id=?", (room_id,))
            return cursor.fetchone()

    @classmethod
    def update(cls, room_id, room_number, hotel_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE rooms SET room_number=?, hotel_id=? WHERE id=?", (room_number, hotel_id, room_id))
            conn.commit()
