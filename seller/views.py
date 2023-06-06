from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth import login, logout, authenticate
from guestWebsite.models import goods_for_sale
from django.urls import reverse_lazy
from .models import sellerProfile, reqClient
from members.models import membersProfile
from members.forms import regisForm
from .form import postForm


# Create your views here.
class homeSeller(ListView):
    model = goods_for_sale
    template_name = "seller/home-seller.html"
    fields = "__all__"
    

def detileViewSeller(request, pk):
    goods = goods_for_sale.objects.filter(id=pk)
    context = {'goods':goods}
    return render(request, 'seller/detail_view-seller.html', context)


class postProduct(CreateView):
    model = goods_for_sale
    form_class = postForm
    template_name = 'seller/post-product.html'
    success_url = reverse_lazy('seller-home')


def requestClient(request):
    req = reqClient.objects.all()
    user = membersProfile.objects.all()
    y = 0
    x = []
    for i in req:
        for j in user:
            if i.client.user.username.id == j.username.id:
                if i.client.user.username.id == y:
                    continue
                else:
                    x.append(i.client.user.username.id)
                    y = i.client.user.username.id
                    print(y)
        
    context = {
        "user_req":user,
        "x_user":x,
    }
    return render(request, 'seller/request-client.html', context )            

def registerSeller(request):
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
            return redirect('seller-home')
    else:
        context ={
            'form':form,
        }
        return render(request, 'seller/register.html', context)

def loginSeller(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seller-home')
    return render(request, 'seller/login.html')

def logoutSeller(request):
    logout(request)
    return redirect('login-seller')

def profileSeller(request,pk):
    profile = sellerProfile.objects.filter(user=pk)
    context={
        'profile_user':profile,
    }
    return render(request, 'seller/profile-seller.html', context)

def detileReqClient(request, pk):
    cartM = reqClient.objects.all()
    membr= membersProfile.objects.filter(id=pk)
    context = {
        'cartM':cartM,
        'x':pk,
        'membr':membr,
    }
    return render (request, 'seller/detile-request-client.html', context)
    
def DeleteProduct(request, pk):
    if request. user.is_authenticated:
        goods = goods_for_sale.objects.get(id=pk)
        goods.delete()
        return redirect('seller-home')
    
class UpdateProduct(UpdateView):
    model = goods_for_sale
    form_class = postForm
    template_name = 'seller/post-product.html'
    success_url = reverse_lazy('seller-home')
    
    
    
