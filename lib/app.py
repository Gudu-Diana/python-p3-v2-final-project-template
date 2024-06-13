# lib/app.py

from lib.models.guest import Guest
from lib.models.room import Room
from lib.helpers import validate_integer_input, validate_string_input

def main_menu():
    print("Welcome to the Hotel Management System")
    print("1. Manage Guests")
    print("2. Manage Rooms")
    print("3. Exit")

def guest_menu():
    while True:
        print("\nGuest Management Menu")
        print("1. Add Guest")
        print("2. Delete Guest")
        print("3. View All Guests")
        print("4. Return to Main Menu")
        choice = validate_integer_input("Enter your choice: ")

        if choice == 1:
            add_guest()
        elif choice == 2:
            delete_guest()
        elif choice == 3:
            view_all_guests()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def room_menu():
    while True:
        print("\nRoom Management Menu")
        print("1. Add Room")
        print("2. Delete Room")
        print("3. View All Rooms")
        print("4. Return to Main Menu")
        choice = validate_integer_input("Enter your choice: ")

        if choice == 1:
            add_room()
        elif choice == 2:
            delete_room()
        elif choice == 3:
            view_all_rooms()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

def add_guest():
    name = validate_string_input("Enter guest name: ")
    nationality = validate_string_input("Enter guest nationality: ")
    room_id = validate_integer_input("Enter room ID: ")
    Guest.create(name, nationality, room_id)
    print("Guest added successfully.")

def delete_guest():
    guest_id = validate_integer_input("Enter guest ID to delete: ")
    Guest.delete(guest_id)
    print("Guest deleted successfully.")

def view_all_guests():
    guests = Guest.get_all()
    if guests:
        for guest in guests:
            print(f"ID: {guest['id']}, Name: {guest['name']}, Nationality: {guest['nationality']}, Room ID: {guest['room_id']}")
    else:
        print("No guests found.")

def add_room():
    room_number = validate_integer_input("Enter room number: ")
    hotel_id = validate_integer_input("Enter hotel ID: ")
    Room.create(room_number, hotel_id)
    print("Room added successfully.")

def delete_room():
    room_id = validate_integer_input("Enter room ID to delete: ")
    Room.delete(room_id)
    print("Room deleted successfully.")

def view_all_rooms():
    rooms = Room.get_all()
    if rooms:
        for room in rooms:
            print(f"ID: {room['id']}, Room Number: {room['room_number']}, Hotel ID: {room['hotel_id']}")
    else:
        print("No rooms found.")

def run_cli():
    while True:
        main_menu()
        choice = validate_integer_input("Enter your choice: ")

        if choice == 1:
            guest_menu()
        elif choice == 2:
            room_menu()
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_cli()
