from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def validator(price_value):
    if price_value < 0:
        raise ValueError('Price cannot be less than 0')


class Broker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cash = models.DecimalField(max_digits=8, decimal_places=2, validators=[validator])

    def __str__(self):
        return str(self.user)


class Stock(models.Model):
    company_name = models.CharField(max_length=40)
    short_form = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[validator])
    price_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.price_date = timezone.now()
        self.save()

    def __str__(self):
        return self.company_name


class MyWallet(models.Model):
    company_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE, null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.company_name)


