from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from welcome.views import index, health
from testApp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index),
    url(r'^health$', health),
    path('test/', views.testHolaMundo.as_view()),
    
]


if settings.DEBUG:
  import debug_toolbar
  urlpatterns = [
      url(r'^__debug__/', include(debug_toolbar.urls)),
  ] + urlpatterns
