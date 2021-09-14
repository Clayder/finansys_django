from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    balance = forms.FloatField(label='Limite')
    bank = forms.CharField(label='Banco')
    due_day = forms.IntegerField(label='Data de vencimento')
    closing_day = forms.IntegerField(label='Data de fechamento')
