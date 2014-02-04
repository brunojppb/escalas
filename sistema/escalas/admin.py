from django.contrib import admin
from sistema.escalas.models import Militar, Escala, Guarnicao

class MilitarAdmin(admin.ModelAdmin):
    list_display = ('posto', 'nome_de_guerra', 'matricula',)
    ordering = ('posto',)

class EscalaAdmin(admin.ModelAdmin):
    filter_horizontal = ('guarnicoes',)


class GuarnicaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'missao',)


admin.site.register(Militar, MilitarAdmin)
admin.site.register(Escala, EscalaAdmin)
admin.site.register(Guarnicao)