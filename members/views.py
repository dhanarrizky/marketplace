from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import membersProfile
from django.contrib.auth.models import User
from guestWebsite.views import cat_menu
from .forms import regisForm
from guestWebsite.models import goods_for_sale

# Create your views here.
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("username or password is incorrect!!!....")
    return render(request, 'members/login.html')

def logout_page(request):
    logout(request)
    return redirect('home')

def profileView(request, pk):
    cartM = membersProfile.objects.filter(username=request.user.id)
    prof = membersProfile.objects.filter(username=pk).values()
    context ={
        'prof':prof,
        'cat_menu':cat_menu,
        'cartM':cartM,
    }
    return render(request, 'members/profile.html', context)

def register_page(request):
    form = regisForm()
    if request.method=="POST":
        form = regisForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            membersProfile.objects.create(
                username=user,
            )
            user = authenticate(username=username, password=password1)
            login(request, user)
            return redirect('home')
    else:
        context ={
            'form':form,
        }
        return render(request, 'members/register.html', context)

def updateProfile(request):
    if request.user.is_authenticated:
        first = request.POST['first']
        last = request.POST['last']
        email = request.POST['email']
        mobileNo = request.POST['mobileNo']
        address1 = request.POST['address1']
        address2 = request.POST['address2']
        country = request.POST['Country']
        city = request.POST['city']
        state = request.POST['state']
        zcode = request.POST['zCode']
        upda_User = User.objects.get(id=request.user.id)
        upda_Profile = membersProfile.objects.get(username=request.user.id)
        if request.method == 'POST':
            upda_User.first_name = first
            upda_User.last_name = last
            upda_User.email = email
            upda_Profile.mobile_no = mobileNo
            upda_Profile.address_line1 = address1
            upda_Profile.address_line2 = address2
            upda_Profile.Country = country
            upda_Profile.city = city
            upda_Profile.state = state
            upda_Profile.zip_code = zcode
            upda_User.save()
            upda_Profile.save()
            return redirect('profile', request.user.id)
        else:
            return HttpResponse('hey this page is fail !!!')

def uploadprofPic(request):
    pic_Profile = membersProfile.objects.get(username=request.user.id)
    profilePic = request.FILES['profilePic']
    if request.method == 'POST':
        pic_Profile.profile_pic = profilePic
        pic_Profile.save()
        return redirect('profile', request.user.id)
    
        
        
