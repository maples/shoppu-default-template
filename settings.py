import os
PROJECT_ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT_PATH, 'static')