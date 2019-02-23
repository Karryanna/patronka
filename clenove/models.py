from django.db import models

class Clenove(models.Model):
  vztahy = (
             ('Předseda', 'Předseda'),
             ('Zakládající člen', 'Zakládající člen'),
             ('Běžný člen', 'Běžný člen'),
           )

  nick = models.CharField('Přezdívka', max_length=40)
  display_name = models.CharField('Zobrazované jméno', max_length=100)
  full_name = models.CharField('Úplné jméno', max_length=130)
  patronci_vztah = models.CharField('Vztah k Patronce', max_length=50, choices=vztahy)
  motto = models.CharField('Motto', max_length=200, blank=True)
  patronci_zajmy = models.TextField('Patrončí zájmy', blank=True)
  pracovni_zkusenosti = models.TextField('Pracovní zkušenosti', blank=True)
  foto = models.ImageField(upload_to="clenove_foto/", null=True, blank=True)

  def __str__(self):
    return self.display_name
