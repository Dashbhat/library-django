from django.db import models
from django.urls import reverse
import uuid

# class MyModelName(models.Model):
#     """A typical class defining a model, derived from the Model class."""
#     my_field_name=models.CharField(max_length=50,help_text="enter field documention")

#     class Meta:
#         ordering=['-my_field_name']

#     def get_absolute_url(self):
#         return reverse("model-detail-view",args=[str(self.id)])
    
#     def __str__(self):
#         """string for represnting the Mymodelname object """

#         return self.my_field_name
    

class Genre(models.Model):
    name=models.CharField(max_length=200,unique=True,help_text='Enter a boog genre')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("genre_detail",args=[str(self.id)])
    
class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True,)
    # Foreign Key used because book can only have one author, but authors can have multiple books.
    # Author as a string rather than object because it hasn't been declared yet in file.

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class BookInstan(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='unique id for this particular book accross')
    book=models.ForeignKey('Book', on_delete=models.RESTRICT,null=True,related_name='instance')
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)

    LOAN_STATUS=(
        ('m','Maintainace'),
        ('o','On Loan'),
        ('a','Available'),
        ('r','Reserved'),
    )

    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default=True,
        help_text='Book Availability',
    )

    class Meta:
        ordering=['due_back']

    def __str__(self):
        """string for representing the model object"""

        return f'{self.id}({self.book.title})'
    
    

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
