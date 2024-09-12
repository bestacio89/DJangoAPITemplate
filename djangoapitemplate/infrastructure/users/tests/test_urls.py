from django.urls import resolve
from django.urls import reverse

<<<<<<<< HEAD:DjangoAPITemplate/users/tests/test_urls.py
from djangoapitemplate.users.models import User
========
from djangoapitemplate.infrastructure.users.models import User
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/tests/test_urls.py


def test_detail(user: User):
    assert reverse("users:detail", kwargs={"pk": user.pk}) == f"/users/{user.pk}/"
    assert resolve(f"/users/{user.pk}/").view_name == "users:detail"


def test_update():
    assert reverse("users:update") == "/users/~update/"
    assert resolve("/users/~update/").view_name == "users:update"


def test_redirect():
    assert reverse("users:redirect") == "/users/~redirect/"
    assert resolve("/users/~redirect/").view_name == "users:redirect"
