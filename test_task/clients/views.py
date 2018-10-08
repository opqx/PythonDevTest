from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from clients.models import Contact
from clients.forms import ContactForm
from django.urls import reverse_lazy

from django.shortcuts import render
import requests
from lxml import html
from io import StringIO


def about_us(request):
    url = "https://breffi.ru/ru/about"
    r = requests.get(url, verify=False)
    root = html.parse(
        StringIO(r.text)
    ).getroot()
    elem = root.cssselect('div.worth > div.content-section__layout > div.content-section__item')
    title = root.cssselect('div.worth > div.content-section__layout > div.content-section__title')

    resutl = []
    for i in elem[:5]:
        resutl.append( (i[0].text, i[1].text, i[2].text_content()) )
    
    return render(request, 'clients/about_us.html', {
        'title': title[0].text,
        'resutl': resutl,
    })


class List(ListView):
    model = Contact
    paginate_by = 2


class View(DetailView):
    model = Contact


class Create(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'company', 'interest']
    template_name = 'clients/contact_create.html'

class Update(UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone', 'company', 'interest']

class Delete(DeleteView):
    model = Contact
    success_url = reverse_lazy('list')
