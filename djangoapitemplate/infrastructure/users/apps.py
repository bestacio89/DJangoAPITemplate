import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "djangoapitemplate.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
<<<<<<<< HEAD:DjangoAPITemplate/users/apps.py
            import djangoapitemplate.users.signals  # noqa: F401
========
            import djangoapitemplate.infrastructure.users.signals  # noqa: F401
>>>>>>>> main:djangoapiwithdeeplearning/infrastructure/users/apps.py
