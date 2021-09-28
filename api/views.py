from rest_framework.decorators import api_view
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from django.core.cache import cache
import requests
from rest_framework.decorators import api_view, throttle_classes
class AnonMinThrottle(AnonRateThrottle):
    scope='anon_min'

class AnonDayThrottle(AnonRateThrottle):
    scope='anon_day'
@api_view(['GET'])
@throttle_classes([AnonMinThrottle,AnonDayThrottle])
def search(request):
    if(request.method == 'GET'):
        get_dict=dict(request.GET)
        get_dict['pagesize']=['100']
        result = cache.get(str(get_dict))
        if not result:
            r=requests.get('https://api.stackexchange.com/2.3/search/advanced?',params=get_dict)
            result=r.json()
            cache.set(str(get_dict),r.json())
        return Response(result)