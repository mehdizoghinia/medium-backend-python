from .base import *  # noqa
from .base import env

ADMINS = [("Mehdi Zoghinia", "mehdizowghi@gmail.com")]

# TODO add domain names of the production server
CSRF_TRUSTED_ORIGINS = []

DEFAULT_FROM_EMAIL = env(
    
    "DJANGO_DEFAULT_FROM_EMAIL",
    default="Authors Haven Support <support@trainingwebdev.com>",
)
