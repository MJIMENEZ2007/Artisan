from django.contrib import admin
from .models import DniProcesos ,  Procesos
# Register your models here.

class DniProcesosAdmin(admin.ModelAdmin):
    list_display = ('id' , 'id_operario' , 'id_seccion' , 'nombre' )
    list_editable = ('nombre',)
    list_filter = ('id_seccion' , 'id_operario')
admin.site.register(DniProcesos , DniProcesosAdmin)

class ProcesosAdmin(admin.ModelAdmin):
    list_display = ('id','id_operario','id_seccion', 'fecha_hora','tipo', 'modelo')
    list_editable = ('tipo',)
    list_filter = ('id_seccion' , 'id_operario')
admin.site.register(Procesos , ProcesosAdmin)