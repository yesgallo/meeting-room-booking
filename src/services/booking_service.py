from models.booking import Booking
from datetime import datetime, timedelta

class BookingService:
    def __init__(self, user_service, room_service):
        self.repo = []
        self.user_service = user_service
        self.room_service = room_service

    def book_room(self, username, roomname, start, end):
        user = self.user_service.get_user(username)
        room = self.room_service.get_room(roomname)

        if not user or not room:
            return False

        try:
            start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M")
            end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M")
        except ValueError:
            return False

        now = datetime.now()

        # Nueva condición: permitir reservas desde ahora + 10 minutos
        min_start_time = now + timedelta(minutes=10)
        if start_dt < min_start_time:
            print(f"Hora de inicio inválida. Debe ser posterior a {min_start_time}")
            return False

        if end_dt <= start_dt:
            print("Hora de fin inválida. Debe ser posterior a la hora de inicio.")
            return False

        new_booking = Booking(user, room, start, end)

        for b in self.repo:
            if new_booking.overlaps(b):
                print("Conflicto de horarios con otra reserva.")
                return False

        self.repo.append(new_booking)
        print(f"Reserva creada: {username} - {roomname} - {start_dt} a {end_dt}")
        return True

    def get_bookings_by_user(self, username):
        return [b for b in self.repo if b.user.username == username]

    def get_bookings_by_room(self, roomname):
        return [b for b in self.repo if b.room.name == roomname]


