from django.shortcuts import render, redirect
from .models import Stock, MyWallet
from .models import Broker
from .forms import StockForm, MyWalletForm
from django.contrib.auth.decorators import login_required

def home(request):
    return redirect('/accounts/login')

@login_required()
def stock_list(request):
    stocks = Stock.objects.order_by('company_name')
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
    wallets = MyWallet.objects.order_by('company_name')
    for wallet in wallets:
        stock = Stock.objects.get(company_name=wallet.company_name)
        setattr(wallet, 'value',  wallet.quantity*stock.price)
    return render(request, 'StockTrading/wallet_list.html', {'wallets': wallets})


@login_required()
def wallet_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MyWalletForm()
        else:
            wallet = MyWallet.objects.get(pk=id)
            form = MyWalletForm(instance=wallet)
        return render(request, 'StockTrading/wallet_form.html', {'form': form})
    else:
        if id == 0:
            form = MyWalletForm(request.POST)
        else:
            wallet = MyWallet.objects.get(pk=id)
            form = MyWalletForm(request.POST, instance=wallet)
        if form.is_valid():
            quantity = form.data['quantity']
            company_name = form.data['company_name']
            stock = Stock.objects.get(pk=company_name)
            value = int(quantity) * float(stock.price)
            broker = Broker.objects.all()[0]  #0 because first user has assigned 'cash'
            if value > broker.cash:
                return render(request, 'StockTrading/wallet_form.html', {'form': form, 'error': 'Your budget is too small to buy as many stocks'})
            form.save()
        return redirect('/stocktrading/walletlist')


@login_required()
def wallet_delete(request, id):
    wallet = MyWallet.objects.get(pk=id)
    wallet.delete()
    return redirect('/stocktrading/walletlist')


