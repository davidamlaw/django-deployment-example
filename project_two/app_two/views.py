from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from app_two.models import AccessRecord, Topic, WebPage # ,User
# from app_two.forms import NewUser
# from . import forms
# Create your views here.
from app_two.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}

    return render(request, 'app_two/index.html', context=date_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in.")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user.form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'app_two/registration.html', {'user_form':user_form,
                                                         'profile_form':profile_form,
                                                         'registered':registered})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active.")

        else:
            print('Someone tried to log in and failed')
            print('Username: {}'.format(username))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'app_two/login.html', {})



# def form_name_view(request):
#     form = forms.FormName()
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             print("Validation Success")
#             print("Name: "+form.cleaned_data['name'])
#             print("Email: "+form.cleaned_data['email'])
#             print("Text: "+form.cleaned_data['text'])
#
#     return render(request, 'app_two/form.html', {'form':form})
#
# def users(request):
#     user_list = User.objects.order_by('first_name')
#     users_dict = {"users":user_list}
#     return render(request, 'app_two/users.html', context=users_dict)
#     form = NewUser()
#     if request.method == 'POST':
#         form = NewUser(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print("Error, Form invalid.")
#     return render(request, 'app_two/users.html', context={'form':form})

def relative(request):
    context_dict = {'text':'hello world', 'number':100}

    return render(request, 'app_two/relative_urls.html', context_dict)
