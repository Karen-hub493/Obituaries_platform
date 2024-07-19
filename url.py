# urls.py in the `obituaries` app
urlpatterns = [
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
    path('view_obituaries/', views.view_obituaries, name='view_obituaries'),
]
