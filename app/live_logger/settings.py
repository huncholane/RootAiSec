from django.conf import settings
import os


LIVE_LOGGER_STORAGE_LENGTH = getattr(settings, 'LIVE_LOGGER_STORAGE_LENGTH', os.getenv('LIVE_LOGGER_STORAGE_LENGTH', 1000))
LIVE_LOGGER_PAGINATION = getattr(settings, 'LIVE_LOGGER_PAGINATION', os.getenv('LIVE_LOGGER_PAGINATION', 100))
LIVE_LOGGER_DOWNLOAD_IPINFO = getattr(settings, 'LIVE_LOGGER_DOWNLOAD_IPINFO', os.getenv('LIVE_LOGGER_DOWNLOAD_IPINFO', True))
LIVE_LOGGER_SHOW_MAP = getattr(settings, 'LIVE_LOGGER_SHOW_MAP', os.getenv('LIVE_LOGGER_SHOW_MAP', True))
LIVE_LOGGER_IGNORED_PATHS = getattr(settings, 'LIVE_LOGGER_IGNORED_PATHS', os.getenv('LIVE_LOGGER_IGNORED_PATHS', ['static', 'favicon.ico', 'logs']))