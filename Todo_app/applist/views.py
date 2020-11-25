from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class Todo_appViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination 
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']

