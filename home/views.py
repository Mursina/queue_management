from rest_framework.response import Response

def generate_token(request):
    return Response({'message': 'Token is created successfully'})
