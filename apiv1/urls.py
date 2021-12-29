from django.urls import path, include
from rest_framework import routers

from . import views

import logging

logger = logging.getLogger(__name__)
logger.info('apiv1 urls')

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path("book/", views.ListView.as_view(), name="list"),
#     path("book/<int:pk>/", views.DetailView.as_view(), name="detail"),
# ]
