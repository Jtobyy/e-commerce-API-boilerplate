from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views


# api/
urlpatterns = [
    path('auth/', obtain_auth_token),
]