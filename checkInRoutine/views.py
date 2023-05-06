from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def step1(request):
    return HttpResponse("welcome to check GHC ins")
def gotoStep1(request):
    return redirect('checkInRoutine:step1')