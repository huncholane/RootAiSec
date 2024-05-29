import datetime
from threading import Thread
from live_logger import settings
from .models import Log


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # request.log = Log.objects.create(meta=request.META)
        # Thread(target=Log.objects.create, kwargs={'meta': request.META}).start()
        for ignore in settings.LIVE_LOGGER_IGNORED_PATHS:
            if ignore in request.path:
                return self.get_response(request)
        request.log = Log(meta=request.META)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        # request.log.duration = time.time() - start
        request.log.user = request.user if request.user.is_authenticated else None
        request.log.start_time = datetime.datetime.now(
            tz=datetime.timezone.utc)
        request.log.end_time = datetime.datetime.now(tz=datetime.timezone.utc)
        request.log.status_code = response.status_code
        Thread(target=request.log.save, daemon=True).start()

        return response
