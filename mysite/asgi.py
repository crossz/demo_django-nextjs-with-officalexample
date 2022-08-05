"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
asgi_application = get_asgi_application()



from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django_nextjs.proxy import NextJSProxyHttpConsumer, NextJSProxyWebsocketConsumer

from django.conf import settings
from django.urls import path, re_path

# http_routes = []
http_routes = [re_path(r"", asgi_application)]
websocket_routers = []

if settings.DEBUG:
    http_routes.insert(0, re_path(r"^(?:_next|__next|next).*", NextJSProxyHttpConsumer.as_asgi()))
    websocket_routers.insert(0, path("_next/webpack-hmr", NextJSProxyWebsocketConsumer.as_asgi()))

application = ProtocolTypeRouter({
  # "http": AsgiHandler(),
  "http": URLRouter(http_routes),
  ## Just HTTP for now. (We can add other protocols later.)
  "websocket": AuthMiddlewareStack(URLRouter(websocket_routers)),
})
