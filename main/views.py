from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    # return render(request, 'main/homepage.html', {})
    return HttpResponse("Hello, world. You're at the main homepage.")