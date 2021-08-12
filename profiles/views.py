from django.shortcuts import render
from profiles.forms import SignUpForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, authenticate
from django.urls import reverse
# Create your views here.
def signup(request):
    form = SignUpForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)    
                return HttpResponseRedirect(reverse('bboard:index')) 
            else:
                raise Http404("Пользователь с такими данными не найден")


    else:
        form = SignUpForm()
    return render(request, 'profiles/sign_up.html', {'form': form})


def login(request):
    form = SignUpForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)    
                return HttpResponseRedirect(reverse('bboard:index')) 
            else:
                raise Http404("Пользователь с такими данными не найден")


    else:
        form = SignUpForm()
    return render(request, 'profiles/sign_up.html', {'form': form})
