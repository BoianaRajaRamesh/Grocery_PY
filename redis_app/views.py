from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import redis
import json
from .models import Message
from .serializers import MessageSerializer

redis_client = redis.Redis(host='localhost', port=6379, db=0)


class MessageAPIView(APIView):
    def post(self, request):
        content = request.data.get('content')
        if not content:
            return Response({'error': 'Content is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new Message instance (but don't save to DB yet)
        # message = Message(content=content)

        # Publish the message to Redis
        message_data = {
            'content': content
        }
        red = redis_client.publish('message_channel', json.dumps(message_data))

        # Return the message ID
        return Response({'id': red}, status=status.HTTP_201_CREATED)