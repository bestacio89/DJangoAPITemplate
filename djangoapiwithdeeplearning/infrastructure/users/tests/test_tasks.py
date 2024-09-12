import pytest
from celery.result import EagerResult

<<<<<<<< HEAD:DjangoAPITemplate/users/tests/test_tasks.py
from DjangoAPITemplate.users.tasks import get_users_count
from DjangoAPITemplate.users.tests.factories import UserFactory
========
from djangoapiwithdeeplearning.infrastructure.users.tasks import get_users_count
from djangoapiwithdeeplearning.infrastructure.users.tests.factories import UserFactory
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/tests/test_tasks.py

pytestmark = pytest.mark.django_db


def test_user_count(settings):
    """A basic test to execute the get_users_count Celery task."""
    batch_size = 3
    UserFactory.create_batch(batch_size)
    settings.CELERY_TASK_ALWAYS_EAGER = True
    task_result = get_users_count.delay()
    assert isinstance(task_result, EagerResult)
    assert task_result.result == batch_size
