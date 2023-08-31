import json
import xml.etree.ElementTree as ET
from typing import List, Union

from .connector import Connector


class ActiveMQClient:
    def __init__(self, url: str, username: str, password: str, retries: int = 3, backoff_factor: float = 0.3):
        self._connector = Connector(url, username, password, retries, backoff_factor)

    def get_connection_details(self, client_id: str) -> Union[dict, None]:
        connections = self.get_connections_details()
        for connection in connections:
            if connection['clientId'] == client_id:
                return connection
        return None

    def get_broker_details(self) -> Union[dict, None]:
        endpoint = "/admin/xml/brokers.jsp"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        broker = tree.find('broker')
        if broker:
            details = {
                'name': broker.find('name').text,
            }
            return details
        return None

    def get_queues_details(self) -> List[dict]:
        endpoint = "/admin/xml/queues.jsp"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        queues = []
        for queue in tree.findall('queue'):
            details = {
                'name': queue.find('name').text,
                'consumerCount': int(queue.find('consumerCount').text),
                'enqueueCount': int(queue.find('enqueueCount').text),
                'dequeueCount': int(queue.find('dequeueCount').text),
            }
            queues.append(details)
        return queues

    def get_queue_details(self, queue_name: str) -> Union[dict, None]:
        endpoint = f"/admin/xml/queues.jsp?queueName={queue_name}"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        queue = tree.find('queue')
        if queue:
            details = {
                'name': queue.find('name').text,
                'consumerCount': int(queue.find('consumerCount').text),
                'enqueueCount': int(queue.find('enqueueCount').text),
                'dequeueCount': int(queue.find('dequeueCount').text),
            }
            return details
        return None

    def get_queue_consumer_count(self, queue_name: str) -> Union[int, None]:
        queues = self.get_queues_details()
        for queue in queues:
            if queue['name'] == queue_name:
                return queue['consumerCount']
        return None

    def get_queue_enqueue_count(self, queue_name: str) -> Union[int, None]:
        queues = self.get_queues_details()
        for queue in queues:
            if queue['name'] == queue_name:
                return queue['enqueueCount']
        return None

    def get_queue_dequeue_count(self, queue_name: str) -> Union[int, None]:
        queues = self.get_queues_details()
        for queue in queues:
            if queue['name'] == queue_name:
                return queue['dequeueCount']
        return None

    def get_connections_details(self) -> List[dict]:
        endpoint = "/admin/xml/connections.jsp"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        connections = []
        for connection in tree.findall('connection'):
            details = {
                'clientId': connection.find('clientId').text,
                'remoteAddress': connection.find('remoteAddress').text,
            }
            connections.append(details)
        return connections

    def get_topics_details(self) -> List[dict]:
        endpoint = "/admin/xml/topics.jsp"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        topics = []
        for topic in tree.findall('topic'):
            details = {
                'name': topic.find('name').text,
                'consumerCount': int(topic.find('consumerCount').text),
                'enqueueCount': int(topic.find('enqueueCount').text),
            }
            topics.append(details)
        return topics

    def get_topic_details(self, topic_name: str) -> Union[dict, None]:
        endpoint = f"/admin/xml/topics.jsp?topicName={topic_name}"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        topic = tree.find('topic')
        if topic:
            details = {
                'name': topic.find('name').text,
                'consumerCount': int(topic.find('consumerCount').text),
                'enqueueCount': int(topic.find('enqueueCount').text),
            }
            return details
        return None

    def get_subscribers_details(self) -> List[dict]:
        endpoint = "/admin/xml/subscribers.jsp"
        response = self._connector.send_request("GET", endpoint)
        tree = ET.fromstring(response.content)
        subscribers = []
        for subscriber in tree.findall('subscriber'):
            details = {
                'clientId': subscriber.find('clientId').text,
                'subscriptionName': subscriber.find('subscriptionName').text,
                'destinationName': subscriber.find('destinationName').text,
            }
            subscribers.append(details)
        return subscribers

    def get_subscriber_details(self, client_id: str) -> List[dict]:
        subscribers = self.get_subscribers_details()
        return [subscriber for subscriber in subscribers if subscriber['clientId'] == client_id]

    def close(self):
        self._connector.close()
