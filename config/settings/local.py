import sys
from .base import *  # noqa: F403

DEBUG = True

# Development email backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if "pytest" in sys.modules:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }
