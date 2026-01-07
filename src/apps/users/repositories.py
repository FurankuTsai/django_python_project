from .models import User

class UserRepository:
    def get_all(self):
        return User.objects.all()

    def get_by_id(self, user_id: int):
        return User.objects.filter(id=user_id).first()

    def create(self, data: dict):
        return User.objects.create(**data)

    def update(self, user: User, data: dict):
        for field, value in data.items():
            setattr(user, field, value)
        user.save()
        return user

    def delete(self, user: User):
        user.delete()
