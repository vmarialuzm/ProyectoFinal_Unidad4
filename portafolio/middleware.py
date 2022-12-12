from ipware import get_client_ip
from .models import Ip
from datetime import datetime

def ip_is_valid(get_response):

    def middleware(request):

        ip, is_routable = get_client_ip(request)

        print(ip)
        print(is_routable)
        ip_data={'number_Ip':ip,'date':datetime.now()}
        Ip.objects.create(**ip_data)

        return get_response(request)

    return middleware
