from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from .models import User

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        return User.objects.filter(email=username,password=password).first()

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None