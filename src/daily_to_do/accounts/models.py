from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models import EmailField, CharField, BooleanField, DateTimeField
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, name=None,
                     full_name=None, is_active=None, is_staff=None, is_admin=None):
        if not email:
            raise ValueError("Пользователь должен иметь email")
        if not password:
            raise ValueError("Пользователь должен иметь пароль")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, full_name=full_name)
        user.password = make_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email=None, password=None,  name=None):
        user = self.create_user(email, name=name, password=password, is_staff=True)
        return user


class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=255)
    full_name = CharField(max_length=255, blank=True, null=True)
    name = CharField(max_length=255, blank=True, null=True)
    staff = BooleanField(default=False)
    is_active = BooleanField(default=False)
    admin = BooleanField(default=False)
    timestamp = DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []