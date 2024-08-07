# Location Search Query Validator

How To Use:
- Install Python Packages geopy, pika, and random_address
- Change settings in config.py to configure with your AMQP (i.e. ZeroMQ)
  solution. I used RabbitMQ for testing so YMMV
- In the config settings the 'queueToSendTo' is the queue that you will
  send the request to in via a string JSON format {id:<int>,query:<str>}
- In the config settings the 'queueToReceiveFrom' is the queue that will receive
  the query result in via a string JSON format {id:<int>,result:<str>}
- A search result that returns None will indicate that the search query
  was not valid

UML Diagram of Application Flow
![image info](./image.png)
