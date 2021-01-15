from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.views import ObtainTokenView, RegisterView, BorrowBooksAPI


urlpatterns = [
    path('token-auth/', ObtainTokenView.as_view(), name='token_obtain_pair'),
    path('token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('books/borrow/', BorrowBooksAPI.as_view(), name='borrow_books'),
]