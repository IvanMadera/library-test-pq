# Application definition

BEFORE_DJANGO_APPS = [
    # before django
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PART_APPS = [
    'django_filters',
    'rest_framework',
    'corsheaders',    
    'drf_yasg',    
]

LOCAL_APPS = [
    # local apps
    'apps.accounts',
]

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS