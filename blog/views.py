from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from .models import BlogPost
from .serializers import BlogPostSerializer


# ----- FILTERS -----
class BlogPostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author', lookup_expr='icontains')
    tags = filters.CharFilter(field_name='tags', lookup_expr='icontains')

    created_after = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_before = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = BlogPost
        fields = ['author', 'tags', 'created_after', 'created_before']


# ----- VIEWSET -----
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)

    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title', 'author']
    
    filterset_class = BlogPostFilter
