from pathlib import Path
import os
import dj_database_url
from django_storage_url import dsn_configured_storage_class


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY', '<a string of random characters>')
DEBUG = os.environ.get('DEBUG', False) == 'True'
DEVELOP = os.environ.get('DEVELOP', False) == 'True'
ALLOWED_HOSTS = [os.environ.get('DOMAIN'),]
if DEBUG:
    ALLOWED_HOSTS = ["*", "ayudate-fundacion-develop-f037f7ceb296.herokuapp.com"]

SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT') != "False"
X_FRAME_OPTIONS = 'SAMEORIGIN'


INSTALLED_APPS = [
    'backend',
    'storages',
    # optional, but used in most projects
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # key django CMS modules
    'cms',
    'menus',
    'treebeard',
    'sekizai',

    # Django Filer - optional, but used in most projects
    'filer',
    'easy_thumbnails',

    # the default publishing implementation - optional, but used in most projects
    'djangocms_versioning',

    # the default alias content - optional, but used in most projects
    'djangocms_alias',
    'parler',

    # the default CKEditor - optional, but used in most projects
    'djangocms_text_ckeditor',

    # optional django CMS frontend modules
    'djangocms_frontend',
    'djangocms_frontend.contrib.accordion',
    'djangocms_frontend.contrib.alert',
    'djangocms_frontend.contrib.badge',
    'djangocms_frontend.contrib.card',
    'djangocms_frontend.contrib.carousel',
    'djangocms_frontend.contrib.collapse',
    'djangocms_frontend.contrib.content',
    'djangocms_frontend.contrib.grid',
    'djangocms_frontend.contrib.jumbotron',
    'djangocms_frontend.contrib.link',
    'djangocms_frontend.contrib.listgroup',
    'djangocms_frontend.contrib.media',
    'djangocms_frontend.contrib.icon',
    'djangocms_frontend.contrib.image',
    'djangocms_frontend.contrib.tabs',
    'djangocms_frontend.contrib.utilities',


]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]
ROOT_URLCONF = 'backend.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.i18n',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',

            ],
        },
    },
]
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
CMS_TEMPLATES = [
    ('minimal.html', 'Minimal template'),
    ('bootstrap5.html', 'Bootstrap 5 Demo'),
    ('whitenoise-static-files-demo.html', 'Static File Demo'),
    ('home.html', 'Home Template'),
    ('tac.html', 'Tac Template'),
    ('prevencion.html', 'Prevencion Template'),
]
WSGI_APPLICATION = 'backend.wsgi.application'
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://:memory:')
DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

CMS_CONFIRM_VERSION4 = True
DJANGOCMS_VERSIONING_ALLOW_DELETING_VERSIONS = True

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'ayudate-web'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'backend/static'),
]
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'backend/static'),)
DEFAULT_FILE_STORAGE = 'backend.filer_backends.storages.MediaStorage'
MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'data/media'), ]
MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
CMS_MEDIA_URL = 'https://%s/%s/data/media/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIAFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'data/media/')
if DEVELOP is False:
    STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = 'backend.filer_backends.storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'backend.filer_backends.storages.MediaStorage'
    MEDIAFILES_DIRS = [os.path.join(BASE_DIR, 'data/media'), ]
    MEDIA_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    CMS_MEDIA_URL = 'https://%s/%s/data/media/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    MEDIAFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'data/media/')
print(f'DEBUG {DEBUG} - DEVELOP {DEVELOP}')