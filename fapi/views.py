from rest_framework.generics import ListAPIView
from myapp.models import Books
from .serializers import BookSerializer


class BookAPIView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
