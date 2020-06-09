from django.shortcuts import render

def stock_list(request):
    return render(request, 'StockTrading/stock_list.html', {})
