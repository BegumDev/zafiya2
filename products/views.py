from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ProductForm
from .models import Product, Category
from django.db.models import Q


def all_products(request):
    """ A view to show all products """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        # filter by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # seraching for products
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "You didn't enter any serach requests")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }
    
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ A view for admin to add a product """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('products'))    
        else:
            messages.error(request, "Adding product failed. Please check the form")
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please check the form again.')
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
    

def delete_product(request, product_id):
    """ A view to delete the product """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))
    