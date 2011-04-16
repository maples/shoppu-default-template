import os
PROJECT_ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')

CURRENCIES = (
('BRL', 'Real'),
('USD', 'US Dollar'),
)