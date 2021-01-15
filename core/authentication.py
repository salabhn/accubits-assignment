from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.middleware.csrf import CsrfViewMiddleware
from djforge_redis_multitokens.tokens_auth import MultiToken


class SafeJWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        authorization_heaader = request.headers.get('Authorization')

        if not authorization_heaader:
            return None
        access_token = authorization_heaader.split(' ')[1]
        user = MultiToken.get_user_from_token(access_token)
        print(user)
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')
        return (user, None)
