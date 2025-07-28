# landing_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import firebase_admin
from firebase_admin import credentials, db
import datetime


class LandingAPI(APIView):
    name = "Landing API"
    collection_name = 'votes'  # Cambia esto por el nombre de tu colección de Firebase

    def get(self, request):
        """Obtiene los datos de la colección de Firebase."""
        ref = db.reference(self.collection_name)
        data = ref.get()  # Obtiene todos los registros de la colección
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crea un nuevo registro en la colección de Firebase."""
        ref = db.reference(self.collection_name)
        data = request.data
        # Agregar una marca de tiempo (opcional)
        data['created_at'] = datetime.datetime.now().isoformat()
        ref.push(data)  # Añadir el nuevo registro a la colección
        return Response(data, status=status.HTTP_201_CREATED)
