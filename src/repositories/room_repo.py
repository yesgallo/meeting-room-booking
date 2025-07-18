class RoomRepository:
    def __init__(self):
        self.rooms = {}

    def add(self, room):
        self.rooms[room.name] = room

    def get(self, name):
        return self.rooms.get(name)
