"""APITX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from app.vistas import vistaDuenio, vistaRuta, vistaHorario, vistaDenuncia, vistaTipodenuncia, vistaActividad

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^duenio/$', vistaDuenio.lista_objetos),
    url(r'^duenio/(?P<pk>[0-9]+)$', vistaDuenio.detalle_objetos),
    url(r'^ruta/$', vistaRuta.lista_objetos),
    url(r'^ruta/(?P<pk>[0-9]+)$', vistaRuta.detalle_objetos),
    url(r'^horario/$', vistaHorario.lista_objetos),
    url(r'^horario/(?P<pk>[0-9]+)$', vistaHorario.detalle_objetos),
    url(r'^denuncia/$', vistaDenuncia.lista_objetos),
    url(r'^denuncia/(?P<pk>[0-9]+)$', vistaDenuncia.detalle_objetos),
    url(r'^tipodenuncia/$', vistaTipodenuncia.lista_objetos),
    #url(r'^tipodenuncia/(?P<pk>[0-9]+)$', vistaTipodenuncia.detalle_objetos),
    #url(r'^tipodiahorariodetalle/$', vistadiahorariodetalle.lista_objetos),
    #url(r'^tipodiahorariodetalle/(?P<pk>[0-9]+)$', vistadiahorariodetalle.detalle_objetos),
    #url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^cultura/$', vistaActividad.lista_objetos),
    url(r'^cultura/(?P<pk>[0-9]+)$', vistaActividad.detalle_objetos),

]
