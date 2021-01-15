from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from .serializers import TokenPairSerializer, RegisterSerializer, BorrowBooksSerializer
from core.models import BookBorrowing


class ObtainTokenView(TokenObtainPairView):
    """
    API to login a user
    URL: /api/token-auth/
    @params
    username: email of the user
    password: password of the user
    """
    serializer_class = TokenPairSerializer


class RegisterView(generics.CreateAPIView):
    """
    API to register a new user
    URL: /api/register/
    @params
    email: email id of user
    password: password of user
    password2: password confirmation, must match with password
    first_name: first name of user
    last_name: last name of user
    """
    serializer_class = RegisterSerializer


class BorrowBooksAPI(generics.ListCreateAPIView):
    """
    API to create a borrowing entry and retrieve list of books borrowed by a user
    URL: /api/books/borrow/
    Methods:
        GET: returns the list of books borrowed by a user in the format
            [{
                "book": 1,
                "date": "2021-01-15"
            },
            {
                "book": 2,
                "date": "2021-01-14"
            }]
        POST: Creates an entry of borrowing for the user
            payload: {"book":2,"date":"2021-01-14"}
                book: id of the book being borrowed
                date: date of borrowing, defaults to current date if not provided
    """
    serializer_class = BorrowBooksSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return BookBorrowing.objects.filter(user=self.request.user)
