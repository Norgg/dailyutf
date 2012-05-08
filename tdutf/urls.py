from django.conf.urls.defaults import *
from main.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='home'),
    url(r'^old/(?P<pk>\d{1,10})/', Old.as_view(), name='old'),
    url(r'^feed$', CharFeed(), name='feed'),
)
