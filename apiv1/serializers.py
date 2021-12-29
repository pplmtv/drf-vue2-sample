from rest_framework import serializers
from shop.models import Book

import logging

logger = logging.getLogger(__name__)
logger.info('apiv1 serializers')


class BookSerializer(serializers.ModelSerializer):

    logger.info('apiv1 serializers BookSerializer class start')

    class Meta:
        model = Book
        # fields = ['id', 'title', 'price']
        fields = "__all__"

    logger.info('apiv1 serializers BookSerializer class finish')
