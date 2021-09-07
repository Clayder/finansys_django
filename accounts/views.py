from django.shortcuts import render


def get_account(request):
    return render(request, 'accounts/account_form.html')
