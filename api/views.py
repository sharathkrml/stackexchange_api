from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache
import requests
# Create your views here.
@api_view(['GET'])
def search(request):
    if(request.method == 'GET'):
        result = cache.get(str(request.GET))
        if not result:
            r=requests.get('https://api.stackexchange.com/2.3/search/advanced?',params=request.GET)
            result=r.json()
            cache.set(str(request.GET),r.json())
        return Response(result)