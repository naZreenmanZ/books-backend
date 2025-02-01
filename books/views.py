from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Book, BookList
from .serializers import BookSerializer , BookListSerializer
# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookListViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all()
    serializer_class = BookListSerializer

    def create(self, request, *args, **kwargs):
        
        book_ids = request.data.get("bookIds", [])  
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            book_list = serializer.save()  

            if isinstance(book_ids, list) and book_ids:  
                books = Book.objects.filter(id__in=book_ids)  
                book_list.books.set(books)  
            
            return Response(BookListSerializer(book_list).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   
   
    @action(detail=True, methods=['post'])
    def add_books(self, request, pk=None):
        book_list = self.get_object()
        book_ids = request.data.get("book_ids", [])  # Expecting list of book IDs

        if not isinstance(book_ids, list):
            return Response({"error": "book_ids must be a list of numbers"}, status=status.HTTP_400_BAD_REQUEST)

        books = Book.objects.filter(id__in=book_ids)  
        book_list.books.add(*books)  # ✅ Efficiently add multiple books
        return Response({"message": "Books added successfully", "books": BookSerializer(books, many=True).data}, status=status.HTTP_200_OK)
    

    @action(detail=True, methods=['delete'])
    def remove_book(self, request, pk=None):
        book_list = self.get_object()
        book_id = request.data.get("book_id")

        try:
            book = Book.objects.get(id=book_id)
            book_list.books.remove(book)
            return Response({"message": "Book removed successfully"}, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
