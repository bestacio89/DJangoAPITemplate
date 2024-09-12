import pytest

from djangoapiwithdeeplearning.infrastructure.users import User
from djangoapiwithdeeplearning.infrastructure.users import UserFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture()
def user(db) -> User:
    return UserFactory()
