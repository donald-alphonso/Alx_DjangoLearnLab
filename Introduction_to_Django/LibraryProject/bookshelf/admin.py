from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Fields to display in admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Fields to filter by in admin list view
    list_filter = ('author', 'publication_year')
    
    # Searchable fields in admin
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)
