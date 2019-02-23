from django.shortcuts import render
from django.views import generic

from .models import Novinky

class IndexView(generic.ListView):
  template_name = 'novinky/index.html'

  def get_queryset(self):
      return Novinky.objects.order_by('-datum_zverejneni')[:5]
