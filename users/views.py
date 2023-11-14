from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, login_form
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            return redirect('/login/')   
    else :
        form = SignUpForm()  
            
    return render(request, 'users/register.html', {'form':form})
 

def login_view(request):
    form = login_form(request.POST or None)
    if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user) 
                return redirect('/articles/list/') 
    
    return render(request, 'users/login.html', {'form':form})