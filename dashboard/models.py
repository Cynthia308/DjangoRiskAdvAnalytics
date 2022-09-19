from django.db import models


class Equity(models.Model):
    # product_category = models.CharField(max_length=20)
    # payment_method = models.CharField(max_length=50)
    # shipping_cost = models.CharField(max_length=50)
    # unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    start_date= models.DateField()
    end_date= models.DateField()
