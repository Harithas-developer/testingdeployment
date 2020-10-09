from django.shortcuts import render
from sessionapp.forms import AddItemForm

# Create your views here.


def add_item_view(request):
    form = AddItemForm()
    if request.method == "POST":
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
        request.session.set_expiry(0)
    return render(request, 'add_item.html', {'form': form})


def display_item_view(request):
    return render(request, 'display_item.html')


def session_info_view(request):
    session = request.session
    date = session.get_expiry_date()
    age = session.get_expiry_age()
    print(date)
    print(age)
    return render(request, 'base.html')
