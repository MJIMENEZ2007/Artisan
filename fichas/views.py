from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import ProcesosForm
from .apis_net_pe import ApisNetPe
from .models import Procesos
# from .models import Ubigeo
def editar_proceso(request, proceso_id):
    proceso = get_object_or_404(Procesos, id=proceso_id)
    if request.method == 'POST':
        form = ProcesosForm(request.POST, instance=proceso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proceso actualizado correctamente.')
            return redirect('inv:lista_inscritos')
    else:
        form = ProcesosForm(instance=proceso)
    
    return render(request, 'inv/inscripcion.html', {'form': form})

def eliminar_proceso(request, proceso_id):
    proceso = get_object_or_404(Procesos, id=proceso_id)
    if request.method == 'POST':
        proceso.delete()
        messages.success(request, 'Proceso eliminado correctamente.')
        return redirect('inv:lista_inscritos')
    
    return render(request, 'inv/eliminar_confirmacion.html', {'proceso': proceso})

def ubigeo_form(request):
    return render(request, 'inv/form.html')
# def search_ubigeo(request):
#     if 'term' in request.GET:
#         qs = Ubigeo.objects.filter(ubigeo__icontains=request.GET.get('term'))
#         ubigeos = list(qs.values('codubigeo', 'ubigeo', 'coddep', 'departamento', 'codprov', 'provincia'))
#         return JsonResponse(ubigeos, safe=False)
#     return JsonResponse([], safe=False)


def inscripcion(request):
    if request.method == 'POST':
        form = ProcesosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proceso ingresado correctamente.')
            return redirect('inv:lista_inscritos')
    else:
        form = ProcesosForm()
    
    return render(request, 'inv/inscripcion.html', {'form': form})

# def inscripcion(request):
#     if request.method == 'POST':
#         form = ProcesosForm(request.POST)
#         if form.is_valid():
#             ficha = form.save()
#             messages.success(request, f'Inscripción exitosa para {ficha.modelo} {ficha.categoria}')
#             return redirect('inv:lista_inscritos')
#         else:
#             messages.error(request, 'Por favor, corrige los errores en el formulario.')
#     else:
#         form = ProcesosForm()
#     return render(request, 'inv/inscripcion.html', {'form': form})

# def get_person_data(request):
#     dni = request.GET.get('dni', None)
#     if dni:
#         print(f"Buscando DNI: {dni}")  # Agrega este print para ver si el DNI se está recibiendo correctamente
#         try:
#             ficha = ProcesosForm.objects.get(dni=dni)
#             data = {
#                 'fecha_hora': ficha.fecha_hora,
#                 'tipo' : ficha.tipo,
#                 'modelo' : ficha.modelo,
#                 'categoria' : ficha.categoria,
#                 'tarifa' : ficha.tarifa,
#             }
#             return JsonResponse(data)
#         except ProcesosForm.DoesNotExist:
#             print("DNI no encontrado.")  # Agrega este print para depurar
#             return JsonResponse({'error': 'No se encontró ninguna persona con ese DNI.'}, status=404)
#     print("DNI no proporcionado.")  # Agrega este print para depurar
#     return JsonResponse({'error': 'DNI no proporcionado.'}, status=400)


def lista_inscritos(request):
    inscritos = Procesos.objects.all().order_by('-fecha_hora')  # Asegúrate de que el nombre del campo es 'fechahora'
    return render(request, 'inv/lista_inscritos.html', {'inscritos': inscritos})

class BaseView(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    
    def handle_no_permission(self):
        messages.error(self.request , "No tienes permiso para acceder a esta página.")
        return redirect('config:home')