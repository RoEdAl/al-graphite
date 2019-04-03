#
# graphite-web : local_settings.py
#
# For more elaborate configuration file see
# /usr/share/graphite-web/conf/local_settings.py.example.
#

URL_PREFIX = '/graphite'

SECRET_KEY = 'Changed but still unsafe'
ALLOWED_HOSTS = [ '*' ]
TIME_ZONE = 'Europe/Warsaw'

LOG_RENDERING_PERFORMANCE = False
LOG_CACHE_PERFORMANCE = False

LOG_FILE_INFO = '+'
LOG_FILE_EXCEPTION = '+'
LOG_FILE_CACHE = '+'
LOG_FILE_RENDERING = '+'

# DEBUG = True

GRAPHITE_ROOT = '/var/lib/graphite-web'
CONF_DIR = '/etc/graphite-web/'
STORAGE_DIR = '/var/lib/graphite-web'
STATICFILES_DIRS = ('/usr/share/graphite-web/webapp/content',)
LOG_DIR = '/var/log/graphite-web/'

WHISPER_DIR = '/var/lib/carbon/whisper'
STANDARD_DIRS = [WHISPER_DIR]

AUTO_REFRESH_INTERVAL = 120

# CARBONLINK_HOSTS = ["[::1]:7002:ip6"]
