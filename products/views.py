from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()
    query = None

    # seraching for products
    if request.GET:
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
    }
    
    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ A view to show product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_details.html', context)