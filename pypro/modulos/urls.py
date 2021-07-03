from django.urls import path

from pypro.modulos import views

app_name = 'moduloos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='detalhe'),
]