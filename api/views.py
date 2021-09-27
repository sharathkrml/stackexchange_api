from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
# Create your views here.
@api_view(['GET'])
def search(request):
    if(request.method == 'GET'):
        r=requests.get('https://api.stackexchange.com/2.3/search/advanced?',params=request.GET)
        return Response(r.json())