from chat.models import Chat
from file.models import file
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, authentication, status
from django.shortcuts import get_object_or_404

from message.models import Message

class ChatViewSet(viewsets.ViewSet):
    
    authentication_classes = [authentication.TokenAuthentication]

    @action(detail=False, methods=['post'])
    def messageAdd(self, request, id=None):
        if (id == None):
            content = {'message': 'Fileid cannot be empty'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        files = file.objects.all()
        File = get_object_or_404(files, id=id)
        chat = Chat.objects.filter(file_id=id)
        if (request.user.status == True and not chat and File.status == True):
            newchat = Chat(receiver_id=File.owner.id, sender_id=request.user.id, status='A', file_id=File.id, Creator_id=request.user.id)
            newchat.save()
            return Response(status=status.HTTP_200_OK)
        else:
            content = {'message': 'Chat Exists'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)