# other settings ...

INSTALLED_APPS = [
    # default apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # your apps
    'accounts',   # make sure this is included
    # etc
]

AUTH_USER_MODEL = 'accounts.CustomUser'

# Media settings for profile_photo if using local file storage
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'   # or as appropriate

# Security settings (some will overlap with task 2 & 3)
DEBUG = False   # in production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # one year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# If you use CSP:
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # you may insert CSP middleware if you use a third‑party or custom
    # e.g. 'csp.middleware.CSPMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # other middleware…
]

# e.g., minimal CSP if you use django-csp
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_IMG_SRC = ("'self'", 'data:',)
# etc
