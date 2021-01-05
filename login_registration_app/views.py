from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from login_registration_app.forms import UserCreateForm

# Create Home Page Views.
@login_required
def index(request):
    return render(request,'accounts/index.html')

# Create sign Up Page Views.
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('accounts')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})
