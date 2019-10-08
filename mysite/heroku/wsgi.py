"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

from mysite.base import STATIC_ROOT
from mysite.wsgi import get_wsgi_application, os
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.production')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
