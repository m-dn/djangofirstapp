from django import forms
from .models import Stock
from .models import myWallet


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('company_name', 'short_form', 'price', 'price_date')
        labels = {
            'company_name': 'Company Name',
            'short_form': 'WSE CODE',
            'price': 'Stock Value',
            'price_date': 'Value date of the stock market',
        }

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.fields['price_date'].required = False


class MyWalletForm(forms.ModelForm):
    class Meta:
        model = myWallet
        fields = ('company_name', 'quantity')
        labels = {
            'company_name': 'Company Name',
            'quantity': 'Stock Quantity',
        }

    def __init__(self, *args, **kwargs):
        super(MyWalletForm, self).__init__(*args, **kwargs)
