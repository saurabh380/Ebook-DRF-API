from django.shortcuts import render
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins,generics
from .serailizers import *
from rest_framework.generics import get_object_or_404

# Create your views here.

class ebook_create(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                GenericAPIView):
    queryset = Ebook.objects.all()
    serializer_class = ebookserializer

    def get(self,request,*args,**kwargs):
        return self.list(request,args,kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class ebook_listview(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = ebookserializer

class ebook_detailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = ebookserializer

class review_create(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = reviewserializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook_detail = get_object_or_404(Ebook,id=ebook_pk)
        serializer.save(ebook = ebook_detail)

class review_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = reviewserializer













