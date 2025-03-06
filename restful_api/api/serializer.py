from rest_framework import serializers
from .models import User


# Create a serializer class
# This class will convert the model into JSON format
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'