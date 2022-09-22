from django.urls import path

from . import views 


# /api/users/
urlpatterns = [
    path('', views.user_list_create_view),
    path('<int:pk>/', views.user_detail_update_view),
]