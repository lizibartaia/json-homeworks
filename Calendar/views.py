from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import Calendar

# Create your views here.

class CalendarView(View):
    def get(self,request):
        calendar = Calendar.objects.first()
        data = {
            'year': Calendar.year,
            'month': Calendar.month,
            'day': Calendar.day
        }

        return JsonResponse(data)