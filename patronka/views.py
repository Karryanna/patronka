from django.shortcuts import render

from novinky.models import Novinky

def index(request):
  novinka = Novinky.objects.order_by("-datum_zverejneni")[:1]
  context = { 'novinky_list': novinka }
  return render(request, "index.html", context)

def static_view(request, page):
  templates = { "onas": "o_nas.html" }
  return render(request, templates[page])

