from django.db import models

class Kurzy(models.Model):
  nazev = models.CharField('Název', max_length=200)
  akreditace_mpsv = models.BooleanField('Akreditace MPSV')
  hodin = models.PositiveSmallIntegerField('Počet hodin')
  misto = models.CharField('Místo konání', max_length=100)
  cena = models.TextField(null=True)
  termin = models.CharField('Termín konání', max_length=200)
  lektor = models.CharField(max_length=80)
  min_ucastniku = models.PositiveSmallIntegerField('Minimální počet účastníků')
  max_ucastniku = models.PositiveSmallIntegerField('Maximální počet účastníků')
  specifika = models.TextField(null=True, blank=True)
  vhodny_pro = models.TextField(null=True)
  opakovani = models.BooleanField('Opakování')
  anotace = models.TextField(null=True)

  def __str__(self):
    return self.nazev
