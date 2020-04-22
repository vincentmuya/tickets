from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.ussd_callback, name ='ussd_callback'),
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
