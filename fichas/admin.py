from django.contrib import admin
from .models import DniProcesos ,  Procesos
# Register your models here.

class DniProcesosAdmin(admin.ModelAdmin):
    list_display = ('id' , 'idoperario' , 'idseccion' , 'nombre' )
    list_editable = ('nombre',)
    list_filter = ('idseccion' , 'idoperario')
admin.site.register(DniProcesos , DniProcesosAdmin)

class ProcesosAdmin(admin.ModelAdmin):
    list_display = ('id','idoperario','idseccion', 'fechahora','tipo')
    list_editable = ('tipo',)
    list_filter = ('idseccion' , 'idoperario')
admin.site.register(Procesos , ProcesosAdmin)