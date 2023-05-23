from django.shortcuts import render
from .models import Experiencia

# Create your views here.


def experiencia(request):
    experiencia = Experiencia.objects.all()
    return render(request, "experiencia/experiencia.html", {"experiencias": experiencia})