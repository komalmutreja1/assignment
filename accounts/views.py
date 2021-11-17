from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from accounts.serializers import AuthCustomTokenSerializer, UserSerializer




class LoginView(ObtainAuthToken):
    """
    Login Authentication View
    Authenticates users against User model.
    """

    def post(self, request, *args, **kwargs):
        serializer = AuthCustomTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        message = serializer.validated_data.get('message')

        if user:
            token, created = Token.objects.get_or_create(user=user) # get existing token for a user or create a new token if it does not exists

            return Response({
                'status': True,
                'message': 'Login success.',
                'data': {
                    'user_id': user.pk,
                    'username': user.username,
                    'full_name': user.get_full_name(),
                    'token': token.key,
                }
            }, status=status.HTTP_200_OK)

        else:
            return Response({
                'status': False,
                'message': message,
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)




class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(): # checking if data provided by the user is valid
            serializer.save() # saving user to database after validating the data provided by user

            return Response({
                'status': True,
                'message': 'User registered successfully.',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
            
        else:
            return Response({
                'status': False,
                'message': serializer.errors, # returning error messages
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)