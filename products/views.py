from django.shortcuts import render, redirect
from .models import Product,Category
from .forms import CategoryForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def show(request, product_id):
    product = Product.objects.get(pk=product_id)
    other_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    return render(request, 'products/show.html', {'product': product, 'other_products': other_products})
@login_required
def delete(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products_index')
def create_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES['image']
        instock = 'instock' in request.POST
        category_id = request.POST['category']
        category = Category.objects.get(pk=category_id)
        product = Product(name=name, price=price, description=description, image=image, instock=instock, category=category)
        product.save()
        return redirect('products_index')
    return render(request, 'products/create.html', {'categories': categories})
@login_required
def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.description = request.POST['description']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.instock = 'instock' in request.POST
        product.save()
        return redirect('products_index')
    return render(request, 'products/edit.html', {'product': product})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'products/categories.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'products/category_detail.html', {'category': category})
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    return render(request, 'products/create_category.html', {'form': form})

class CategoryEdit(LoginRequiredMixin,UpdateView):
    model = Category
    fields = ['name', 'info', 'image']
    template_name_suffix = '_edit'
    success_url = reverse_lazy('categories')  # Change to desired URL after edit

class CategoryDelete(LoginRequiredMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('categories')
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)