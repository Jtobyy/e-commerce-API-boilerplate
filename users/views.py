from django.contrib.auth.hashers import make_password
from rest_framework import generics, permissions
 
from .models import CustomUser
from .serializers import CustomUserSerializer
from api.permissions import IsStaffEditorPermission

# import smtplib, ssl


# User Registration 
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        # Allow users to view only their own details
        user = self.request.user    
        if user.is_staff:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)    

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data.get('password'), salt=None, hasher='default')
        # Check if user provided email, if there is, send confirmation email to user.
        email = serializer.validated_data.get('email') or None
        if email is not None:
            pass
        serializer.save(password=password)

user_list_create_view = UserListCreateAPIView.as_view()


class UserDetailUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomUserSerializer
    lookup_field = 'pk' # Could be email addresses instead or any other fields

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Allow users to view only their own details
        user = self.request.user    
        if user.is_staff:
            return CustomUser.objects.all()
        else:
            return CustomUser.objects.filter(id=user.id)

    # User has to be a staff or an admin to edit the list of all users.
    def get_object(self):
        obj = super().get_object()
        user = self.request.user
        if user.is_staff:
            return obj
        elif self.request.user != obj:
            return CustomUser.objects.none()
        return obj

    def perform_update(self, serializer):
        print(serializer.validated_data)
        password = serializer.validated_data.get('password') or None
        if password:
            hashed_password = make_password(password=password)
            serializer.save(password=hashed_password)
        else:
            serializer.save()    
        

user_detail_update_view = UserDetailUpdateAPIView.as_view()    
