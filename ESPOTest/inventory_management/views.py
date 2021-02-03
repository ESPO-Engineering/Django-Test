from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Inventory
from .models import Sales
import csv, io




def buyProducts(request):
    obj = Inventory.objects.all()
    return render(request, "buy_products.html", {'obj': obj})

def buyProduct(request):
    item_name = request.POST.get("item_name")
    amount = request.POST.get("amount")
    sell = 0
    buy = 0

    obj = Inventory.objects.all()

    it = Inventory.objects.get(item_name=item_name)
    it.quantity -= int(amount)
    it.save()

    sell = it.sell_price
    buy = it.buy_price
            
            
    profit = float((sell - buy)) * float(amount)
    count = 1

    if not Sales.objects.all() is None:
        for i in Sales.objects.all():
            count += 1

    _, created = Sales.objects.update_or_create(
            saleNumber=count,
            item_name=item_name,
            amount_sold=amount,
            profit=profit
        )

    return render(request, "buy_products.html", { 'obj' : obj})


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

    

    return render(request, template, {})



def addSingleProduct(request):
    if request.method=="GET":
        return render(request, "addPr.html", {})
 
    _, adding = Inventory.objects.update_or_create(
            index=request.POST.get('index'),
            item_name=request.POST.get('item_name'),
            quantity=request.POST.get('quantity'),
            sell_price=request.POST.get('sell_price'),
            buy_price=request.POST.get('buy_price')
        )
    
    return render(request, 'add_products.html', {})