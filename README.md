# ActiveMQ API Client

An auxiliary Python client for the ActiveMQ REST API, designed to facilitate administrative and monitoring tasks, rather than replacing the native messaging protocols (STOMP, MQTT) for sending and receiving messages.

## Overview

ActiveMQ is a powerful open-source message broker that supports various messaging protocols like AMQP, MQTT, OpenWire, and WebSocket. While these protocols are recommended for regular message processing due to their efficiency, reliability, and feature set, there are certain administrative and monitoring tasks that can be efficiently handled using the ActiveMQ REST API. This Python client acts as a wrapper around the ActiveMQ REST API, providing developers and system administrators with a simple and convenient way to manage and monitor their ActiveMQ broker, queues, topics, and connections.

## Features

This package is designed to assist with the following administrative and monitoring tasks:

1. **Broker Status**: Check if the broker is running, its uptime, etc.
2. **Queue and Topic Monitoring**: Monitor the number of messages enqueued, dequeued, and the number of consumers connected.
3. **Connection Management**: Monitor the clients connected, their IP addresses, etc.
4. **Subscription Management**: Monitor the clients subscribed to various topics.

## Important Note

This package is not intended to replace the native messaging protocols (STOMP, MQTT, etc.) supported by ActiveMQ for sending and receiving messages. The REST API, and by extension this package, may not provide the same level of performance, scalability, reliability, and real-time updates as the native protocols. Therefore, it is recommended to use this package only for administrative and monitoring purposes, and to use the native messaging protocols for regular message processing in your application.

## Installation

Install the package via pip:

```
pip install activemq-api-client
```

## Usage

After installing the package, you can use it to interact with the ActiveMQ REST API.

```python
from activemq_api_client.client import ActiveMQClient

# Create an ActiveMQClient instance
client = ActiveMQClient('http://localhost:8161', 'admin', 'admin')

# Get details about all queues
queues = client.get_queues_details()
print(queues)

# Get the number of consumers connected to a specific queue
consumer_count = client.get_queue_consumer_count('exampleQueue')
print(consumer_count)

# Close the connection to the broker
client.close()
```

## Methods

The `ActiveMQClient` class provides the following methods to interact with the ActiveMQ REST API:

- `get_queues_details() -> List[dict]`

  Returns a list of dictionaries containing details about all the queues. Each dictionary contains the following keys:
    - `name`: The name of the queue.
    - `consumerCount`: The number of consumers connected to the queue.
    - `enqueueCount`: The number of messages enqueued in the queue.
    - `dequeueCount`: The number of messages dequeued from the queue.

- `get_queue_consumer_count(queue_name: str) -> Union[int, None]`

  Returns the number of consumers connected to the specified queue, or `None` if the queue does not exist.

- `get_queue_enqueue_count(queue_name: str) -> Union[int, None]`

  Returns the number of messages enqueued in the specified queue, or `None` if the queue does not exist.

- `get_queue_dequeue_count(queue_name: str) -> Union[int, None]`

  Returns the number of messages dequeued from the specified queue, or `None` if the queue does not exist.

- `get_connections_details() -> List[dict]`

  Returns a list of dictionaries containing details about all the connections. Each dictionary contains the following keys:
    - `clientId`: The client ID of the connection.
    - `remoteAddress`: The remote address of the connection.

- `get_topics_details() -> List[dict]`

  Returns a list of dictionaries containing details about all the topics. Each dictionary contains the following keys:
    - `name`: The name of the topic.
    - `consumerCount`: The number of consumers connected to the topic.
    - `enqueueCount`: The number of messages enqueued in the topic.

- `get_subscribers_details() -> List[dict]`

  Returns a list of dictionaries containing details about all the subscribers. Each dictionary contains the following keys:
    - `clientId`: The client ID of the subscriber.
    - `subscriptionName`: The subscription name of the subscriber.
    - `destinationName`: The destination name of the subscriber.

- `close()`

  Closes the connection to the ActiveMQ broker.

All methods except `close` send a GET request to the ActiveMQ REST API and return the response in the specified format. The `close` method does not send any request and simply closes the connection to the broker.


Closes the connection to the ActiveMQ broker.

## License

This package is released under the MIT License. See the `LICENSE` file for more details.
