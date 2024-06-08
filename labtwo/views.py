from django.shortcuts import render
from datetime import datetime, timedelta

def current_datetime(request):
    now = datetime.now()
    five_hours_before = now - timedelta(hours=5)
    five_hours_after = now + timedelta(hours=5)
    context = {
        'current_datetime': now,
        'five_hours_before': five_hours_before,
        'five_hours_after': five_hours_after
    }
    return render(request, 'lab2.html', context)
