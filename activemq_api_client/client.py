import json
import xml.etree.ElementTree as ET
from typing import List, Union

from connector import Connector


class ActiveMQClient:
    def __init__(self, url: str, username: str, password: str, retries: int = 3, backoff_factor: float = 0.3):
        self._connector = Connector(url, username, password, retries, backoff_factor)

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

    def send_message(self, queue_name: str, message: str) -> str:
        endpoint = f"/api/message/{queue_name}?type=queue"
        response = self._connector.send_request("POST", endpoint, data=message)
        return response.text

    def receive_message(self, queue_name: str) -> str:
        endpoint = f"/api/message/{queue_name}?type=queue"
        response = self._connector.send_request("GET", endpoint)
        return response.text

    def acknowledge_message(self, queue_name: str, message_id: str) -> str:
        endpoint = f"/api/message/{queue_name}?type=queue&messageSelector=JMSMessageID='{message_id}'"
        response = self._connector.send_request("GET", endpoint)
        return response.text

    def browse_messages(self, queue_name: str) -> List[dict]:
        endpoint = f"/api/jolokia/exec/org.apache.activemq:type=Broker,brokerName=localhost,destinationType=Queue," \
                   f"destinationName={queue_name}/browse()"

        response = self._connector.send_request("GET", endpoint)
        messages = json.loads(response.text)
        return messages

    def list_queues(self) -> List[str]:
        endpoint = "/api/jolokia/read/org.apache.activemq:type=Broker,brokerName=localhost/Queues"
        response = self._connector.send_request("GET", endpoint)
        queues = json.loads(response.text)["value"]
        return queues

    def list_topics(self) -> List[str]:
        endpoint = "/api/jolokia/read/org.apache.activemq:type=Broker,brokerName=localhost/Topics"
        response = self._connector.send_request("GET", endpoint)
        topics = json.loads(response.text)["value"]
        return topics

    def close(self):
        self._connector.close()
