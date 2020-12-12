from .models import AstroAutomation
from .serializers import AstroAutomationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ArticleAPIView(APIView):

    def get(self, request):
        articles = AstroAutomation.objects.all()
        serializer = AstroAutomationSerializer(articles, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AstroAutomationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ArticleDetails(APIView):

    def get_object(self, id):
        try:
            return AstroAutomation.objects.get(id = id)
        except AstroAutomation.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        article = self.get_object(id)
        serializer = AstroAutomationSerializer(article)
        return Response(serializer.data)


    def put(self, request, id):
        article = self.get_object(id)
        serializer = AstroAutomationSerializer(article, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)