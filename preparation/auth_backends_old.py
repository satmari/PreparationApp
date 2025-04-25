from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class UsernameOnlyAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Reject usernames containing '@'
        if '@' in username:
            return None

        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
