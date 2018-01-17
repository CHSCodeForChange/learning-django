from django.conf.urls import url

from . import views
from teaching.models import Animal

urlpatterns = [
    url(r'^$', views.animal, name='animal'),
    url(r'^animal/', views.animal, name='animal'),
]
