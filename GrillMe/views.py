from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from GrillMe.models import FoodItem
# Create your views here.
class Index(TemplateView):
    template_name = "GrillMe/index.html"

class FoodList(ListView):
    model = FoodItem

class FoodCreate(CreateView):
    model = FoodItem
    success_url = reverse_lazy('food_list')
    fields = ['name','type','timer','temperature']

class FoodUpdate(UpdateView):
    model = FoodItem
    success_url = reverse_lazy('food_list')
    fields = ['name', 'type', 'timer','temperature']

class FoodDelete(DeleteView):
    model = FoodItem
    success_url = reverse_lazy('food_list')

class FoodTimer(DetailView):
    model = FoodItem
    template_name = "GrillMe/fooditem_timer.html"
