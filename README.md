# Next.js in Django with Channels and  ASGI
[Django + Next.js The Easy Way
](https://medium.com/@danialkeimasi/django-next-js-the-easy-way-655efb6d28e1)

## Introduction

After reading this article, you can create or enhance your projects using the many convenient features of Next.js and Django.

Using React instead of a Django template to create your frontend gives you access to many existing modern tools without the SEO issues of a SPA (Single Page Application) thanks to Next.js SSR capability.

You’ll also learn how to add Next.js to your existing Django project without any hassle, using [django-nextjs](https://github.com/QueraTeam/django-nextjs).

### How We Integrated Django + Next.js
There are several approaches to using these two frameworks together, but we are using one of them.

We are going to run Django and Next.js servers at the same time, use Django to accept web requests and use Next.js as an internal service that generates the HTML.
Accordingly, Django handles web requests, and for each request, Next.js is called inside the Django view to get the HTML response.

This is perfect if you already have a Django project, and you don’t want to change anything and just start using Next.js with it!
You can use this approach even if you are starting a new project because you’ll be able to use more Django features (e.g. sessions).

## Steps

### Nextjs
- Create Next.js project inside your Django project (or anywhere you want):
```
npx create-next-app
```

- Run the Next.js development server:
```
yarn dev
```

### Django
- Install the django-nextjs package, inside the same python environment, your Django project uses:
```
pip install django-nextjs
```
`channels is optional if using asgi.py, this is required for Next.js with HMR websocket connections. See asgi.py.

- Add django_nextjs to INSTALLED_APPS in Django settings:
```
INSTALLED_APPS = [
    # ...
    # channels,
    "django_nextjs",
]
```

- Include the django-nextjs URLs inside your root urls.py file:

- Write the next.js page view inside your app:

- Add the new view to urls.py:

- asgi.py:

```
# ...

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django_nextjs.proxy import NextJSProxyHttpConsumer, NextJSProxyWebsocketConsumer

from django.conf import settings
from django.urls import path

# http_routes = []
websocket_routers = []

if settings.DEBUG:
    # http_routes.insert(0, re_path(r"^(?:_next|__next|next).*", NextJSProxyHttpConsumer.as_asgi()))
    websocket_routers.insert(0, path("_next/webpack-hmr", NextJSProxyWebsocketConsumer.as_asgi()))


application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  ## Just HTTP for now. (We can add other protocols later.)
  "websocket": AuthMiddlewareStack(URLRouter(websocket_routers)),
})

```