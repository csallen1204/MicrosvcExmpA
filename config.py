config = {
    "messageSystem": {
        "host": "192.168.0.27",
        "port": 5672,
        "user": "test",
        "password": "test",
        "virtual_host": "test",
        "exchange": "",
        "routingKey": "outbox",
        "queueToSendTo": "outbox",
        "queueToGetFrom": "inbox"
    }
}