from rest_framework.serializers import ModelSerializer
from .models import Account
from rest_framework.validators import UniqueValidator

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'email', 'is_superuser']
        read_only_fields = ['id']
        extra_kwargs={
            'password': {'write_only':True},
            'username': {'validators':[UniqueValidator(queryset=Account.objects.all(),message="A user with that username already exists.")]},
            'email': {'validators':[UniqueValidator(queryset=Account.objects.all(),message="user with this email already exists.")]}
        }
    def create(self, validated_data):
        # if validated_data['is_superuser']:
        #     return Account.objects.create_superuser(**validated_data)
        return Account.objects.create_user(**validated_data)
    


        