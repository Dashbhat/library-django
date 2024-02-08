from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstan, Genre
from django.shortcuts import get_object_or_404

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstan.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstan.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def book_detail_view(request, pk): #here we should pass the agrs means pk same as in the urls.py file what we mention it like that only.
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', context={'book': book})


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'  # Update to the correct template path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
