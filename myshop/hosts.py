from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'www', 'myshop.urls', name='www'),
    # host(r'[a-z]+', settings.ROOT_URLCONF, name='admin'),
    host(r'elpizo', 'myshop.urls', name='elpizo'),
    host(r'[a-z]+', 'myshop.subdomain_urls', name='subdomain'),
)
