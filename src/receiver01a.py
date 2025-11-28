import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='wdprir_queue')

def callback(channel, method, properties, body):
    print(f"Received '{body}'")

channel.basic_consume(queue='wdprir_queue',
                      on_message_callback=callback,
                      auto_ack=True)
channel.start_consuming()

channel.close()