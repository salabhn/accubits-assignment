from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Books(models.Model):
    book_name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "%s by %s" % (self.book_name, self.author)


class BookBorrowing(models.Model):
    user = models.ForeignKey(User, related_name='borrowed_by', on_delete=models.CASCADE)
    book = models.ForeignKey(Books, related_name='books_borrowed', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now().date())

