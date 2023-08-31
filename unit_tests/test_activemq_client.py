import unittest
from unittest.mock import Mock
from activemq_api_client.client import ActiveMQClient


class TestActiveMQClient(unittest.TestCase):

    def setUp(self):
        self.connector = Mock()
        self.client = ActiveMQClient('http://localhost:8161', 'admin', 'admin')
        self.client._connector = self.connector

    def test_get_broker_details(self):
        self.connector.send_request.return_value.content = b'<broker><name>brokerName</name></broker>'
        result = self.client.get_broker_details()
        self.assertEqual(result, {'name': 'brokerName'})

    def test_get_queues_details(self):
        self.connector.send_request.return_value.content = b'<queues><queue><name>queue1</name><consumerCount>1</consumerCount><enqueueCount>10</enqueueCount><dequeueCount>5</dequeueCount></queue></queues>'
        result = self.client.get_queues_details()
        self.assertEqual(result, [{'name': 'queue1', 'consumerCount': 1, 'enqueueCount': 10, 'dequeueCount': 5}])

    def test_get_queue_details(self):
        self.connector.send_request.return_value.content = b'<queue><name>queue1</name><consumerCount>1</consumerCount><enqueueCount>10</enqueueCount><dequeueCount>5</dequeueCount></queue>'
        result = self.client.get_queue_details('queue1')
        self.assertEqual(result, {'name': 'queue1', 'consumerCount': 1, 'enqueueCount': 10, 'dequeueCount': 5})

    def test_get_connections_details(self):
        self.connector.send_request.return_value.content = b'<connections><connection><clientId>clientId1</clientId><remoteAddress>remoteAddress1</remoteAddress></connection></connections>'
        result = self.client.get_connections_details()
        self.assertEqual(result, [{'clientId': 'clientId1', 'remoteAddress': 'remoteAddress1'}])

    def test_get_topics_details(self):
        self.connector.send_request.return_value.content = b'<topics><topic><name>topic1</name><consumerCount>1</consumerCount><enqueueCount>10</enqueueCount></topic></topics>'
        result = self.client.get_topics_details()
        self.assertEqual(result, [{'name': 'topic1', 'consumerCount': 1, 'enqueueCount': 10}])

    def test_get_topic_details(self):
        self.connector.send_request.return_value.content = b'<topic><name>topic1</name><consumerCount>1</consumerCount><enqueueCount>10</enqueueCount></topic>'
        result = self.client.get_topic_details('topic1')
        self.assertEqual(result, {'name': 'topic1', 'consumerCount': 1, 'enqueueCount': 10})

    def test_get_subscribers_details(self):
        self.connector.send_request.return_value.content = b'<subscribers><subscriber><clientId>clientId1</clientId><subscriptionName>subscriptionName1</subscriptionName><destinationName>destinationName1</destinationName></subscriber></subscribers>'
        result = self.client.get_subscribers_details()
        self.assertEqual(result, [{'clientId': 'clientId1', 'subscriptionName': 'subscriptionName1', 'destinationName': 'destinationName1'}])

    def test_get_connection_details(self):
        self.client.get_connections_details = Mock(return_value=[{'clientId': 'clientId1', 'remoteAddress': 'remoteAddress1'}, {'clientId': 'clientId2', 'remoteAddress': 'remoteAddress2'}])
        result = self.client.get_connection_details('clientId1')
        self.assertEqual(result, {'clientId': 'clientId1', 'remoteAddress': 'remoteAddress1'})

    def test_get_subscriber_details(self):
        self.client.get_subscribers_details = Mock(return_value=[{'clientId': 'clientId1', 'subscriptionName': 'subscriptionName1', 'destinationName': 'destinationName1'}, {'clientId': 'clientId2', 'subscriptionName': 'subscriptionName2', 'destinationName': 'destinationName2'}])
        result = self.client.get_subscriber_details('clientId1')
        self.assertEqual(result, [{'clientId': 'clientId1', 'subscriptionName': 'subscriptionName1', 'destinationName': 'destinationName1'}])

    def test_close(self):
        self.client.close()
        self.connector.close.assert_called()


if __name__ == '__main__':
    unittest.main()
