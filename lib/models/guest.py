# lib/models/guest.py

from lib.database.connection import create_connection

class Guest:
    @classmethod
    def create(cls, name, nationality, room_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO guests (name, nationality, room_id) VALUES (?, ?, ?)", (name, nationality, room_id))
            guest_id = cursor.lastrowid
        return guest_id

    @classmethod
    def delete(cls, guest_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM guests WHERE id=?", (guest_id,))
            conn.commit()

    @classmethod
    def get_all(cls):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM guests")
            return cursor.fetchall()

    @classmethod
    def find_by_id(cls, guest_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM guests WHERE id=?", (guest_id,))
            return cursor.fetchone()

    @classmethod
    def update(cls, guest_id, name, nationality, room_id):
        conn = create_connection()
        with conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE guests SET name=?, nationality=?, room_id=? WHERE id=?", (name, nationality, room_id, guest_id))
            conn.commit()
