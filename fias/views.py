from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import AddrObj


def index(request):
    data = {}
    if request.POST:
        addr = request.POST.get('addr', '')
        data['addr'] = addr
        response = AddrObj.objects.filter(Q(formal_name__contains=addr) | Q(official_name__contains=addr))
        data['response'] = response
    return HttpResponse(render(request, 'fias/index.html', data))
