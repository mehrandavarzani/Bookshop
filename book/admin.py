from django.contrib import admin
from .models import Book,Author,Bookmark


class BookAdmin(admin.ModelAdmin):

    list_display = ('title','desc')
    search_fields = ('title','desc')


admin.site.register(Book,BookAdmin)
admin.site.register([Author,Bookmark])
