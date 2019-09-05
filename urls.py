
from django.urls import path
from . import views

urlpatterns = [
    path('get', views.get, name='get'),

    path('post', views.post, name='post'),

    path('submit', views.submit, name='submit'),
]
