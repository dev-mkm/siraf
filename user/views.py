from file.models import file
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, authentication, status

from user.models import Favorites

class FileViewSet(viewsets.ViewSet):
    
    authentication_classes = [authentication.TokenAuthentication]

    @action(detail=True)
    def files(self, request):
        if (request.user.status == True):
            files = file.objects.get(owner=request.user).all().values()
            return Response(files)
        else:
            content = {'message': 'Your Account is disabled'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True)
    def favorites(self, request):
        if (request.user.status == True):
            files = Favorites.objects.get(status=True, user=request.user).all().values()
            return Response(files)
        else:
            content = {'message': 'Your Account is disabled'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #@action()
    #def ConsultantRequst(self, request):
    #   return Response()