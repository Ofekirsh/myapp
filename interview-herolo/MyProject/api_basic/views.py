from django.shortcuts import render
from django.http import HttpResponse
from .models import Messages
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins


# from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Messages.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class ArticleAPIView(APIView):

    def get(self, request):
        articles = Messages.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return Messages.objects.get(id=id)

        except Messages.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        change_read = Messages.objects.get(id=id)
        change_read.read = True
        change_read.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetSpecificAuthor(APIView):
    def get(self, request, sender):
        articles = Messages.objects.filter(sender=sender)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class GetSpecificAuthorUnread(APIView):
    def get(self, request, sender, read):
        articles = Messages.objects.filter(sender=sender).filter(read=read)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class GetSpecificAuthorUnread(APIView):
    def get(self, request, sender, read):
        articles = Messages.objects.filter(sender=sender).filter(read=read)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)