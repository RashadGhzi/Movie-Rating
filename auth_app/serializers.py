from rest_framework import serializers
from auth_app.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, min_length=4, max_length=100)
    password_confirmation = serializers.CharField(
        write_only=True, required=True, min_length=4, max_length=100)

    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'email',
                  'password', 'password_confirmation')

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        new_user = User.objects.create(**validated_data)
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password": "XXXXXXXXX don't match."})
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"email": "XXXXXXXXX already exists."})
        return value


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, min_length=4, max_length=100)

    def validate(self, attrs):
        return attrs
