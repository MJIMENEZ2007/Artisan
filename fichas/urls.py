from django.urls import path

from .views import get_person_data ,\
    inscripcion , lista_inscritos, search_ubigeo,ubigeo_form

app_name = "fichas"

urlpatterns = [
    path("inscripcion", inscripcion , name = "inscripcion"),
    path("lista_inscritos", lista_inscritos , name= "lista_inscritos"),
    path('get_person_data/', get_person_data, name='get_person_data'),
    path('search-ubigeo/', search_ubigeo, name='search_ubigeo'),
    path('form/', ubigeo_form, name='ubigeo_form'),

]