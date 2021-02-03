from django.db import models

# Create your models here.

class Inventory(models.Model):
    index = models.BigIntegerField(primary_key=True, verbose_name="Index")
    item_name = models.TextField(verbose_name="Item Name")
    quantity = models.BigIntegerField(verbose_name="Quantity")
    sell_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Sell Price")
    buy_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Buy Price") 


class Sales(models.Model):
    saleNumber = models.BigIntegerField(primary_key=True, verbose_name="Sale Number")
    item_name = models.TextField(verbose_name="Item Name")
    amount_sold = models.BigIntegerField(verbose_name="Amount sold")
    profit = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Profit")
