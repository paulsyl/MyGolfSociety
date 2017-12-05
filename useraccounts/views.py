from django.shortcuts import render, redirect

#Authentication libraries
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method == 'POST':
        if request.POST['username'] and request.POST['firstname'] and request.POST['surname'] and request.POST['date_of_birth'] and request.POST['email']:
        # Check that the passwords match before submitting
            if request.POST['password1'] == request.POST['password2'] :

                # Check for username uniqueness, in the event the user exists, error, otherwise submit.
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'useraccounts/signup.html', {'error': 'Username already exists!'})
                except User.DoesNotExist:
                    user = User.objects.create_user(username=request.POST['username'].rstrip(),
                                                    password=request.POST['password1'].rstrip(),
                                                    first_name=request.POST['firstname'].rstrip(),
                                                    last_name=request.POST['surname'].rstrip(),
                                                    email=request.POST['email'].rstrip(),
                                                    )
                    user.profile.date_of_birth = request.POST['date_of_birth']
                    #user.save()
                    login(request, user)  # login the user
                    return render(request, 'useraccounts/signup.html')
            # Mismatching passwords
            else:
                print("Invalid Password")
                return render(request, 'useraccounts/signup.html', {'error': 'Passwords did not match, please try again.'})
        else:
            print("Please supply all information")
            return render(request, 'useraccounts/signup.html', {'error': 'Please supply all information, please try again.'})
    else:
        return render(request, 'useraccounts/signup.html')

def home(request):
        return render(request, 'useraccounts/home.html')

def userlogin(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            print("logged in")
            """ if the user arrived here via the redirect from the authentication, then following the login,
             send the user back to their original page, first check to see if name of the rediect is contained
             within the POST request"""
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return render(request, 'results/dashboard.html')
        else:
            print("Invalid Login")
            return render(request, 'useraccounts/home.html', {'error': 'The username and password not found'})
    else:
        return render(request, 'results/dashboard.html')

def userlogout(request):   # Logout's should always be a POST request as browsers guess about GET requests
    if request.method == 'POST':
        logout(request)
        return redirect('home')
