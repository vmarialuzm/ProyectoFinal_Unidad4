from django.shortcuts import redirect,render
from .models import usuario,datos_portafolio
from .forms import LoginForm,DatosForm
from django.views.generic import FormView


class LoginCreate(FormView):
    model:usuario
    template_name="form.html"
    form_class=LoginForm

    def form_valid(self,form):
        usuario.objects.create(**form.cleaned_data)
        return redirect("datos")
    
#----------------------------------------------------
class DatosAlmacenar(FormView):
    model:datos_portafolio
    template_name="portafolio.html"
    form_class=DatosForm

    def form_valid(self,form):
        datos_portafolio.objects.create(**form.cleaned_data)

#----------------------------------------------------

def index(request):
    datos=usuario.objects.all()
    info=datos_portafolio.objects.all()
    contexto={'datos':datos,'info':info}
    return render(request,'index.html',contexto)     










