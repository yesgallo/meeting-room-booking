class BookingRepository:
    def __init__(self):
        self.bookings = []

    def add(self, booking):
        self.bookings.append(booking)

    def get_all(self):
        return self.bookings
