from django.conf.urls import url
from .views import MascotasList, RazasList, EspeciesList

urlpatterns = [
	url(r'^$',MascotasList.as_view()),
	url(r'^razas/$',RazasList.as_view()),
	url(r'especies/$',EspeciesList.as_view())
]