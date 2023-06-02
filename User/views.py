from datetime import date
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from .models import User

# Create your views here.

class UserView(View):
    def get(self,request):
            user = User.objects.first()
            years_passed = (date.today()-user.date_of_birth).days//365
            data = {
                  'firstname': User.firstname,
                  'lastname': User.lastname,
                  'date_of_birth': User.date_of_birth,
                  'years_passed': years_passed
                }

            return JsonResponse(data)


