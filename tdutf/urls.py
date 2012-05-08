from django.conf.urls.defaults import *
from main.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='home'),
)
