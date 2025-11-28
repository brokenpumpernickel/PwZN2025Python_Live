import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.basic_qos(prefetch_count=1)

channel.queue_declare(queue='wdprir_queue_durable', durable=True)

def callback(channel, method, properties, body):
    print(f"Received '{body}'")
    time.sleep(0.5)
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='wdprir_queue_durable',
                      on_message_callback=callback,
                      auto_ack=False)
channel.start_consuming()

channel.close()