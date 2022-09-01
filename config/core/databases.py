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
    'postgres://paramq:MbuLlvLjgz2asnTDfs6TCWX9lshbi8EE@dpg-cc7uol4gqg4fs9crb140-a/testdb_4xr4')

DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=600)

DATABASES['atomic'] = DATABASES['default']