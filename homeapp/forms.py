from django import forms


class ItemSearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False)
    category = forms.CharField(max_length=50, required=False)
    # min_price = forms.DecimalField(required=False)
    # max_price = forms.DecimalField(required=False)