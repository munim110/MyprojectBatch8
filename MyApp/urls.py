from django.urls import path
from .views import hello, hi, single_contact


urlpatterns = [
    path('', hello),
    path('<int:id>/', single_contact, name='single_contact'),
    path('hi/', hi),
]