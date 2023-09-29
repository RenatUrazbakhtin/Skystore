from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserConfirmEmailView, EmailConfirmationSentView, generate_password, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm-email/<str:token>/', UserConfirmEmailView.as_view(), name='email_verified'),
    path('email-sent/', EmailConfirmationSentView.as_view(), name='email_sent'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/changed_password/', generate_password, name='changed_password'),
]