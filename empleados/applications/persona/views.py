from django.shortcuts import render
from django.views.generic import(
    ListView,
    DetailView,
    CreateView
)
from .models import Empleado
# Create your views here.
#listar todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 10
    model = Empleado

#listar todos los empleados que pertenecen a un area de la empresa
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['name']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
    )
        return lista

#listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista

class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'


    def get_queryset(self):
        empleado = Empleado.objects.get(id=1)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

class EmpleadoCreateView(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    fields = ('__all__')
    success_url = '.'