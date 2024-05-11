from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Books
# Create your views here.

'''class BookListView(View):
    def get(self, request):
        book = Books.objects.all().order_by('-created_at')
        return render(request, 'book_list.html', {'books': book})'''

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    context_object_name = 'books'    


class BookDetailView(View):
    model = Books
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Books
    template_name = 'book_create.html'
    fields = ['title', 'description', 'price', 'category', 'image', 'page', 'book_lang']

class BookUpdateView(UpdateView):
    model = Books
    template_name = 'book_update.html'
    fields = ['title', 'description', 'price', 'category', 'image', 'page', 'book_lang']

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book_delete.html'
    success_url = '/'

