from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    cui = models.CharField(max_length=13, unique=True)
    PROFESION_CHOICES = [
        ('matematico', 'Matemático'),
        ('fisico', 'Físico'),
    ]
    profesion = models.CharField(max_length=10, choices=PROFESION_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_usuario_set',  # Añade related_name aquí
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_usuario_set',  # Añade related_name aquí
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='usuario',
    )

class Archivo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to='archivos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
