from django.contrib import admin

from django.urls import *
from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('login.urls')),
    url(r'^$',include('login.urls'),name='home')


]
