from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contact(request):
    contact_form = ContactForm
    if request.method == 'POST':
        contact_form = contact_form(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            print(name, email, content)
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["baristamanu@gmail.com"],
                reply_to=[email]
            )
            try:
              email.send()
              # Todo va bien, redireccionamos a OK
              return redirect(reverse('contact') + "?ok")
            except:
              # Todo va mal, redireccionamos a FAIL
              return redirect(reverse('contact') + "?fail")
    return render(request, "contact/contact.html", {"form": contact_form})