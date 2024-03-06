from django.urls import path
from .views import hello, hi


urlpatterns =[
    path('hello/', hello),
    path('hi/', hi),
]