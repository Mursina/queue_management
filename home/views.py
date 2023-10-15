from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def generate_token(request):
    return Response({'message': 'Token is created successfully'})
