from rest_framework import serializers
from .models import *


class reviewserializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class ebookserializer(serializers.ModelSerializer):
    reviews = reviewserializer(many=True,read_only=True)
    
    class Meta:
        model = Ebook
        fields = "__all__"