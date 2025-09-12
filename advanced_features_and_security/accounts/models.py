from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser that handles extra fields: date_of_birth and profile_photo.
    """

    def create_user(self, username, email, date_of_birth=None, profile_photo=None, password=None, **extra_fields):
        """
        Create and save a regular user with the given username, email, date_of_birth, and profile_photo.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth=None, profile_photo=None, password=None, **extra_fields):
        """
        Create and save a superuser. Must set is_staff=True and is_superuser=True.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, profile_photo, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    Custom user model extending AbstractUser to include date_of_birth and profile_photo.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    # Optionally override string representation
    def __str__(self):
        return self.username

# Example model with custom permissions:

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, related_name='articles')
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ("can_view_article", "Can view article"),
            ("can_create_article", "Can create article"),
            ("can_edit_article", "Can edit article"),
            ("can_delete_article", "Can delete article"),
        ]

    def __str__(self):
        return self.title
