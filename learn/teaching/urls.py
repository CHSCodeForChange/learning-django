from django.conf.urls import url

from . import views
from teaching.models import Animal

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^animal/', views.animal, name='animal'),
    url(r'^answer/', views.answer, name='answer')
]
