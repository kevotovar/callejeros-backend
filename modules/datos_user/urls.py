from django.conf.urls import url, include
from .views import UserList

urlpatterns = [
	url(r'^$',UserList.as_view())
]