from django.contrib import admin
from .models import Stock, Broker, MyWallet

admin.site.register(Stock)
admin.site.register(MyWallet)
admin.site.register(Broker)
