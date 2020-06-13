from django.contrib import admin
from .models import Stock, Broker
from .models import MyWallet

admin.site.register(Stock)
admin.site.register(MyWallet)
admin.site.register(Broker)
