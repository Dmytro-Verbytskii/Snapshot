from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def sign_in(request):
    view = "sign_in"
    username = password = None
    if request.method == 'POST':
        form = AuthenticationForm(request)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def sign_out(request):
    view = "sign_out"
    logout(request)
    return HttpResponseRedirect('/')


def sign_up(request):
    view = "sign_up"
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'reg.html', {"form": form})
