from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContentSerializer
from .models import Content

class ContentViewSet(viewsets.ModelViewSet):
	queryset= Content.objects.all().order_by('content')
	serializer_class = ContentSerializer
