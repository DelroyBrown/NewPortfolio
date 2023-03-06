from django.shortcuts import render, redirect
from .forms import WelcomePageVisitorNameForm


def home(request):
    visitor_name = None
    if request.method == 'POST':
        form = WelcomePageVisitorNameForm(request.POST)
        if form.is_valid():
            visitor_name = form.cleaned_data['visitor_name']
            form.save()
    else:
        form = WelcomePageVisitorNameForm()
    return render(request, 'home.html', {'visitor_name': visitor_name})


def welcome_page(request):
    if request.method == 'POST':
        form = WelcomePageVisitorNameForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            return render(request, 'home.html', {'visitor': visitor})
    else:
        form = WelcomePageVisitorNameForm()
    return render(request, 'welcome_page.html', {'form': form})
