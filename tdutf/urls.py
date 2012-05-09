from django.conf.urls.defaults import *
from main.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='home'),
    url(r'^vote/(?P<pk>\d{1,10})/', vote, name='vote'),
    url(r'^old/(?P<pk>\d{1,10})/', Old.as_view(), name='old'),
    url(r'^feed$', CharFeed(), name='feed'),
    url(r'^json$', json, name='json'),
    url(r'^random$', Random.as_view(), name='random'),
)
