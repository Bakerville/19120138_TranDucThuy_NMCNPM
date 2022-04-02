from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html')
def contact(request):
    return HttpResponse("19120138-TranDucThuy")
def customer(request):
    return render(request, "accounts/customer.html")
def products(request):
    return render(request, 'accounts/products.html')
