# ActiveMQ API Client

A Python client for interacting with the ActiveMQ REST API.

## Installation

Install the package via pip:

```
pip install activemq-api-client
```

## Usage

After installing the package, you can use it to interact with the ActiveMQ REST API.

### Example

```python
from activemq_api_client.client import ActiveMQClient

# Create an instance of the ActiveMQClient
client = ActiveMQClient("http://localhost:8161", "admin", "admin")

# Send a message to a queue
response = client.send_message("test-queue", "test message")

# Print the response status code
print(response)
```

In this example, we create an instance of the `ActiveMQClient` class and then use the `send_message` method to send a message to the "test-queue" queue. The `send_message` method returns the HTTP response text, which is then printed to the console.

### Methods

#### `send_message(queue_name: str, message: str) -> str`

Sends a message to the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.
- `message` (str): The message content.

Returns:

- `str`: The HTTP response text.

#### `receive_message(queue_name: str) -> str`

Receives a message from the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.

Returns:

- `str`: The HTTP response text.

#### `acknowledge_message(queue_name: str, message_id: str) -> str`

Acknowledges a message on the specified queue using the message ID.

Parameters:

- `queue_name` (str): The name of the queue.
- `message_id` (str): The ID of the message to acknowledge.

Returns:

- `str`: The HTTP response text.

#### `browse_messages(queue_name: str) -> List[dict]`

Browses messages on the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.

Returns:

- `List[dict]`: A list of messages on the queue.

#### `list_queues() -> List[str]`

Lists all queues available in the ActiveMQ broker.

Returns:

- `List[str]`: A list of queue names.

#### `list_topics() -> List[str]`

Lists all topics available in the ActiveMQ broker.

Returns:

- `List[str]`: A list of topic names.

#### `get_queues_details() -> List[dict]`

Retrieves details of all available queues in the ActiveMQ broker.

Returns:

- `List[dict]`: A list of dictionaries containing details of each queue.

#### `get_queue_consumer_count(queue_name: str) -> Union[int, None]`

Gets the consumer count for the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.

Returns:

- `int, None`: The consumer count for the specified queue or `None` if the queue does not exist.

#### `get_queue_enqueue_count(queue_name: str) -> Union[int, None]`

Gets the enqueue count for the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.

Returns:

- `int, None`: The enqueue count for the specified queue or `None` if the queue does not exist.

#### `get_queue_dequeue_count(queue_name: str) -> Union[int, None]`

Gets the dequeue count for the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.

Returns:

- `int, None`: The dequeue count for the specified queue or `None` if the queue does not exist.

#### `get_connections_details() -> List[dict]`

Retrieves details of all connections in the ActiveMQ broker.

Returns:

- `List[dict]`: A list of dictionaries containing details of each connection.

#### `get_topics_details() -> List[dict]`

Retrieves details of all available topics in the ActiveMQ broker.

Returns:

- `List[dict]`: A list of dictionaries containing details of each topic.

#### `get_subscribers_details() -> List[dict]`

Retrieves details of all subscribers in the ActiveMQ broker.

Returns:

- `List[dict]`: A list of dictionaries containing details of each subscriber.

#### `close()`

Closes the connection to the ActiveMQ broker.

## License

This package is released under the MIT License. See the `LICENSE` file for more details.
