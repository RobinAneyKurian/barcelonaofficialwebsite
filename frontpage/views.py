from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.

def common(request):

    return render(request, 'common.html')

