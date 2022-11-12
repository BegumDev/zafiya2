from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def error_404(request, exception):
    """ A view to render a custom page for 404 errors """
 
    return render(request, '404.html')


def error_500(request):
    """ A view to render a custom 500 page"""

    return render(request, '500.html')


def error_403(request, exception):
    """ A view to render a custom page for 404 errors """
 
    return render(request, '403.html')
    