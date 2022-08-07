from rest_framework import serializers
from apps.books.models import Books

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"