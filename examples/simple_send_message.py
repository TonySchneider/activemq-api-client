from activemq_api_client.client import ActiveMQClient

# create an instance of the ActiveMQClient
client = ActiveMQClient("http://localhost:8161", "admin", "admin")

# send a message to a queue
response = client.send_message("test-queue", "test message")

# print the response status code
print(response)
