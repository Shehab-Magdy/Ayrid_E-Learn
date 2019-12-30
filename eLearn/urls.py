from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .views import registration, home

app_name = 'eLearn'

urlpatterns = [
    path('', home.index, name='elearn.home'),
    path('/register', registration.newRegistration, name='elearn.newRegistration'),
    path('/login', registration.login, name='elearn.login'),
]
