# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpResponse
from django_nextjs.render import render_nextjs_page_async

async def jobs(request):
    return await render_nextjs_page_async(request)