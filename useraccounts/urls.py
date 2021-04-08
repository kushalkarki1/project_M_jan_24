from django.urls import path
from django.contrib.auth.views import LogoutView
from useraccounts.views import signup_view, UserLoginView, send_confirm_email

app_name = "user"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("register/", signup_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("send-mail/", send_confirm_email, name="send_email"),
]