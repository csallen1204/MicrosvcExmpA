import pika
import json
from geopy.geocoders import Nominatim
import time
exec(open("config.py").read())

credentials = pika.PlainCredentials(config['messageSystem']['user'],config['messageSystem']['password'])

def sendMessage(messageData):
    
    parameters = pika.ConnectionParameters(host=config["messageSystem"]['host'],\
                    port=config['messageSystem']['port'],credentials=credentials,\
                        virtual_host=config['messageSystem']['virtual_host'])
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=config['messageSystem']['queueToSendTo'])
    channel.basic_publish(exchange=config['messageSystem']['exchange'],routing_key=config['messageSystem']['routingKey'],\
                          body=json.dumps(messageData))
    connection.close()

def main():
    parameters = pika.ConnectionParameters(host=config["messageSystem"]['host'],port=config['messageSystem']['port'],\
                                           credentials=credentials,virtual_host=config['messageSystem']['virtual_host'])
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=config['messageSystem']['queueToReceiveFrom'])
    def callback(ch, method, properties, body):
            data = json.loads(body)
            print(f"Received Search Query #{data['id']}: {config['messageSystem']['virtual_host']}")
            loc = Nominatim(user_agent="searchValidator")
            result = loc.geocode(f"{data['searchQuery']}")
            print(f"Search Result for #{data['id']}: {result}")
            sendMessage({'id':data['id'],'data':str(result)})
            time.sleep(2)
    channel.basic_consume(queue=config['messageSystem']['queueToReceiveFrom'], on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()