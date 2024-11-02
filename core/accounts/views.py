from django.shortcuts import render
from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class=AuthenticationForm

    # dige be safhe login barnagarde va bere be safhe marboot be next login
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    pass