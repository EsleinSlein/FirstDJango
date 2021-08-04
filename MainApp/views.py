from django.http import Http404
from django.shortcuts import render, HttpResponse
from MainApp.models import Items
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    context = {
        "name": "Евгений",
        "surname": "Юрченко",
        "hobbies": ["programming", "bike", "sleep"]
    }
    return render(request, "index.html", context)


def about(request):
    name = 'Михаил'
    second_name = 'Викторович'
    surname = 'Никитенко'
    tel = '8-999-999-99-99'
    email = 'xm4dn355x@gmail.com'
    return HttpResponse(f'Имя: <b>{name}</b><br>Отчество: <b>{second_name}</b><br>'
                        f'Фамилия: <b>{surname}</b><br>Телефон: <b>{tel}</b><br>'
                        f'e-mail: <b>{email}<b>')


def items(request):
    items = Items.objects.all();
    context = {"items":items}
    return render(request, "items_list.html", context)


def item_details(request, id):
    try:
        items = Items.objects.get(pk=id);
    except ObjectDoesNotExist:
        raise Http404
    context = {
                "item": items
            }
    return render(request, "item_page.html", context)
