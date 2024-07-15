from rest_framework import serializers
from .models import Book,Author,Bookmark


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','author','title','desc')


class BookmarkSerializer(serializers.ModelSerializer):

    book = BookSerializer()

    class Meta:
        model = Bookmark
        fields = ('id','book')
