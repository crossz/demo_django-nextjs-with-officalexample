"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# application = get_asgi_application()


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  ## Just HTTP for now. (We can add other protocols later.)
})




# http_routes = [path("", django_asgi_app)]

# application = ProtocolTypeRouter(
#     {
#         # Django's ASGI application to handle traditional HTTP and websocket requests.
#         "http": URLRouter(http_routes),
#         "websocket": AuthMiddlewareStack(URLRouter(websocket_routers)),
#         # ...
#     }
# )