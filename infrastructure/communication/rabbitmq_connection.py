import json
import os

import pika


# context manager class
class RabbitMQConnection:
    def __init__(self):
        self.host = os.getenv("RABBITMQ_HOST", "localhost")
        self.port = int(os.getenv("RABBITMQ_PORT", 5672))
        self.username = os.getenv("RABBITMQ_USERNAME", "guest")
        self.password = os.getenv("RABBITMQ_PASSWORD", "guest")
        self.queue_name = "video_queue"

    def __enter__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                port=self.port,
                credentials=pika.PlainCredentials(username=self.username, password=self.password)
            )
        )
        self.channel = self.connection.channel()
        return self

    def publish(self, payload: bytes):
        self.channel.queue_declare(queue="video_queue", durable=True)
        self.channel.basic_publish(
            exchange="",
            routing_key="video_queue",
            body=json.dumps(payload),
            properties=pika.BasicProperties(delivery_mode=2)  # pika.spec.PERSISTENT_DELIVERY_MODE
        )

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('closing the connection')
        self.connection.close()
