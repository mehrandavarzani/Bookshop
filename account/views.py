from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from . import serializers
from rest_framework.authtoken.models import Token
from .authentication import token_expire_handler, expires_in
from django.contrib.auth import authenticate


class Login(APIView):
    permission_classes = [AllowAny,]

    def post(self,request,format=None):
        login_serializer = serializers.UserLoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return Response(login_serializer.errors,400)

        user = authenticate(
            username=login_serializer.data['username'],
            password=login_serializer.data['password']
        )
        if not user:
            return Response({'detail':['Invalid Credentials or inactive account']},401)

        # TOKEN STUFF
        token, _ = Token.objects.get_or_create(user=user)

        # token_expire_handler will check, if the token is expired it will generate new one
        is_expired, token = token_expire_handler(token)  # The implementation will be described further
        user_serialized = serializers.UserAuthSerializer(user)

        return Response({
            'user': user_serialized.data,
            'expires_in': expires_in(token),
            'token': token.key,
        }, 200)


def delete_token(user):
    try:
        token = Token.objects.get(user=user)
        token.delete()
    except Token.DoesNotExist:
        pass
    return


class Logout(APIView):
    permission_classes = [IsAuthenticated,]

    def post(self,request,format=None):
        delete_token(request.user)
        return Response({'detail':['Logged out']})
