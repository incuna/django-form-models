#! /usr/bin/env python
"""From http://stackoverflow.com/a/12260597/400691"""
import sys

from colour_runner.django_runner import ColourRunnerMixin
from django.conf import settings

import dj_database_url


settings.configure(
    DATABASES={
        'default': dj_database_url.config(default='postgres://localhost/django_form_models'),
    },
    DEFAULT_FILE_STORAGE='inmemorystorage.InMemoryStorage',
    INSTALLED_APPS=(
        # Put contenttypes before auth to work around test issue.
        # See: https://code.djangoproject.com/ticket/10827#comment:12
        'django.contrib.sites',
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.admin',

        # Added for templates
        'crispy_forms',
        'form_models',
    ),
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',),
)

import django
if django.VERSION >= (1, 7):
    django.setup()
try:
    from django.test.runner import DiscoverRunner
except ImportError:
    from discover_runner.runner import DiscoverRunner

class TestRunner(ColourRunnerMixin, DiscoverRunner):
    pass


test_runner = TestRunner(verbosity=1)
failures = test_runner.run_tests(['form_models'])
if failures:
    sys.exit(1)
