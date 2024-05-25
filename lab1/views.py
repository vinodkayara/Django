from datetime import datetime
from django.shortcuts import render

# Create your views here.
def current_datetime(request):
    now = datetime.now()
    return render(request,'lab1.html',{'current_datetime':now})
