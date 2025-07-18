from models.user import User
from repositories.user_repo import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, username):
        user = User(username)
        self.repo.add(user)

    def get_user(self, username):
        return self.repo.get(username)
