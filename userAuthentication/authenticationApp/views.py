from django.shortcuts import render
from authenticationApp.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'authenticationApp/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, NICE!!")

#decorator for views that only logged in people can access
@login_required
def user_logout(request):
    #built in django logout
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            #Defining the one to one relationship
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'authenticationApp/registration.html', {'user_form':user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    if request.method == "POST":
        #For simple html form
        username = request.POST.get('username')
        password = request.POST.get('password')
        #automatically authenticating user
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                #Logging in the user, thank you Django
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, 'authenticationApp/login.html',{})
