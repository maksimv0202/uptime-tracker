from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('The username field must be set')

        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password, **kwargs):
        if not password:
            raise ValueError('Superusers must have a password')

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if not kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')

        if not kwargs.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(username, password, **kwargs)
