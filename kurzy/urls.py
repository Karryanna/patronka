from django.urls import path

from . import views

app_name = 'kurzy'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),
  path('<int:pk>/', views.detail, name='detail'),
]
