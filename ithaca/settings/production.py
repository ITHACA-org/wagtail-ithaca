from .base import *

DEBUG = False

TAGGIT_CASE_INSENSITIVE = True

try:
    from .local import *
except ImportError:
    pass
