from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
  permission_classes = (IsAuthorOrReadOnly,)
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
