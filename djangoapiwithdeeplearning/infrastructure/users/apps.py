import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "DjangoAPITemplate.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
<<<<<<<< HEAD:DjangoAPITemplate/users/apps.py
            import DjangoAPITemplate.users.signals  # noqa: F401
========
            import djangoapiwithdeeplearning.infrastructure.users.signals  # noqa: F401
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/apps.py
