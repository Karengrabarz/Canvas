
from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.views import ListCreateAccountView, LoginView


urlpatterns = [
    path("accounts/", ListCreateAccountView.as_view()),
    path('login/', LoginView.as_view()),
]