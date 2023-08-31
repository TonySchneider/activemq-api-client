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

In this example, we create an instance of the `ActiveMQClient` class and then use the `send_message` method to send a message to the "test-queue" queue. The `send_message` method returns the HTTP response status code, which is then printed to the console.

### Methods

#### `send_message(queue_name, message)`

Sends a message to the specified queue.

Parameters:

- `queue_name` (str): The name of the queue.
- `message` (str): The message content.

Returns:

- `int`: The HTTP response status code.

## License

This package is released under the MIT License. See the `LICENSE` file for more details.
