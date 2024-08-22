from django.urls import path
from .views import inscripcion, lista_inscritos, ubigeo_form, editar_proceso, eliminar_proceso

app_name = "inv"

urlpatterns = [
    path("inscripcion", inscripcion , name = "inscripcion"),
    path("lista_inscritos", lista_inscritos , name= "lista_inscritos"),
    path("editar_proceso/<int:proceso_id>/", editar_proceso, name="editar_proceso"),
    path("eliminar_proceso/<int:proceso_id>/", eliminar_proceso, name="eliminar_proceso"),
    path('form/', ubigeo_form, name='ubigeo_form'),
]
