from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=500,null=True)
    author = models.ForeignKey(
        to='book.Author',related_name='books',on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title


class Bookmark(models.Model):
    user = models.ForeignKey(to='account.User',related_name='bookmarks',
                             on_delete=models.CASCADE)
    book = models.ForeignKey(to='book.Book',related_name='bookmarks',
                             on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title
