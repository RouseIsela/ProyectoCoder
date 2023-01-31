from django.http import HttpResponse
from AppCoder.models import Curso

def curso(self):
    curso= Curso(nombre="Desarrollo Web",camada="12345")
    curso.save()
    documento_de_Texto= f"-->Curso:{curso.nombre} camada {curso.camada}"
    return HttpResponse(documento_de_Texto)

