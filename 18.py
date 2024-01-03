from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        for reservation in self.reservations:
            if start_time < reservation.end_time and end_time > reservation.start_time:
                return False  # Room is not available during the specified time slot
        return True  # Room is available

    def book_room(self, user, start_time, end_time):
        if self.check_availability(start_time, end_time):
            reservation = Reservation(user, start_time, end_time)
            self.reservations.append(reservation)
            user.add_reservation(reservation)
            print(f"Room {self.room_number} booked successfully by {user.username}.")
            return True
        else:
            print(f"Room {self.room_number} is not available during the specified time slot.")
            return False


class Reservation:
    def __init__(self, user, start_time, end_time):
        self.user = user
        self.start_time = start_time
        self.end_time = end_time


class User:
    def __init__(self, username):
        self.username = username
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def send_notification(self, message):
        print(f"Notification sent to {self.username}: {message}")


# Example usage:

# Create rooms
room1 = Room(room_number="101", capacity=10)
room2 = Room(room_number="102", capacity=15)

# Create users
user1 = User(username="Alice")
user2 = User(username="Bob")

# Check room availability
start_time = datetime(2023, 1, 1, 9, 0)
end_time = datetime(2023, 1, 1, 10, 0)

available = room1.check_availability(start_time, end_time)
if available:
    print(f"Room {room1.room_number} is available during the specified time slot.")
else:
    print(f"Room {room1.room_number} is not available during the specified time slot.")

# Book room
room1.book_room(user=user1, start_time=start_time, end_time=end_time)

# Send notification to the user
user1.send_notification("Your reservation has been confirmed.")

# Display user's reservations
print(f"{user1.username}'s Reservations:")
for reservation in user1.reservations:
    print(f"Room {room.room_number} - {reservation.start_time} to {reservation.end_time}")
