from .base import *

DEBUG = False

INSTALLED_APPS += (
    'wagtail.contrib.postgres_search',
)

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.contrib.postgres_search.backend',
    },
}

try:
    from .local import *
except ImportError:
    pass
