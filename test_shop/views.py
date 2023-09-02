# Create your views here.
import io
import os

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import *
from rest_framework import routers

from .models import *
from .permissions import *
from .serializers import *
from django.contrib.gis.geoip2 import GeoIP2

class ModelAnusViewSet(ModelViewSet):
    permission_classes = (PenisPermission, AnusPermission, )
    queryset = Article.objects.all()
    serializer_class = PenisSerializer

class AnusViewSet(ViewSet):
    # permission_classes = (PenisPermission, AnusPermission, )
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def list(self, request):
        #po fanu
        g = GeoIP2()
        # print(os.path.join(os.getcwd(), 'geo2'))
        print(request.META.get('HTTP_X_FORWARDED_FOR'))
        print(request.META.get('REMOTE_ADDR'))
        # g.country(request.META.get('REMOTE_ADDR'))
        print(g.city('google.com'))
        print(g.city('93.76.176.71'))
        print(request.user)
        # print(g.city(request.META.get('REMOTE_ADDR')))
        serial = PenisSerializer(Article.objects.all(), many=True)
        # self.get_queryset()
        return Response(serial.data)

    def retrieve(self, request, pk=None):
        print(pk)
        try:
            instance = Article.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(PenisSerializer(instance).data)

class PenisViewSet(ModelViewSet):
    serializer_class = TestSerializer
    # queryset = Article.objects.all()
    def get_queryset(self, pk=None):
        if not pk:
            return Article.objects.all()
        return Article.objects.filter(id=pk)

    @action(methods=['get'], detail=True)
    def hui(self, request, pk=None):
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'hui'})
        try:
            instance = CategoryArticle.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'hui2'})
        return Response(status=status.HTTP_200_OK, data={'data':CategorySerializer(instance).data})

class PenisView(APIView):
    # permission_classes = (IsAuthenticated, )
    permission_classes = (AllowAny, )

    def get(self, request):
        quer = Article.objects.all()
        serial = PenisSerializer(quer, many=True)
        return Response(data={'data':serial.data})

    def post(self, request):
        serial = PenisSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response(status=status.HTTP_200_OK, data={'data':serial.data})

    def put(self, request, id=None):
        if not id:
            return Response(status.HTTP_400_BAD_REQUEST, data={'message':'sosi'})
        try:
            instance = Article.objects.get(id=id)
        except:
            return Response(status.HTTP_400_BAD_REQUEST, data={'message':'sosi'})
        serial = PenisSerializer(data=request.data, instance=instance)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response(status=status.HTTP_200_OK, data={'data':serial.data})


class ArticlesCRAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class ArticleAPIView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class ArticleClearAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = TestSerializer

























#-------------------------------------------------

class hui:
    def __init__(self):
        self.penis='her'
        self.menis=10

class ZakrViewSet(ModelViewSet):
    serializer_class = TestSerializer
    # queryset = Article.objects.all()

    def get_queryset(self, pk=None):
        if not pk:
        #     serial = TestSerializer(Article.objects.all(), many=True)
        #     return Response(status=status.HTTP_200_OK, data={'data':serial})
        # serial = TestSerializer(Article.objecs.get(id=pk))
        # return Response(status=status.HTTP_200_OK, data={'data': serial})
            return Article.objects.all()
        return Article.filter(id=pk)

    @action(methods=['get'], detail=True, serializer_class=CategorySerializer)
    def penis(self, request, pk=None):
        # print('popa', pk)
        if not pk:
            serial = self.serializer_class(CategoryArticle.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data={'data':serial.data})
        try:
            serial = self.serializer_class(CategoryArticle.objects.get(id=pk))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'No cat with such an id'})
        return Response(status=status.HTTP_200_OK, data={'data': serial.data})


class TestViewSet(ModelViewSet):
    #queryset = Article.objects.all()
    serializer_class = TestSerializer

    def get_queryset(self, pk=None):
        if not pk:
            return Article.objects.all()
        return Article.objects.filter(id=pk)

    # @action(methods=['get', 'put'], detail=True, serializer_class=CategorySerializer)
    # def cats(self, request, pk=None):
    #     if request.method == 'GET':
    #         list = CategoryArticle.objects.all()
    #         serial = self.serializer_class(list, many=True)
    #         return Response(status=status.HTTP_200_OK, data={'data': serial.data})
    #     try:
    #         instance = CategoryArticle.objects.get(id=pk)
    #     except:
    #         return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'No such an id!'})
    #     serial = self.serializer_class(instance=instance, data=request.data)
    #     serial.is_valid(raise_exception=True)
    #     serial.save()
    #     return Response(status=status.HTTP_200_OK, data={'data': serial.data})

