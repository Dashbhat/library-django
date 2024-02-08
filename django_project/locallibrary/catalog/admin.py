from django.contrib import admin
from .models import Author, Genre, Book, BookInstan

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class BooksInstanceInline(admin.TabularInline):
    model = BookInstan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Define the display_genre function outside the BookAdmin class
def display_genre(self):
    """Create a string for the Genre. This is required to display genre in Admin."""
    # return ', '.join(genre.name for genre in self.genre.all()[:3])
    return','.join(genre.name for genre in self.genre.all()[:3])

# Check if BookAdmin is already registered and unregister it before registering again
if admin.site.is_registered(Book):
    admin.site.unregister(Book)

# Register the display_genre function with the admin site
admin.site.register(Book, BookAdmin)
BookAdmin.display_genre = display_genre
