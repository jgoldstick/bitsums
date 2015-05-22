from django import forms


class BitSumForm(forms.Form):
    A = forms.IntegerField(max_value=100000000, min_value=1, required=True)
    B = forms.IntegerField(max_value=100000000, min_value=1, required=True)
