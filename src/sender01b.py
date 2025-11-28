import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.queue_declare(queue='wdprir_queue_durable', durable=True)

index = 0
while True:
    message = f'Hello World! {index}'
    channel.basic_publish(exchange='',
                          routing_key='wdprir_queue_durable',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # Make message persistent
                          ))
    print(f"Sent '{message}'")
    index += 1
    time.sleep(1)

channel.close()