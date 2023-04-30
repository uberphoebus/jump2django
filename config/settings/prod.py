import environ
from config.settings.base import *

ALLOWED_HOSTS = ['3.34.50.123']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False


env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'), # DB명
        'USER': env('DB_USER'), # 데이터베이스 계정
        'PASSWORD': env('DB_PASSWORD'), # 계정 비밀번호
        'HOST': env('DB_HOST'), # 데이테베이스 주소(IP)
        'PORT': '5432', # 데이터베이스 포트(보통은 5432)
    }
}

