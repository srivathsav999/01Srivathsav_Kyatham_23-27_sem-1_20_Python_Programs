from datetime import datetime, timedelta

class Room:
    def __init__(self, room_number, capacity, rate_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.rate_per_night = rate_per_night
        self.reservations = []

    def check_availability(self, start_date, end_date):
        for reservation in self.reservations:
            if start_date < reservation.check_out_date and end_date > reservation.check_in_date:
                return False  # Room is not available during the specified time period
        return True  # Room is available

    def book_room(self, guest, check_in_date, check_out_date):
        if self.check_availability(check_in_date, check_out_date):
            reservation = Reservation(guest, self, check_in_date, check_out_date)
            self.reservations.append(reservation)
            guest.add_reservation(reservation)
            print(f"Room {self.room_number} booked successfully for {guest.name}.")
            return True
        else:
            print(f"Room {self.room_number} is not available during the specified time period.")
            return False


class Guest:
    def __init__(self, guest_id, name, email):
        self.guest_id = guest_id
        self.name = name
        self.email = email
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def calculate_total_cost(self):
        nights = (self.check_out_date - self.check_in_date).days
        return nights * self.room.rate_per_night


# Example usage:

# Create rooms
room1 = Room(room_number="101", capacity=2, rate_per_night=100)
room2 = Room(room_number="102", capacity=4, rate_per_night=150)

# Create guests
guest1 = Guest(guest_id=1, name="Alice", email="alice@example.com")
guest2 = Guest(guest_id=2, name="Bob", email="bob@example.com")

# Check room availability
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 1, 5)

available = room1.check_availability(start_date, end_date)
if available:
    print(f"Room {room1.room_number} is available during the specified time period.")
else:
    print(f"Room {room1.room_number} is not available during the specified time period.")

# Book room
room1.book_room(guest1, start_date, end_date)

# Calculate total cost for a reservation
reservation = guest1.reservations[0]
total_cost = reservation.calculate_total_cost()
print(f"Total cost for the reservation: ${total_cost}")
