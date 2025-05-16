from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Customer
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# Create your views here.

class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer

class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customers:customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('customers:customer_list')

