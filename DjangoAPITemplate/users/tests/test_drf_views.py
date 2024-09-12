import pytest
from rest_framework.test import APIRequestFactory

<<<<<<<< HEAD:DjangoAPITemplate/users/tests/test_drf_views.py
from DjangoAPITemplate.users.api.views import UserViewSet
from DjangoAPITemplate.users.models import User
========
from djangoapiwithdeeplearning.infrastructure.users.api.views import UserViewSet
from djangoapiwithdeeplearning.infrastructure.users.models import User
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/tests/test_drf_views.py


class TestUserViewSet:
    @pytest.fixture()
    def api_rf(self) -> APIRequestFactory:
        return APIRequestFactory()

    def test_get_queryset(self, user: User, api_rf: APIRequestFactory):
        view = UserViewSet()
        request = api_rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, api_rf: APIRequestFactory):
        view = UserViewSet()
        request = api_rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)  # type: ignore[call-arg, arg-type, misc]

        assert response.data == {
            "url": f"http://testserver/api/users/{user.pk}/",
            "name": user.name,
        }
