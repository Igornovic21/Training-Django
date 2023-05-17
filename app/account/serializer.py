from rest_framework import serializers

from account.models import User

class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        read_only_fields = ['id', 'date_created', 'last_login']
        fields = ["id", "email", "password", "first_name", "last_name", "is_staff", "is_active", "is_superuser", "last_login", "date_joined"]