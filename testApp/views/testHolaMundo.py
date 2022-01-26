from django.http.response import JsonResponse
from rest_framework import generics, views, status

from django.core import serializers
import json

class testHolaMundo(views.APIView):

  def get(self, request, *args, **kwargs):
    data = {"mensaje": "Qué onda gente, me gustan los gatos"}

    return JsonResponse(data)
    #return Response(status=status.HTTP_200_OK)