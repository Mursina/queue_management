from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

@api_view(['POST'])
def generate_token(request):
    return render(request, 'home/index.html', {'response': {'token': 123, 'message': 'Token is created successfully'}})

@api_view(['PUT'])
def update_counter_status(request):
    return Response({'message': 'Counter status updated successfully'})

@api_view(['GET'])
def check_token_assignment(request):
    return Response({
        "token": "A123",
        "status": "open"
    })

@api_view(['PUT'])
def choose_service_mode(request):
    return Response({'message': 'Service mode updated successfully'})

@api_view(['PUT'])
def update_system_configuration(request):
    return Response({'message': 'System configurations updated successfully'})