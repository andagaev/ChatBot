import pika

QUEUE = "message_queue"


def create_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))

    return connection


def declare_chanel(connection):
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE, durable=True)

    return channel
