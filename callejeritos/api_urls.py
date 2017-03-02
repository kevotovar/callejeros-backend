from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Callejeritos API')

urlpatterns=[
	url(r'^mascotas/',include('modules.mascotas.urls')),
	url(r'^comentarios/',include('modules.comentarios.urls')),
	url(r'^solicitudes_adopcion/',include('modules.solicitudes_adopcion.urls')),
	url(r'^auth/', obtain_jwt_token),
	url(r'^users/',include('modules.datos_user.urls')),


	#Documentation
	url(r'^documentation/',schema_view)

]