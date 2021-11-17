from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.backends import ModelBackend
from utils.core.customModelSerializer import CustomDynamicFieldsModelSerializer, CustomNestedSerializerField




class UserSerializer(CustomDynamicFieldsModelSerializer):
    """
    User Serializer 
    Validates data provided by user and creates user object accordingly.
    """
    full_name = serializers.SerializerMethodField(read_only=True)
    user_id = serializers.IntegerField(read_only=True, source='id') # renaming id field as user_id, since it will be helpful further


    class Meta:
        model = User
        fields = ('user_id', 'first_name', 'last_name', 'username', 'password', 'full_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True}, 'first_name': {'required': True}, 'last_name': {'required': True}, 'username': {'required': True}}


    def create(self, validated_data): # create method for creating new user in database
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user) # creating token object for this newly created user
        return user

    def get_full_name(self, obj):
        return obj.get_full_name()

    


class AuthCustomTokenSerializer(serializers.Serializer):
    """
    Login Authentication Serializer
    Authenticates a user against User model. 
    """

    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})


    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            try:
                user_request = User.objects.get(username=username) # checking if user exists with provided username
            except:
                user_request = None	
            if user_request:
                user = ModelBackend().authenticate(self.context.get('request'), username=username, password=password) # authenticating the user with provided credentials
                if user:
                    if not user.is_active:
                        attrs['message'] = 'User account is disabled.'
                    else:
                        attrs['user'] = user
                else:
                    attrs['message'] = 'Incorrect password for this username.'
            else:
                attrs['message'] = "This username isn't registered."
        else:
            attrs['message'] = 'Must include "username" and "password".'
            
        return attrs

