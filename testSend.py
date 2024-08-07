import pika
from random_address import real_random_address
import random
import json
import time
exec(open("config.py").read())

# Followed documentation and starter code from RabbitMQ Python Tutorial:
# https://www.rabbitmq.com/tutorials/tutorial-one-python
for i in range(0,20,1):
    address = real_random_address()
    body = address['address1'] + ' ' + address['city'] + ' ' + address['state'] + ' ' + address['postalCode'] 
    messageID = random.randrange(99999999999)
    credentials = pika.PlainCredentials(config['messageSystem']['user'],config['messageSystem']['password'])
    parameters = pika.ConnectionParameters(host=config['messageSystem']['host'],port=config['messageSystem']['port'],\
                                           credentials=credentials,virtual_host=config['messageSystem']['virtual_host'])
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=config['messageSystem']['queueToSendTo'])
    channel.basic_publish(exchange='',
                        routing_key=config['messageSystem']['queueToSendTo'],
                        body=json.dumps({'id':messageID,'searchQuery':body}))
    time.sleep(2)
    print(f"Sending Search #{messageID}: {body}" )
    connection.close()
