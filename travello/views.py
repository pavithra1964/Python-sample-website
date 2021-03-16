from django.shortcuts import render
from .models import portfolio
# Create your views here.


def index(request):

    
    wells = portfolio.objects.all()
   
    return render(request, 'index.html', {'wells': wells})
