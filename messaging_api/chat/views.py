from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Message
from .serializers import MessageSerializer

class MessagePagination(PageNumberPagination):
    page_size = 10

class RetrieveMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, conversation_id):
        messages = Message.objects.filter(
            models.Q(receiver_user=request.user) | models.Q(receiver_group__members=request.user),
            receiver_user_id=conversation_id
        ).order_by("-timestamp")
        paginator = MessagePagination()
        paginated_messages = paginator.paginate_queryset(messages, request)
        serializer = MessageSerializer(paginated_messages, many=True)
        return paginator.get_paginated_response(serializer.data)