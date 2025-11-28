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

kyes = ['info', 'warning', 'error']

index = 0
while True:
    message = f'Hello World! {index} {kyes[index % len(kyes)]}'
    channel.basic_publish(exchange='wdprir_direct',
                          routing_key=kyes[index % len(kyes)],
                          body=message)
    print(f"Sent '{message}'")
    index += 1
    time.sleep(1)

channel.close()