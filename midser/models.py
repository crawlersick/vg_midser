from django.db import models

# Create your models here.
class vgitem(models.Model):
    country = models.CharField(max_length=20)
    ipadd = models.CharField(max_length=20)
    ovpnfile = models.CharField(max_length=5000)
    pub_date = models.DateTimeField('date published')

