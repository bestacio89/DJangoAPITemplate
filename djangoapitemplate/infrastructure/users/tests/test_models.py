<<<<<<<< HEAD:DjangoAPITemplate/users/tests/test_models.py
from djangoapitemplate.users.models import User
========
from djangoapitemplate.infrastructure.users.models import User
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/tests/test_models.py


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.pk}/"
