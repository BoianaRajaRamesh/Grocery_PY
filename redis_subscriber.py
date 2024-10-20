import redis
import json
import django
import os
from django.conf import settings

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from redis_app.models import Message

redis_client = redis.Redis(host='localhost', port=6379, db=0)


def message_handler(message):
    data = json.loads(message['data'].decode('utf-8'))
    print(f"Received message: {data}")

    # Save the message to the database
    msg = Message.objects.create(content=data['content'])
    print(f"Saved message with ID: {msg.id}")


pubsub = redis_client.pubsub()
pubsub.subscribe(**{'message_channel': message_handler})

print("Listening for messages...")
for message in pubsub.listen():
    if message['type'] == 'message':
        message_handler(message)