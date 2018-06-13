from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


from .forms import RegModelForm, ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
    titulo = "HOLA"
    if request.user.is_authenticated:
    	titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    
    context = {
    			"titulo": titulo,
        		"el_form": form,
    }

    if form.is_valid():
    	instance = form.save(commit=False)
    	nombre = form.cleaned_data.get("nombre")
    	email = form.cleaned_data.get("email")
    	if not instance.nombre:
    		instance.nombre = "PERSONA"
    	instance.save()

    	context = {
    		"titulo": "Gracias %s!" %(nombre) 
    	}

    	if not nombre:
    		context = {
    		"titulo": "Gracias persona sin nombre"
    		}
    	print (instance)
    	print (instance.timestamp)
    	# form_data = form.cleaned_data
    	# abc = form_data.get("email")
    	# abc2 = form.data.get("nombre")
    	# obj = Registrado.objects.create(email=abc, nombre=abc2)
    
    
    return render(request, "base.html", context)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print (key)
        #     print (form.cleaned_data.get(key))

        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        asunto = 'Mensaje Maricafé'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from, "otroemail@gmail.com"]
        email_mensaje = "%s: %s enviado por %s" %(form_nombre, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=False
            )


        # print (email, mensaje, nombre)
    context = {
                 "titulo": "COMUNICATE CON NOSOTROS",
                 "form": form,
                 "titulo2": "NUESTRA UBICACIÓN",
    }

    return render(request, "forms.html", context)

# def about(request):
#     return render(request, "about.html")

# def products(request):
#     return render(request, "productos.html")