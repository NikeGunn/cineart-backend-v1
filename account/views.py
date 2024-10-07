from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer

# Create your views here.
class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           user = serializer.save()
           return Response({
            "status": "success",
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            email = serializers.data.get('email')
            password = serializers.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({
                    "status": "success",
                    "message": "User login successfully"
                }, status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {'none_field_error': ['Email or password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
