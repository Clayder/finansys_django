from django.shortcuts import render

from accounts.forms import SubscriptionForm


def get_account(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'accounts/account_form.html', context)
