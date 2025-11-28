import pika
import time

credentials = pika.PlainCredentials('', '')
connection_params = pika.ConnectionParameters('',
                                              virtual_host='wdprir',
                                              credentials=credentials)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

channel.exchange_declare(exchange='wdprir_fanout', exchange_type='fanout')


index = 0
while True:
    message = f'Hello World! {index}'
    channel.basic_publish(exchange='wdprir_fanout',
                          routing_key='',
                          body=message)
    print(f"Sent '{message}'")
    index += 1
    time.sleep(1)

channel.close()