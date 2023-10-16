from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
import json

from .models import Token, Counter, Service

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})

@api_view(['POST'])
def generate_token(request):
    return render(request, 'home/index.html', {'response': {'token': 123, 'message': 'Token is created successfully'}})

@api_view(['PUT'])
def update_counter_status(request):
    return Response({'message': 'Counter status updated successfully'})

@api_view(['GET'])
def check_token_assignment(request):
    counter = request.GET.get('counter_id')
    counter_ins = Counter.objects.get(pk=counter)
    token = Token.objects.filter(counter_id=counter_ins)
    
    return Response({
        "token": token.values().first(),
        "status": "open"
    })

@api_view(['PUT'])
def choose_service_mode(request):
    return Response({'message': 'Service mode updated successfully'})

@api_view(['PUT'])
def update_system_configuration(request):
    return Response({'message': 'System configurations updated successfully'})