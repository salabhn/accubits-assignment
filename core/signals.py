from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import BookBorrowing, Books


@receiver(post_save, sender=BookBorrowing)
def update_available_books_count(sender, instance, created, **kwargs):
    if created:
        if instance.book.count > 0:
            Books.objects.filter(id=instance.book_id).update(count=F('count') - 1)
    else:
        # ASSUMPTION: Update happens when borrowed book is returned
        Books.objects.filter(id=instance.book_id).update(count=F('count') + 1)
