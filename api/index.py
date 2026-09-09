import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
os.environ.setdefault("VERCEL", "1")

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

call_command("collectstatic", interactive=False, verbosity=0)
application = get_wsgi_application()
app = application
