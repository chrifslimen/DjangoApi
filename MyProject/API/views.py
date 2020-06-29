from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Artical, compte, Photo
from .serializers import ArticalSerializer,compteSerializer, PhotoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@csrf_exempt
def Artical_list(request):
    if request.method == 'GET':
        articles = Artical.objects.all()
        serializer = ArticalSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',

    }

    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    articles = Artical.objects.all()
    serializer = ArticalSerializer(articles, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def taskDetail(request, pk):
    articles = Artical.objects.get(id = pk)
    serializer = ArticalSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetailTitle(request, pk):
    articles = Artical.objects.get(title = pk)
    serializer = ArticalSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = ArticalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    articles = Artical.objects.get(id = pk)
    serializer = ArticalSerializer(instance=articles, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    articles = Artical.objects.get(id = pk)
    articles.delete()
    return Response("item seccsesfully delete")

@api_view(['GET'])
def compteList(request):
    comptes = compte.objects.all()
    serializer = compteSerializer(comptes, many=True)
    return Response(serializer.data)
@api_view(['GET','POST'])
def compteDetail(request):
    if request.method == 'POST':
        try:
            comptes = compte.objects.get(email = request.data.get('email'), password = request.data.get("password"))
            serializer = compteSerializer(comptes, many=False)
            return Response([{"exist": "true"}, serializer.data])
        except:
            return Response([{"exist": "false"}])
        return Response([{"exist": "bad data"}])
    elif request.method == 'GET':
        return Response("invalide request")
@api_view(['POST','GET'])
def compteCreate(request):
    try:
        comptes = compte.objects.get(email=request.data.get("email"))
        serializer = compteSerializer(comptes, many=False)
        return Response([{"exist": "true"}])
    except:
        serializer = compteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([{"exist": "false"}, serializer.data])
        return Response([{"exist": "bad data"}])


# Photo Views
@api_view(['GET'])
def photoList(request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def photoUpload(request):
    print('request.data')
    serializer = PhotoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response([{"save": "true"}, serializer.data])
    return Response([{"save": "false"}])