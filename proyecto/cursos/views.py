# views.py
from django.shortcuts import render
from .models import Curso

def home(request):
    # Obtener todos los cursos de la base de datos
    cursos = Curso.objects.all()  # Esto obtiene todos los cursos

    # Pasar los cursos al contexto de la plantilla
    context = {
        'cursos': cursos,
    }
    
    return render(request, 'cursos/home.html', context)
