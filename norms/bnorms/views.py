from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from bnorms.models import *

# Create your views here.

def index(request):
    return HttpResponse("Hello, world, here is start of norms app.")

def boyd3(request):
    boyd_female = Boyd4.objects.filter(sex='f').order_by('low_age')
    #template = loader.get_template('bnorms/index.html')
    context = {
        'boyd_female': boyd_female,
    }
    return render(request, 'bnorms/index.html', context)
    #return HttpResponse(template.render(context, request))
    
def boyd3onegirl(request, value):
    try:
        low_age = float(value)
        wgts = Boyd4.objects.filter(low_age=low_age, sex='f')
        context = {'wgts': wgts}
    except Boyd4.DoesNotExist:
        raise Http404("No records for that age")
    return render(request, 'bnorms/onegirlboyd.html', context)