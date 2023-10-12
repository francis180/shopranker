from django.http import HttpResponseRedirect
from django.shortcuts import render


def landing(request):
    return render(request, 'landing/landing.html')
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('/dashboard/')
    # else:
    #     return HttpResponseRedirect('/auth/login/')
