from django.db import models
from . import settings
import requests

# Create your models here.
class Location(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    city = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    loc = models.CharField(max_length=60, null=True)
    org = models.CharField(max_length=100, null=True)
    postal = models.CharField(max_length=20, null=True)
    timezone = models.CharField(max_length=50, null=True)
    bogon = models.BooleanField(default=False)
    success = models.BooleanField(default=False)

    def download(self):
        try:
            data = requests.get(f'http://ipinfo.io/{self.ip}/json').json()
        except:
            return
        self.success = True
        self.city = data.get('city')
        self.region = data.get('region')
        self.country = data.get('country')
        self.loc = data.get('loc')
        self.org = data.get('org')
        self.postal = data.get('postal')
        self.timezone = data.get('timezone')
        self.bogon = data.get('bogon')
        return data

    def save(self, *args, **kwargs):
        if settings.LIVE_LOGGER_DOWNLOAD_IPINFO and not self.success:
            self.download()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.ip


class Log(models.Model):
    meta = models.JSONField()
    messages = models.JSONField(default=list)
    json = models.JSONField(default=dict)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    status_code = models.IntegerField(null=True)

    def save(self, *args, **kwargs):
        kwargs.pop('loc', None)
        kwargs.pop('is_new', None)
        meta = kwargs.pop('meta', self.meta).copy()
        (loc, is_new) = Location.objects.update_or_create(ip=meta['REMOTE_ADDR'], defaults={
            'ip': meta['REMOTE_ADDR']
        })
        for key, val in meta.items():
            meta[key] = str(val)
        self.location = loc
        self.is_new = is_new
        self.meta = meta
        overflow = Log.objects.count() - settings.LIVE_LOGGER_STORAGE_LENGTH
        if overflow > 0:
            ids_to_delete = Log.objects.all().order_by('id')[:overflow].values_list('id', flat=True)
            Log.objects.filter(id__in=list(ids_to_delete)).delete()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.meta['PATH_INFO']

    def __call__(self, message):
        self.messages += [message]
        return self