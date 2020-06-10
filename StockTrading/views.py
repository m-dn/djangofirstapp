from django.shortcuts import render, redirect
from .models import Stock, myWallet
from .forms import StockForm
from .forms import MyWalletForm
from django.contrib.auth.decorators import login_required

# def home(request):
#     return render(request, 'StockTrading/home.html')

@login_required()
def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'StockTrading/stock_list.html', {'stocks': stocks})


@login_required()
def stock_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StockForm()
        else:
            stock = Stock.objects.get(pk=id)
            form = StockForm(instance=stock)
        return render(request, 'StockTrading/stock_form.html', {'form': form})
    else:
        if id == 0:
            form = StockForm(request.POST)
        else:
            stock = Stock.objects.get(pk=id)
            form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
        return redirect('StockTrading/stocklist.html')

@login_required()
def stock_delete(request, id):
    stock = Stock.objects.get(pk=id)
    Stock.delete()
    return


@login_required()
def wallet_list(request):
    wallet = myWallet.objects.all()
    return render(request, 'StockTrading/wallet_list.html', {'wallet': wallet})


@login_required()
def wallet_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MyWalletForm()
        else:
            wallet = myWallet.objects.get(pk=id)
            form = MyWalletForm(instance=wallet)
        return render(request, 'StockTrading/wallet_form.html', {'form': form})
    else:
        if id == 0:
            form = MyWalletForm(request.POST)
        else:
            wallet = myWallet.objects.get(pk=id)
            form = MyWalletForm(request.POST, instance=wallet)
        if form.is_valid():
            form.save()
        return redirect('StockTrading/walletlist.html')

@login_required()
def wallet_delete(request, id):
    wallet = myWallet.objects.get(pk=id)
    myWallet.delete()
    return
