from django.conf.urls import patterns, url
from sistema.escalas.views import *

urlpatterns = patterns('',
    url(r'^$', home),
	url(r'^guarnicao/listar/$', guarnicao_listar),
    url(r'^guarnicao/criar/$', guarnicao_criar),
    url(r'^guarnicao/(?P<ident>\d+)/$', guarnicao_detalhes),
    url(r'^militar/(?P<mat>\d{7})/$', militar_detalhes),
    url(r'^militar/editar/(?P<ident>\d+)/$', militar_editar),
    url(r'^militar/criar/$', militar_criar),
    url(r'^militar/listar/$', militar_listar),
    url(r'^militar/consultar/$', consultar_militar_via_ajax),
    url(r'^escala/criar/$', escala_criar),
    url(r'^escala/consultar/$', consultar_guarnicao_via_ajax),

)
