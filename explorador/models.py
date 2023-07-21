from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Qr(models.Model):

    CATEGORY = (
        ('Opc_1','Opc_1'),
        ('Opc_2','Opc_2'),
    )

    serialnum = models.CharField(primary_key=True, max_length=200) # #models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    Creador =  models.CharField(max_length=200, null=True, blank = True)
    url =  models.URLField(max_length=200, null=True, blank = True)
    campo3 =  models.CharField(max_length=200, null=True, blank = True)
    campo4 =  models.CharField(max_length=200, null=True, blank = True)
    campo5 =  models.CharField(max_length=200, null=True)
    campo6 =  models.CharField(max_length=200, null=True)
    campo7 =  models.CharField(max_length=200, null=True)
    campo8_cat =  models.CharField(max_length=200, null=True,choices=CATEGORY)

    def __str__(self):
        return self.serialnum

class Carga(models.Model):

    qr = models.ForeignKey(Qr, null=True, on_delete= models.CASCADE) #https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    date_created = models.DateTimeField(auto_now_add=True)
    author =  models.ForeignKey(User, null=True ,on_delete=models.PROTECT) #https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models

    def __str__(self):
        return str(self.date_created)


