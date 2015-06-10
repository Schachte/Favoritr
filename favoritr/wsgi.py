"""
WSGI config for favoritr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "favoritr.settings")

application = get_wsgi_application(DjangoWhiteNoise)
=======

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "favoritr.settings")

application = get_wsgi_application()
>>>>>>> ed78a14ef7596ba3f0ade075f760d5b486bdc2f8
