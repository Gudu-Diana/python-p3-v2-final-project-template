# lib/helpers.py

def validate_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def validate_string_input(prompt):
    while True:
        value = input(prompt)
        if value.strip():
            return value.strip()
        else:
            print("Input cannot be empty. Please try again.")

def format_guest_info(guest):
    return f"ID: {guest.id}, Name: {guest.name}, Nationality: {guest.nationality}, Room ID: {guest.room_id}"

def format_hotel_info(hotel):
    return f"ID: {hotel.id}, Name: {hotel.name}"

def format_room_info(room):
    return f"ID: {room.id}, Room Number: {room.room_number}, Hotel ID: {room.hotel_id}"

def exit_program():
    print("Goodbye!")
    exit()
