<<<<<<<< HEAD:DjangoAPITemplate/users/tests/test_models.py
from DjangoAPITemplate.users.models import User
========
from djangoapiwithdeeplearning.infrastructure.users.models import User
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/tests/test_models.py


def test_user_get_absolute_url(user: User):
    assert user.get_absolute_url() == f"/users/{user.pk}/"
