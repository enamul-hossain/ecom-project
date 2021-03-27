from django.shortcuts import render
from EcomApp.models import Setting
from Products.models import Product

# Create your views here.
def Home(request):
    setting=Setting.objects.get(id=1)
    sliderimg = Product.objects.all().order_by('id')[:2]
    context = {'setting': setting, 'sliderimg': sliderimg}
    return  render(request, 'home.html', context)