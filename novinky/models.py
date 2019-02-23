from django.db import models
from django.conf import settings

class Novinky(models.Model):
  titulek = models.CharField(max_length=150)
  datum_zverejneni = models.DateTimeField('Datum zveřejnění')
  autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  text = models.TextField()

  def __str__(self):
    return self.titulek
