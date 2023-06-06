from django.shortcuts import redirect, render, get_object_or_404
from .models import goods_for_sale, category
from members.models import membersProfile,cartMembers
from seller.models import reqClient
from django.urls import reverse


# Create your views here.
cat_menu = category.objects.all()

def index(request):
    cartM = membersProfile.objects.filter(username=request.user.id)
    goods = goods_for_sale.objects.all()
    context = {
        'goods':goods,
        'cat_menu':cat_menu,
        'cartM':cartM
    }
    return render(request, 'store/index.html', context)

def search(request):
    cartM = membersProfile.objects.filter(username=request.user.id)
    if request.method == "POST":
        query = request.POST['search']
        goods = goods_for_sale.objects.filter(name__contains=query)
        context = {
            'goods':goods,
            'cat_menu':cat_menu,
            'cartM':cartM,
        }
        return render(request, 'store/index.html', context)
    
a = {
    'price':'low_price',
    'las_up': 'last_upload',
}
def shop(request):
    cartM = membersProfile.objects.filter(username=request.user.id)
    goods = goods_for_sale.objects.all().order_by('id')
    context = {
        'goods':goods,'cat_menu':cat_menu,'a':a,'cartM':cartM,
    }
    return render(request, 'store/shop.html', context)

def shop_sort(request,sortby):
    cartM = membersProfile.objects.filter(username=request.user.id)
    if sortby == "last_upload":
        goods = goods_for_sale.objects.all().order_by('-id')
    if sortby == "low_price":
        goods = goods_for_sale.objects.all().order_by('price')
    context = {
        'goods':goods,'cat_menu':cat_menu,'a':a,'cartM':cartM,
    }
    return render(request, 'store/shop.html', context)

def shop_search(request):
    if request.method == "POST":  
        cartM = membersProfile.objects.filter(username=request.user.id)
        query = request.POST['search']
        goods = goods_for_sale.objects.filter(name__contains=query)
        context = {
            'goods':goods,
            'cat_menu':cat_menu,
            'cartM':cartM,
            'a':a,
        }
        return render(request, 'store/shop.html', context)


def add_cart(request, pk):
    if request.user.is_authenticated:
        cartU =  goods_for_sale.objects.get(id=pk)
        c = cartMembers.objects.all()
        mycart = request.user.membersprofile
        for i in c:
            if cartU.id == i.product.id and mycart.id == i.user.id:
                print('same')
                return redirect('cart-page', request.user.id)
        mycart.cart.add(cartU)
        mycart.save()
        cartMembers.objects.create(
            user=mycart,
            product=cartU,
        )
        return redirect('cart-page', request.user.id) 
    return redirect('cart-page', request.user.id) 
    
def remove_cart(request, pk):
    if request.user.is_authenticated:
        get_c = cartMembers.objects.get(id=pk)
        id_cart = get_c.product.id
        cartU =  goods_for_sale.objects.get(id=id_cart)
        mycart = request.user.membersprofile
        mycart.cart.remove(cartU)
        mycart.save()
        get_c.delete()
        return redirect('cart-page', request.user.id) 
    return redirect('cart-page', request.user.id)     

def cart(request,pk):
    cartM = membersProfile.objects.filter(username=request.user.id)
    carts = cartMembers.objects.filter(user=pk)
    b =0
    for i in carts:
        b = b+i.Total_per_product
    context = {
        'carts':carts,
        'cat_menu':cat_menu,
        'cartM':cartM, 'b':b,
    }
    return render(request, 'store/cart.html', context)

def updatecart(request, pk):
    if request.user.is_authenticated:
        c = cartMembers.objects.get(id=pk)
        varTwo = request.POST['varTwo']
        if request.method == "POST":
            c.quantity_cart = float(varTwo)
            c.save()
            return redirect('cart-page', request.user.id) 
        return redirect('cart-page', request.user.id) 


def checkout(request,pk):
    cartM = membersProfile.objects.filter(username=pk)
    for i in cartM:
        id_c = i.id
    carts = cartMembers.objects.filter(user=id_c)
    b =0
    for i in carts:
        b = b+i.Total_per_product
    context = {
        'cartM':cartM,
        'cat_menu':cat_menu,'b':b,
        'carts':carts,
    }
    return render(request, 'store/checkout.html', context)

def send_checkout(request,pk):
    cartM = membersProfile.objects.filter(username=pk)
    for i in cartM:
        for x in i.cart.all():
            c = cartMembers.objects.filter(product=x.id)
            d = 0
            for j in c:
                d = j.product.id
                if j.product.id == x.id and j.user.id == i.id:
                    reqCl = reqClient.objects.all()
                    for h in reqCl:
                        if h.client.id == j.id:
                            rr = reqClient.objects.get(id=h.id)
                            rr.delete()
                    req = cartMembers.objects.get(id=j.id)
                    reqClient.objects.create(
                        client = req
                    )
    return redirect('home')
    

def detail_view(request, slug):
    cartM = membersProfile.objects.filter(username=request.user.id)
    goods = goods_for_sale.objects.filter(slug=slug)
    context ={
        'goods':goods,
        'cat_menu':cat_menu,
        'cartM':cartM
    }
    return render(request, 'store/detail_view.html', context)

def filterByCat(request,pk):
    cartM = membersProfile.objects.filter(username=request.user.id)
    goods = goods_for_sale.objects.filter(category=pk)
    context = {
        'goods':goods,
        'cat_menu':cat_menu,
        'cartM':cartM
    }
    return render(request, 'store/index.html', context)