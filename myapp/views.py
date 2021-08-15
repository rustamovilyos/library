from django.views.generic import ListView
from .models import Books


class BookListView(ListView):
    model = Books
    template_name = 'myapp/bookList.html'

