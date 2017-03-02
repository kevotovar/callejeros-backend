from django.conf.urls import url
from .views import SolicitudesList

urlpatterns = [
	url(r'^$',SolicitudesList.as_view())
	
]