from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('a_propos', views.a_propos, name='a_propos'),
    path('evenements', views.evenements, name='evenements'),
    path('outils', views.outils, name='outils'),
    path('contact', views.contact, name='contact'),
    path('evenements/<int:pk>', views.page_ev, name='page_ev')
]
