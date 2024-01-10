from rest_framework_simplejwt.views import TokenObtainPairView
from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework.generics import CreateAPIView

class LoginView(TokenObtainPairView):
    ...

class ListCreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer