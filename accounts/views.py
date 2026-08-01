from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm
from .forms import UserLoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .decorators import candidate_required
from .decorators import employer_required

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    if request.method == "POST":

        form = UserLoginForm(request, data=request.POST)

        if form.is_valid():

            login(request, form.get_user())

            return redirect("home")

    else:

        form = UserLoginForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
        },
    )

def register_view(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    else:

        form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        },
    )
    
def logout_view(request):
        logout(request)
        return redirect("home")
    
@login_required
@candidate_required
def candidate_dashboard(request):

    return render(
        request,
        "accounts/candidate_dashboard.html"
    )  
    
@login_required
@employer_required
def employer_dashboard(request):

    return render(
        request,
        "accounts/employer_dashboard.html"
    )      
    
    
