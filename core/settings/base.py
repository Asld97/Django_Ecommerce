"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-0cao=$2bph#yr0i68nwjwzf&g!0f8g-ar%zim0i&)br8t_k^cy"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "yourdomain.com",
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "basket",
    "store",
    "account",
    "orders",
    "mptt",
    "checkout",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Media Config
MEDIA_URL = "/media/"  # makes media accessible over HTTP
MEDIA_ROOT = os.path.join(
    BASE_DIR, "media/"
)  # Path to the filesystem to the directory containing static meedia
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

# Basket session Id
BASKET_SESSION_ID = "basket"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Custom user model
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login"

# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Stripe Payment
# STRIPE_PUBLISHABLE_KEY = 'pk_test_51NzKZwLxGQ0N3mNafZOt2kqCvYGooxLxEWi6I2iyiaoHvL74kvU1PnbpjDhfIaD2lICn7Fd1xn29kQ17swyUPfWv00FfYWqNfj' # webhook secret
# STRIPE_SECRET_KEY = 'sk_test_51NzKZwLxGQ0N3mNagLW3BGcrBkEJUimfJH2Ufaf9465fBU50WYebW4hNXroCnfr7FGNB4PvplkBaiu3p2QE6H29Z00d50Lg48j'
# STRIPE_PUBLISHABLE_KEY = "pk_test_51NzKZwLxGQ0N3mNafZOt2kqCvYGooxLxEWi6I2iyiaoHvL74kvU1PnbpjDhfIaD2lICn7Fd1xn29kQ17swyUPfWv00FfYWqNfj"
# STRIPE_SECRET_KEY = "sk_test_51NzKZwLxGQ0N3mNagLW3BGcrBkEJUimfJH2Ufaf9465fBU50WYebW4hNXroCnfr7FGNB4PvplkBaiu3p2QE6H29Z00d50Lg48j"

# stripe listen --forward-to localhost:8000/payment/webhook/
# Code for getting payments info
CORS_ALLOW_ALL_ORIGINS = True
