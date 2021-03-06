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

TAGGIT_CASE_INSENSITIVE = True

try:
    from .local import *
except ImportError:
    pass
