from django.conf.urls import url
from .views import *
from . import views
app_name='register'

urlpatterns = [
    url(r'^$',views.index.as_view(), name='index'),
    url(r'^register', views.UserFormView.as_view(), name='register'),
    url(r'^login$', views.login.as_view(), name='login'),
    url(r'^verify$', views.verify, name='verify')
]

