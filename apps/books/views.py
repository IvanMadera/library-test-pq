from django.shortcuts import render
from rest_framework import viewsets
from apps.books.models import Books
from apps.books.serializers import BookSerializer
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer