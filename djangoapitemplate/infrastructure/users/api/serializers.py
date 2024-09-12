from rest_framework import serializers

<<<<<<<< HEAD:DjangoAPITemplate/users/api/serializers.py
from djangoapitemplate.users.models import User
========
from djangoapitemplate.infrastructure.users.models import User
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/api/serializers.py


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
