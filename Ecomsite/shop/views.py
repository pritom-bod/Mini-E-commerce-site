from django.shortcuts import render
from .models import Products
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
