from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'book'

router = DefaultRouter()

router.register('book',views.BookView)
router.register('author',views.AuthorView)
# router.register('bookmark',views.BookmarkView)
router.register('bookv',views.BookViewSet)

urlpatterns = [
    path('booklist',views.BookList.as_view()),
    # path('bookr/<int:id>/',views.Bookre.as_view()),
    path('bookc',views.BookCreate.as_view()),
    path('bookd/<int:pk>',views.BookDelete.as_view()),
    path('booku/<int:pk>', views.BookUpdate.as_view()),
    path('bookmark/',views.UserBookmark.as_view())
]+router.urls