from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import UserProfile
from . forms import ProfileForm

def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        username = request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        form = ProfileForm(request.POST,request.FILES)

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email id exist")
                return redirect('register')
            else:
                if form.is_valid():
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                    profile = UserProfile(profilepic=form.cleaned_data['profilepic'], bio=form.cleaned_data['bio'], user=user)
                    profile.save()
                    user.save()
                    return redirect('login')
        else:
            messages.info(request, "Password is not matching")
            return redirect('register')
    else:
        form = ProfileForm()
        context = {'form' :form}
        return render(request, 'register.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def editprofile(request):
    if request.method == 'POST':
        username = request.user.username
        user = request.user
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        email= request.POST['email']
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = UserProfile.objects.get(user=user)
            profile.profilepic = form.cleaned_data['profilepic']
            profile.bio = form.cleaned_data['bio']
            profile.save()
            user = User.objects.filter(username=username).update(first_name=first_name,last_name=last_name,email=email)
            return redirect('home')
    else:
        user = request.user
        profile_obj = UserProfile.objects.get(user=user)
        initial_dic = {'bio':profile_obj.bio}
        form = ProfileForm(initial=initial_dic)
        context = {'user':user,'form':form}
        return render(request,'editprofile.html',context)

def logout(request):
    auth.logout(request)
    return redirect('login')
