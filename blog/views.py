from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics



class PostListView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def post(self, request, *args, **kwargs):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({}, status=400)

class PostDetailView(APIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer 

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
            
    def get(self, request, pk, format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)        
    
    def put(self, request, pk, format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400) 

    def delete(self, request, pk, format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=204)            