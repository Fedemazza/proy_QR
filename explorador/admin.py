from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Qr) 
admin.site.register(Carga)
#admin.site.register(Usuario) 