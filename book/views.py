from rest_framework import viewsets,generics,views
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .models import Book,Author,Bookmark
from .serializers import BookSerializer,AuthorSerializer,BookmarkSerializer


class BookView(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(methods=['post','delete'],detail=True,url_path='bookmark',url_name='book_bookmark')
    @csrf_exempt
    def bookmark(self,request,*args,**kwargs):
        book = self.get_object()
        user = request.user

        if request.method == 'POST':
            Bookmark.objects.create(user=user,book=book)
            return Response({"detail":"book added to bookmarks"},status=200)

        elif request.method == 'DELETE':
            try:
                bookmarks = Bookmark.objects.filter(user=user, book=book)
                bookmarks.delete()
                return Response({"detail": "bookmark removed"}, status=200)
            except Bookmark.DoesNotExist:
                return Response({"detail": 'user has not bookmarked this book'})


class AuthorView(viewsets.ReadOnlyModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookmarkView(viewsets.ReadOnlyModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = 'user'

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(user__pk=kwargs['user'])
        serializer = BookmarkSerializer(queryset,many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return Response([])


class UserBookmark(generics.RetrieveAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:

            print(user)
            queryset = self.get_queryset().filter(user=user)
            serilaizer = self.get_serializer_class()(queryset,many=True)
            return Response(serilaizer.data)
        return Response({'error':'not authenticated'},401)


class UserBookmarkDelete(generics.DestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:

            print(user)
            queryset = self.get_queryset().filter(user=user)
            serilaizer = self.get_serializer_class()(queryset,many=True)
            return Response(serilaizer.data)
        return Response({'error':'not authenticated'}, 401)


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookmarkRetrieve(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()


class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

