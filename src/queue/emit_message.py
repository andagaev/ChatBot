import pika

from src.queue import queue_config


def send_message_to_queue(message: str):
    connection = queue_config.create_connection()

    channel = queue_config.declare_chanel(connection=connection)
    print(f"Sending message: {message}")

    channel.basic_publish(
        exchange="",
        routing_key=queue_config.QUEUE,
        body=message,
        properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
    )
    print(f"Message {message} sent to queue!")

    connection.close()
