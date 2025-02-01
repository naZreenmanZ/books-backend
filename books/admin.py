from django.contrib import admin
from .models import Book, BookList


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year','author_name')



@admin.register(BookList)
class BookListAdmin(admin.ModelAdmin):
    list_display=('name',)
    filter_horizontal = ('books',)
