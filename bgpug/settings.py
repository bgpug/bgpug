import os

PROJECT_PATH = os.path.abspath(os.path.join(__file__, '../../'))
project = lambda x: os.path.join(PROJECT_PATH, x)

DEBUG = bool(os.environ.get('DEBUG'))
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
    }
}

SITE_ID = 1

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split()

LANGUAGE_CODE = 'bg'

LANGUAGES = (
    ('bg', 'Bulgarian'),
)

USE_I18N = True

USE_L10N = False

USE_TZ = True

TIME_ZONE = 'Europe/Sofia'

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', project('media/'))

MEDIA_URL = '/media/'

STATIC_ROOT = os.environ.get('STATIC_ROOT', project('static/'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    project('bgpug/static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE = True

PIPELINE_CSS = {
    'bgpug': {
        'source_filenames': (
        ),
        'output_filename': 'bgpug.min.css',
    },
}

PIPELINE_JS = {
    'bgpug': {
        'source_filenames': (
        ),
        'output_filename': 'bgpug.min.js',
    },
}


PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

SECRET_KEY = os.environ.get('SECRET_KEY', 'secret_key')

TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    project('bgpug/templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

ROOT_URLCONF = 'bgpug.urls'

WSGI_APPLICATION = 'bgpug.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django_comments',
    'mptt',
    'tagging',
    'tinymce',
    'sorl.thumbnail',
    'mce_filebrowser',
    'zinnia_bootstrap',
    'zinnia',
    'pipeline',
    'bgpug',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'table,spellchecker,paste,searchreplace',
    'theme': 'advanced',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'file_browser_callback': 'mce_filebrowser',
}

ZINNIA_PING_EXTERNAL_URLS = False

ZINNIA_SAVE_PING_DIRECTORIES = False

ZINNIA_PAGINATION = 100

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'log_file_debug': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('LOG_FILE', project('main.log')),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
        },
        'log_file_errors': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.environ.get('LOG_FILE_ERROR', project('error.log')),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'log_file_debug'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['log_file_errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar',
        'django_extensions',
        'djangobower',
    )

    STATICFILES_FINDERS += (
        'djangobower.finders.BowerFinder',
    )

    BOWER_COMPONENTS_ROOT = PROJECT_PATH

    BOWER_INSTALLED_APPS = (
        'jquery#2.1.1',
        'bootstrap#3.2.0',
        'font-awesome#4.1.0',
    )

else:
    INSTALLED_APPS += (
        'raven.contrib.django.raven_compat',
    )

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    )

    RAVEN_CONFIG = {
        'dsn': os.environ.get('RAVEN_CONFIG_DSN'),
    }
