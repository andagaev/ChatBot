from src import discrd, tg
from src.queue import queue_config


def start_worker():
    connection = queue_config.create_connection()
    channel = queue_config.declare_chanel(connection=connection)
    print("Worker started, waiting for messages...")

    def callback(ch, method, properties, body):
        message = body.decode()
        tag = message.split(" ")[0]

        if tag == "telegram":
            tg.send_message_to_Telegram(message_to_send=message)
        elif tag == "discord":
            discrd.send_message_to_Discord(message_to_send=message)
        else:
            tg.send_message_to_Telegram(message_to_send=message)
            discrd.send_message_to_Discord(message_to_send=message)

        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=queue_config.QUEUE, on_message_callback=callback)

    channel.start_consuming()
