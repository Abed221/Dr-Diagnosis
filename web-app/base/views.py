from django.shortcuts import render
from django.http import HttpResponse
from . import process
# Create your views here.
def home(request):
    return render(request, 'index.html')

    
def form(request):
    return render(request, 'form.html')


def result(request):
    if request.method == 'POST':
        arr = []
        for x in range(1,14):
            arr += str(request.POST['s{n}'.format(n=x)])
    diagnosis = process.findres(arr) 
    try:
        R = diagnosis
    except diagnosis.DoesNotExist:
        raise HttpResponse("Missing information")
    return render(request, 'result.html', {'diagnosis': R})   
    #return HttpResponse(diagnosis)
