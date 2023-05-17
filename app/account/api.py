from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from account.serializer import RegisterSerializer
from account.models import User

class AuthView(ViewSet):
    serializer_class = RegisterSerializer
    
    # la methode post pour recuperer une liste d'elements
    def create(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # la methode get pour recuperer une liste d'elements
    def list(self, request):
        queryset = User.objects.filter(is_active=True, is_superuser=False, is_staff=False)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # la methode get pour recuperer un d'element
    def retrieve(self, request, pk=None):
        queryset = User.objects.get(pk=pk)
        serializer = self.serializer_class(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # la methode put pour modifier un element
    def update(self, request, pk=None):
        pass

    # la methode delete pour creer un element
    def destroy(self, request, pk=None):
        instance = User.objects.filter(pk=pk)
        instance.delete()
        return Response({"detail": "content delete"}, status=status.HTTP_204_NO_CONTENT)