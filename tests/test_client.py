import pytest
from activemq_api_client.client import ActiveMQClient


@pytest.fixture
def client():
    return ActiveMQClient('your_activemq_url', 'your_username', 'your_password')


def test_get_queues_details(client):
    queues = client.get_queues_details()
    assert isinstance(queues, list)
    for queue in queues:
        assert 'name' in queue
        assert 'consumerCount' in queue
        assert 'enqueueCount' in queue
        assert 'dequeueCount' in queue


def test_get_queue_consumer_count(client):
    consumer_count = client.get_queue_consumer_count('your_queue_name')
    assert isinstance(consumer_count, int)


def test_get_queue_enqueue_count(client):
    enqueue_count = client.get_queue_enqueue_count('your_queue_name')
    assert isinstance(enqueue_count, int)


def test_get_queue_dequeue_count(client):
    dequeue_count = client.get_queue_dequeue_count('your_queue_name')
    assert isinstance(dequeue_count, int)


def test_get_connections_details(client):
    connections = client.get_connections_details()
    assert isinstance(connections, list)
    for connection in connections:
        assert 'clientId' in connection
        assert 'remoteAddress' in connection


def test_get_topics_details(client):
    topics = client.get_topics_details()
    assert isinstance(topics, list)
    for topic in topics:
        assert 'name' in topic
        assert 'consumerCount' in topic
        assert 'enqueueCount' in topic


def test_get_subscribers_details(client):
    subscribers = client.get_subscribers_details()
    assert isinstance(subscribers, list)
    for subscriber in subscribers:
        assert 'clientId' in subscriber
        assert 'subscriptionName' in subscriber
        assert 'destinationName' in subscriber


def test_send_message(client):
    response = client.send_message('your_queue_name', 'your_message')
    assert response == 'your_expected_response'


def test_receive_message(client):
    message = client.receive_message('your_queue_name')
    assert isinstance(message, str)


def test_acknowledge_message(client):
    response = client.acknowledge_message('your_queue_name', 'your_message_id')
    assert response == 'your_expected_response'


def test_browse_messages(client):
    messages = client.browse_messages('your_queue_name')
    assert isinstance(messages, list)


def test_list_queues(client):
    queues = client.list_queues()
    assert isinstance(queues, list)


def test_list_topics(client):
    topics = client.list_topics()
    assert isinstance(topics, list)


def test_close(client):
    client.close()
    # assert that the connection is closed

