from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Inventory
import csv, io


def buyProducts(request):
    return render(request, "buy_products.html")


def viewProducts(request):
    template = 'view_products.html'
    obj = Inventory.objects.all()
    return render(request, template, {'obj': obj})


def home(request):
    return render(request, 'home.html')


def navBar(request):
    return render(request, 'nav.html')


def addProducts(request):
    template = 'add_products.html'
    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Inventory.objects.update_or_create(
            index=column[0],
            item_name=column[1],
            quantity=column[2],
            sell_price=column[3],
            buy_price=column[4]
        )

    context = {}

    return render(request, template, context)