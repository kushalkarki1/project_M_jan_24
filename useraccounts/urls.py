from django.urls import path
from useraccounts.views import login_view

app_name = "user"

urlpatterns = [
    path("login/", login_view, name="login"),
]