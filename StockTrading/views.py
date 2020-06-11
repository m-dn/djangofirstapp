from django.shortcuts import render, redirect
from .models import Stock, myWallet
from .forms import StockForm, MyWalletForm
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('/accounts/login')

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
        return redirect('/stocktrading/stocklist')

@login_required()
def stock_delete(request, id):
    stock = Stock.objects.get(pk=id)
    stock.delete()
    return redirect('/stocktrading/stocklist')


@login_required()
def wallet_list(request):
    wallets = myWallet.objects.all()
    return render(request, 'StockTrading/wallet_list.html', {'wallets': wallets})


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
        return redirect('/stocktrading/walletlist')

@login_required()
def wallet_delete(request, id):
    wallet = myWallet.objects.get(pk=id)
    wallet.delete()
    return redirect('/stocktrading/walletlist')