class TestCatViewSet(ModelViewSet):
    queryset = CategoryArticle.objects.all()
    serializer_class = CategorySerializer

class RestAtView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = TestSerializer

class RestUdView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = TestSerializer

class RestGenView(APIView):

    def get(self, request):
        serial = TestSerializer(
            Article.objects.all(),
            many=True
        )
        return Response(status=status.HTTP_200_OK, data={'articles':serial.data})

    def post(self, request):
        serial = TestSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        #extr_data = serial.validated_data
        # new_art = Article.objects.create(
        #     name=extr_data['name'],
        #     content_mockup='Hui',
        #     category=extr_data['category'],
        # )
        # return Response(status=status.HTTP_200_OK, data={'result':model_to_dict(new_art)})
        #arc = {'name':'penis', 'content_mockup':'benis', 'category':CategoryArticle.objects.get(id=2)}
        serial.save()
        return Response(status=status.HTTP_200_OK, data={'result': serial.data})

    def put(self, request, *args, **kwargs):
        id = args.get('id', None)
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'No object id stated in request!'})
        try:
            instance = Article.objects.get(id=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'No object found with stated id!'})

        serial = TestSerializer(data=request.data, instance=instance)
        print(model_to_dict(instance))
        serial.is_valid()
        serial.save()
        return Response(status=status.HTTP_200_OK, data={'result':serial.data})

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'No id stated!'})
        try:
            instance = Article.objects.get(id=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message':'No record with such an id!'})

        serial = TestSerializer(instance)
        return Response(status=status.HTTP_200_OK, data={'result':serial.data})














#------------------------------------------------------------

class TestArticleList(generics.ListAPIView):
    queryset = Article.objects.all().filter(id=2)
    serializer_class = TestSerializer

class DJBasicTemplateView(TemplateView):
    template_name = 'penis.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Article.objects.all()
        return context

class TestArticle(View):
    def get(self, request):
        serializer = TestSerializer(Article.objects.all(), many=True)
        return HttpResponse(status=status.HTTP_200_OK, content={'message':f'Penis!', 'data':serializer.data})

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_article = Article.objects.create(
            name=serializer.validated_data['name'],
            category=serializer.validated_data['category']
        )
        return Response({'message':f'POST delivered! ({model_to_dict(new_article)})'}, status=status.HTTP_200_OK)


















#--------------------------------------------

class ArticlesAPIView(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        return Response({'data':ArticleSerializer(queryset, many=True).data}, status=status.HTTP_200_OK)

    def post(self, request):
        exmplr = ArticleSerializer(data=request.data)
        print(request.data)
        exmplr.is_valid(raise_exception=True)
        print(exmplr.validated_data)
        new_inst = Article.objects.create(
            name=exmplr.validated_data['name'],
            content_mockup=exmplr.validated_data['content_mockup'],
            category=exmplr.validated_data['category']
        )
        return Response(status=status.HTTP_200_OK, data=model_to_dict(new_inst))

class ArticlesAPIView(APIView):
    def get(self, request):
        queryset = Article.objects.all().values()
        return Response({'data': list(queryset)})

    def post(self, request):
        new_article = Article.objects.create(
            name=request.data['name'],
            content_mockup=request.data['content_mockup'],
            category_id=request.data['category_id']

        )
        print(type(model_to_dict(new_article)))
        return Response({'post':model_to_dict(new_article)}, status=status.HTTP_200_OK)

# @csrf_exempt
# def test_get(request):
    # str = io.BytesIO(b'{"name":"article1","category_id":2,"content_mockup":"yes_no"}')
    # data = JSONParser().parse(str)
    # ser = TestSerializer(data=data)
    # if(ser.is_valid()):
        # print(ser.validated_data)
        # return HttpResponse({'message':'AntiShit'}, status=status.HTTP_200_OK)
    # else:
    #     return HttpResponse({'message':'Shit'}, status=status.HTTP_400_BAD_REQUEST)

# class ArticlesAPIView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer