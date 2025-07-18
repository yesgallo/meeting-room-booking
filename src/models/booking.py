from datetime import datetime

class Booking:
    def __init__(self, user, room, start_time, end_time):
        self.user = user
        self.room = room
        self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        self.end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M")

    def overlaps(self, other):
        return (
            self.room.name == other.room.name and
            self.start_time < other.end_time and
            self.end_time > other.start_time
        )

    def __str__(self):
        return f"{self.user.username} reservó {self.room.name} de {self.start_time} a {self.end_time}"

