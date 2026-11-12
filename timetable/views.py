from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):
    slots = TimeSlot.objects.all()

    return render(request, 'timetable/timetable.html', {'slots': slots})