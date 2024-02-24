from django.urls import path
from .views import LoginView, SignupView, UserLogoutView

app_name = "user"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
