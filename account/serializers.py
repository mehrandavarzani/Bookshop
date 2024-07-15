from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAuthSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','username','name')

    def get_name(self,obj):
        return obj.get_full_name()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )


class ReadUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','is_active',
                  'is_superuser')
