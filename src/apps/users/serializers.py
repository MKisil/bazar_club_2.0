from django.utils.translation import gettext_lazy as _

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
from allauth.account import app_settings as allauth_account_settings
from rest_framework import serializers


class CustomLoginSerializer(LoginSerializer):
    username = None


class CustomRegisterSerializer(RegisterSerializer):
    username = None

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and EmailAddress.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    _('A user is already registered with this e-mail address.'),
                )
        return email


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        extra_fields = UserDetailsSerializer.Meta.extra_fields + ['phone']
        fields = ('pk', *extra_fields)
