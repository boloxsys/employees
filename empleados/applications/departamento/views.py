from django.shortcuts import render
#esta vista solo se usa para formularios que usen varios modelos 
from django.views.generic.edit import FormView
#from empleados.applications import departamento
# Importamos formulario creado
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from applications.departamento.models import Departamento

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa

        )
        return super(NewDepartamentoView, self).form_valid(form)
