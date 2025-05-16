
from .views import CustomerCreateView,CustomerListView,CustomerUpdateView
from django.urls import path


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('new/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
]