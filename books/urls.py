from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListViewSet


router = DefaultRouter()
router.register(r'books',BookViewSet)
router.register(r'book-lists', BookListViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]