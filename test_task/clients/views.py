from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from clients.models import Contact
from clients.forms import ContactForm
from django.urls import reverse_lazy


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
