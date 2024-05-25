from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import pyshorteners

from . import service

# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)


def shorten_post(request):
    return shorten(request, request.POST['url'])


def shorten(request, url):
    shortener = pyshorteners.Shortener()
    shortened_url = shortener.isgd.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')