from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from product.forms import ProductForm
from product.models import Product
from django.views.generic import CreateView

def dashboard(request):
    return render(request, "dashboard.html")

def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)

class SaveProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse("product:product_list")

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

# def add_weight_range(request):
#     form = WeightRangeForm(request.POST or None,  request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("product:product_list"))
#     context = {"form": form}
#     return render(request, "form.html", context)