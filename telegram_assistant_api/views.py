from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt
@api_view(['GET'])
def news(request):
    result = {
        'result': 'OK'
    }

    return Response(result)