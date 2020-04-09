from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns=[
    url(r'^$',views.callback, name ='callback'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^edit/profile/(\d+)$', views.update_profile, name='update-profile'),
    url('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    url('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    #register, confirmation, validation and callback url
    url('c2b/register', views.register_urls, name="register_mpesa_validation"),
    url('c2b/confirmation', views.confirmation, name="confirmation"),
    url('c2b/validation', views.validation, name="validation"),
    url('c2b/callback', views.call_back, name="call_back"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
