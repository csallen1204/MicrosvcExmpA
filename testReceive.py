import pika
import time
exec(open("config.py").read())

# Followed documentation and starter code from RabbitMQ Python Tutorial:
# https://www.rabbitmq.com/tutorials/tutorial-one-python
credentials = pika.PlainCredentials(config['messageSystem']['user'],config['messageSystem']['password'])
parameters = pika.ConnectionParameters(host=config['messageSystem']['host'],port=config['messageSystem']['port'],\
                                       credentials=credentials,virtual_host=config['messageSystem']['virtual_host'])
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=config['messageSystem']['queueToReceiveFrom'])
def callback(ch, method, properties, body):
        print(body)
        time.sleep(2)
channel.basic_consume(queue=config['messageSystem']['queueToReceiveFrom'], on_message_callback=callback, auto_ack=True)
channel.start_consuming()
