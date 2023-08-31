import requests


class ActiveMQClient:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    def send_message(self, queue_name, message):
        url = f"{self.url}/api/message/{queue_name}?type=queue"
        headers = {"Content-Type": "text/plain"}
        response = requests.post(url, data=message, headers=headers, auth=(self.username, self.password))
        return response.status_code
