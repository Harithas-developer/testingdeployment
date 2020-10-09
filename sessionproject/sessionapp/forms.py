from django import forms


class AddItemForm(forms.Form):
    name = forms.CharField(max_length=20)
    quantity = forms.IntegerField()
