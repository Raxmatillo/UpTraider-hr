from django.shortcuts import render
from .models import MenuItem

# Create your views here.
def menu_view(request, menu_name):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})




def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, "home.html", {'menu_items': menu_items})