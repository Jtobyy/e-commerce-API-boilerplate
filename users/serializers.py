from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = [ # Serialize and display all fields
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone_number',
            'address',
            'city',
            'state',
            'country',
            'profile_picture',
        ]

    def get_id(self, obj):
        return obj.id