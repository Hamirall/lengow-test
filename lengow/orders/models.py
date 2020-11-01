from django.db import models

# Create your models here.
class Order(models.Model):
    marketplace = models.CharField(max_length=100)
    id_flux = models.IntegerField()
    order_purchase_date = models.DateField()
    order_amount = models.FloatField(null=True)
