from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .validators import phone_regex


# Path to store user images
def user_directory_path(instance, filename): 
    return 'user_{0}/{1}'.format(instance.id, filename) 
# Custom User model
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=False)    
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)    
    address = models.CharField(_('address'), max_length=255)
    city = models.CharField(_('city'), max_length=85)
    state = models.CharField(_('state'), max_length=85)
    country = models.CharField(_('country'), max_length=150)
    date = models.DateTimeField(_('registration date'), auto_now_add=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, null=True)


