from django.shortcuts import render

from .models import Clenove

def seznam(request):
  clenove = Clenove.objects.all()
  for clen in clenove:
    if clen.patronci_zajmy:
      clen.patronci_zajmy = clen.patronci_zajmy.split("\r\n")
    if clen.pracovni_zkusenosti:
      clen.pracovni_zkusenosti = clen.pracovni_zkusenosti.split("\r\n")
  context = { 'clenove_list': clenove }
  return render(request, "clenove/seznam.html", context)
