# urls.py in the `obituaries` app
from django.urls import path
from . import views

urlpatterns = [
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
]
