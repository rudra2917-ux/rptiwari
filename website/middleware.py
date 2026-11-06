from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class ForceHttpsMiddleware:
    """Redirect visitors who reached the site over plain HTTP to HTTPS.

    Railway's edge terminates HTTPS and forwards requests to the app with an
    X-Forwarded-Proto header saying how the visitor connected. Only requests
    that came through the edge over HTTP are redirected; Railway's internal
    health check (no forwarded header) and local development are left alone,
    which is why Django's own SECURE_SSL_REDIRECT is not used.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        proto = request.META.get('HTTP_X_FORWARDED_PROTO', '').split(',')[0].strip().lower()
        if not settings.DEBUG and proto == 'http':
            return HttpResponsePermanentRedirect(f'https://{request.get_host()}{request.get_full_path()}')
        return self.get_response(request)
