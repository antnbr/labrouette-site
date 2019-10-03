from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Evenement

# Create your views here.
def index(request):
    return redirect('home')

def home(request):
    last_ev = Evenement.objects.all().last()
    return render(request, 'ouf/home.html', {'last_ev': last_ev})

def a_propos(request):
    # Data related call
    return render(request, 'ouf/a_propos.html', {})

def evenements(request):
    evenements = Evenement.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'ouf/evenements.html', {'evenements': evenements})

def outils(request):
    # Data related call
    return render(request, 'ouf/outils.html', {})

def contact(request):
    # Data related call
    return render(request, 'ouf/contact.html', {})

def page_ev(request):
    ev = get_object_or_404(Evenement, titre=titre)
    return render(request, 'ouf/page_ev.html', {'ev': ev})
