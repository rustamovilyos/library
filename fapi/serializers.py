from myapp.models import Books
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('title', 'about', 'pages', 'author', 'isbn')
