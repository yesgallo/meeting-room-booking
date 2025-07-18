class UserRepository:
    def __init__(self):
        self.users = {}

    def add(self, user):
        self.users[user.username] = user

    def get(self, username):
        return self.users.get(username)
