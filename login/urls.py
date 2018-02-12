from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import *
from . import views
app_name='reg'

urlpatterns = [
    url(r'^$',views.index.as_view(), name='index'),
    url(r'^register', views.UserFormView.as_view(), name='register'),
    url(r'^login$', views.login.as_view(), name='login'),
    url(r'^verify$', views.verify, name='verify'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
