import os
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent / 'admin'
sys.path.insert(0, str(PROJECT_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')

from admin.wsgi import application

app = application
