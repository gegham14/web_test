from django.shortcuts import render
from .models import Items
from clients.models import Client


def index(request):

    items = Items.objects.all()
    client = Client.objects.all()
    data = {'items': items, 'client': client}
    return render(request, 'index.html', context=data)
