from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shop.models import Book
from .serializers import BookSerializer

import logging

logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ModelViewSet):
    """本モデルのCRUD用APIクラス"""

    logger.info('apiv1 views BookViewSet class start')

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    logger.info('apiv1 views BookViewSet class finish')


class ListView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('-id')
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
