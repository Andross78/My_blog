from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostAPI(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "head", "delete"]

    def perform_create(self, serializer):
        serializer.save()


class CommentAPI(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "post", "put", "head", "delete"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)