# seed_data.py

import os
import django

# Configura Django para acceder a los modelos
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyecto.settings")
django.setup()

from cursos.models import Curso

# Borra datos previos (opcional)
Curso.objects.all().delete()

# Crea datos de ejemplo
cursos_iniciales = [
    {
        "nombre": "Curso de Django Básico",
        "descripcion": "Aprende los fundamentos de Django.",
        "fecha_inicio": "2024-01-01",
        "duracion_semanas": 8,
        "plazas_disponibles": 30,
        "precio": 150.00,
    },
    {
        "nombre": "Curso de JavaScript Avanzado",
        "descripcion": "JavaScript avanzado para desarrollo frontend.",
        "fecha_inicio": "2024-02-01",
        "duracion_semanas": 10,
        "plazas_disponibles": 20,
        "precio": 200.00,
    },
    {
        "nombre": "Curso de Python Intermedio",
        "descripcion": "Profundiza en Python con ejemplos prácticos.",
        "fecha_inicio": "2024-03-01",
        "duracion_semanas": 12,
        "plazas_disponibles": 25,
        "precio": 180.00,
    },
]

# Inserta los datos en la base de datos
for curso_data in cursos_iniciales:
    Curso.objects.create(**curso_data)

print("Datos iniciales cargados en la base de datos.")
