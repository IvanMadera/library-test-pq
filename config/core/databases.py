import os
import dj_database_url

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    },
    'atomic': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
    }
}

DATABASE_URL = os.environ.get(
    'DATABASE_URL', 'postgres://postgres:postgres@localhost:5432/postgres')

DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=0)

DATABASES['atomic'] = DATABASES['default']