from chat.models import Chat
from file.models import file
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, authentication, status
from django.shortcuts import get_object_or_404

from message.models import Message

class ChatViewSet(viewsets.ViewSet):
    
    authentication_classes = [authentication.TokenAuthentication]

    @action(detail=False, methods=['delete'])
    def chatDelete(self, request):
        if (request.user.status == True):
            #request.DELETE
            files = file.objects.get(owner=request.user).all().values()
            return Response(files)
        else:
            content = {'message': 'Your Account is disabled'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(detail=False, methods=['post'])
    def messageAdd(self, request, chat_id=None):
        if (chat_id == None):
            content = {'message': 'ChatID cannot be empty', 'status': 400}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        chats = Chat.objects.all()
        chat = get_object_or_404(chats, id=chat_id)
        if (request.user.status == True and chat.status == 'A'):
            if (chat.receiver_id != request.user.id and chat.sender_id != request.user.id):
                content = {'message': 'Your not in this chat', 'status': 405}
                return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                message = Message(message=request.POST['message'], chat=chat, status=False, Creator_id=request.user)
                message.save()
                content = {'status': 200}
                return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'This Chat is Disabled', 'status': 405}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    @action(detail=False, methods=['delete'])
    def message(self, request, chat_id=None, id=None):
        if (chat_id == None or id == None):
            content = {'message': 'ChatID and ID cannot be empty', 'status': 400}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        chats = Message.objects.all()
        chat = get_object_or_404(chats, chat_id=chat_id, id=id)
        if (request.user.status == True and chat.status == 'A'):
            if (chat.receiver_id != request.user.id and chat.sender_id != request.user.id):
                content = {'message': 'Your not in this chat', 'status': 405}
                return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
            else:
                messages = Message.objects.all()
                message = get_object_or_404(messages, chat_id=chat_id, id=id)
                message.delete()
                content = {'status': 200}
                return Response(content, status=status.HTTP_200_OK)
        else:
            content = {'message': 'This Chat is Disabled', 'status': 405}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)
  
