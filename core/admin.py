from django.contrib import admin
from django.contrib.auth.models import User

from core.models import Books, BookBorrowing


class BooksAdmin(admin.ModelAdmin):
    list_display = ("book_name", "count")


class BookBorrowingAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "date")


admin.site.register(Books, BooksAdmin)
admin.site.register(BookBorrowing, BookBorrowingAdmin)
