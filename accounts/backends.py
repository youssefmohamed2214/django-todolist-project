from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class EmailBackend(ModelBackend):
    """
    Custom authentication backend.

    Allows users to log in using their email address instead of a username.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 1. Find a user with the matching email.
            user = User.objects.get(email=username)

            # 2. Check if the found user's password is correct.
            if user.check_password(password):
                return user  # Success case
                
        except User.DoesNotExist:
            # 3. If no user is found, the login fails.
            return None

