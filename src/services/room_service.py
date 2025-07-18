from models.room import Room
from repositories.room_repo import RoomRepository

class RoomService:
    def __init__(self):
        self.repo = RoomRepository()

    def create_room(self, name):
        room = Room(name)
        self.repo.add(room)

    def get_room(self, name):
        return self.repo.get(name)
