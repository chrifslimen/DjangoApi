from rest_framework import serializers
from .models import Artical
from .models import compte, Photo


class ArticalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artical
        fields = ['id', 'title', 'email', 'auth']

class compteSerializer(serializers.ModelSerializer):
    class Meta:
        model = compte
        fields = ['id', 'email', 'userName', 'password']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'date']