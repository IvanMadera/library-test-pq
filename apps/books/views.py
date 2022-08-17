from django.shortcuts import render
from rest_framework import viewsets
from apps.books.models import Books
from apps.books.serializers import BookSerializer
from rest_framework.response import Response
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    # def destroy(self, request, *args, **kwargs):
    #     books = self.get_object()
    #     books.title = "Prueba4"
    #     books.save()
    #     return Response({}, status=204)