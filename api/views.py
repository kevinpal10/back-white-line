from rest_framework import viewsets
from .serializer import PersonaSerializer
from .models import Persona
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
class  PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
@csrf_exempt
def recibir_formulario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({'message': 'Datos recibidos correctamente'}, status = 200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalido'}, status =400)
    return JsonResponse({'error': 'Método no permitida'}, status =405)