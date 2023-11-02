from django.urls import path
from .views import menu_view, home

urlpatterns = [
    path('menu/<str:menu_name>/', menu_view, name='menu_view'),
    path('', home, name='home'),
]