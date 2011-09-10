from django.db import models
import datetime; now=datetime.date.today()
from django.contrib import admin 
from django.contrib.auth.models import User, UserManager
# Create your models here.
#class LoginForm(forms.Form):
#	username = forms.CharField(max_length=100)
#	password = forms.CharField(widget=forms.PasswordInput(rendervalue=False),max_length=100)



class Usuario(User):
    direccion = models.CharField(max_length=200)
    celular   = models.CharField(max_length=12)
    objects = UserManager()
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
#admin.site.register(Usuario) 
    
class TipoIncidencia(models.Model):
    nombre  = models.CharField(max_length=60)
    detalle = models.CharField(max_length=260)
    def __unicode__(self):
        return self.nombre
        
class DetalleIncidencia(models.Model):
    descripcion = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    longitud = models.IntegerField()
    latitud = models.IntegerField()
    fecha = models.DateField(default=now)
    hora = models.CharField(max_length=12)
    usuario = models.ForeignKey(Usuario)
    tipo = models.ForeignKey(TipoIncidencia)
    def __unicode__(self):
        return self.descripcion
    
