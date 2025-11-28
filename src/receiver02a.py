import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange='wdprir_fanout', exchange_type='fanout')
queue = channel.queue_declare('', exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange='wdprir_fanout', queue=queue_name)

def callback(channel, method, properties, body):
    print(f"Received '{body.decode()}'")

print(f'Queue name: {queue_name}')

channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
channel.start_consuming()

channel.close()