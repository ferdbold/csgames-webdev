from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template import loader
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'spookyducky/index.html')
    
def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            
    return render(request, 'spookyducky/login.html', {'state': state, 'username': username})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('spookyducky:index'))