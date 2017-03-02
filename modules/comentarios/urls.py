from django.conf.urls import url
from .views import ComentariosList

urlpatterns = [
	url(r'^$',ComentariosList.as_view())

]