"""WSGI configuration required to serve up your Django app"""
import sys
from mysite.wsgi import get_wsgi_application, os

# Add your project directory to the sys.path
settings_path = '/home/leonardocaballero/djangogirls_mysite'
sys.path.insert(0, settings_path)

# Set environment variable to tell django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.pythonanywhere.settings'

# Set the 'application' variable to the Django wsgi app
application = get_wsgi_application()
