from django.shortcuts import render
from django.views import generic
from django.http import Http404

from .models import Kurzy

class IndexView(generic.ListView):
  template_name = 'kurzy/seznam.html'

  def get_queryset(self):
    return Kurzy.objects.order_by('-akreditace_mpsv', 'nazev')

class DetailView(generic.DetailView):
  model = Kurzy
  context_object_name = 'kurz'
  template_name = 'kurzy/detail.html'

def detail(request, pk):
  try:
    kurz = Kurzy.objects.get(pk=pk)
  except Kurzy.DoesNotExist:
    raise Http404("Kurz neexistuje")

  context = { 'kurz': kurz }
  kurz.cena = kurz.cena.replace(",,", "<br>")
  kurz.vhodny_pro = kurz.vhodny_pro.split("\r\n")
  if kurz.hodin == 0:
    kurz.hodin = "Dle potřeby"

  return render(request, 'kurzy/detail.html', context)
