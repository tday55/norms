from django.shortcuts import render
from django.http import HttpResponse
from bnorms.models import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world, here is start of norms app.")

def boyd3(request):
    boyd_female = Boyd4.objects.filter(sex='f').order_by('low_age')
    output = [b.age + ': ' + str(b.uterus_wgt) + '</br>' for b in boyd_female]
    return HttpResponse(output)
