from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.encoding import force_str
from django.core.mail import send_mail
from .forms import RegistroForm, AccesoForm
from .models import Usuario, Archivo

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(f'/{user.username}')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def acceso(request):
    if request.method == 'POST':
        form = AccesoForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Send login email
           # send_mail(
            #    force_str('Login Notification'),
             #   force_str(f'Fecha y hora: {timezone.now()}\nIP: {get_client_ip(request)}'),
              #  'from@example.com',
               # [user.email],
                #fail_silently=False,
            #)
            return redirect(f'/{user.username}')
    else:
        form = AccesoForm()
    return render(request, 'usuarios/acceso.html', {'form': form})

@login_required
def perfil(request, username):
    user = Usuario.objects.get(username=username)
    archivos = Archivo.objects.filter(usuario=user)
    return render(request, 'usuarios/perfil.html', {'user': user, 'archivos': archivos})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from django import forms

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['archivo']

    def clean_archivo(self):
        archivo = self.cleaned_data['archivo']
        if not archivo.name.endswith('.p2'):
            raise forms.ValidationError("El archivo debe tener la extensión .p2")
        return archivo

@login_required
def subir_archivos(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.save(commit=False)
            archivo.usuario = request.user
            archivo.save()
            return redirect(f'/{request.user.username}')
    else:
        form = ArchivoForm()
    return render(request, 'usuarios/subir_archivos.html', {'form': form})
