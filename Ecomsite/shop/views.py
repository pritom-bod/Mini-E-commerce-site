from django.shortcuts import render
from .models import Products, order
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    product_object = Products.objects.all()

    #search code here
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        product_object = product_object.filter(title__icontains =item_name) 
    
    #paginator code here
    paginator = Paginator(product_object,4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)


    return render(request, 'shop/index.html', {'product_object':product_object})


def detail(request, id):
    product_objects = Products.objects.get(id=id)
    return render(request, "shop/detail.html", {'product_objects':product_objects})


def checkout(request):

    if request.method == "POST":
        item = request.POST.get('item')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        total = request.POST.get('total')

        Order = order(total=total, item=item, name=name, email=email, address=address,  city=city, state=state, zipcode=zipcode)
        Order.save()
        
    return render(request, 'shop/checkout.html')