from django.shortcuts import render
from .models import Stock

# def freeze(stocks):
#     if isinstance(stocks, dict):
#         return frozenset((key, freeze(value)) for key, value in stocks.items())
#     elif isinstance(stocks, list):
#         return tuple(freeze(value) for value in stocks)
#     return stocks

def stock_list(request):
    stocks = Stock.objects.all
    return render(request, 'StockTrading/stock_list.html', {'stocks': stocks})
