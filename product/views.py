from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from product.forms import ProductForm
from product.models import Product

def dashboard(request):
    return render(request, "dashboard.html")

def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)

def save_product(request):
    form = ProductForm(request.POST or None,  request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("product:product_list"))
    context = {"form": form}
    return render(request, "form.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("product:product_list"))
    context = {"form": form}
    return render(request, "form.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return HttpResponseRedirect(reverse("product:product_list"))