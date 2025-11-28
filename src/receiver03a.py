import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange='wdprir_direct',
                         exchange_type='direct')

queue = channel.queue_declare('', exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange='wdprir_direct',
                   queue=queue_name,
                   routing_key='error')

def callback(channel, method, properties, body):
    print(f"Received '{body.decode()}'")

print(f'Queue name: {queue_name}')

channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
channel.start_consuming()

channel.close()