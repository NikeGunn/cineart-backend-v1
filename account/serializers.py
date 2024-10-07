from rest_framework import serializers
from account.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # Validating password and confirm password fields
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords and confirm passwords must match")
        return attrs
    
    # Creating user
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)