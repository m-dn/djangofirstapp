from django.db import models
from django.utils import timezone


class Stock(models.Model):
    company_name = models.CharField(max_length=40)
    short_form = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    price_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.price_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name


class myWallet(models.Model):
    company_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.company_name)


