'''
Urls for shortener app urlshortener/urls.py
'''

from django.urls import path

# Import the home view
from .views import home_view

appname = "shortener"

urlpatterns = [
    # Home view
    path("", home_view, name="home")
]
