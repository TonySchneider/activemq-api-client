import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from typing import Optional


class Connector:
    def __init__(self, url: str, username: str, password: str, retries: int = 3, backoff_factor: float = 0.3):
        self._url = url
        self._session = requests.Session()
        self._session.auth = HTTPBasicAuth(username, password)
        self._session.headers.update({"Content-Type": "text/plain"})

        # Configure retries
        retry = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self._session.mount("http://", adapter)
        self._session.mount("https://", adapter)

    def send_request(self, method: str, endpoint: str, data: Optional[str] = None, params: Optional[dict] = None) -> requests.Response:
        url = f"{self._url}{endpoint}"
        response = self._session.request(method, url, data=data, params=params)
        return response

    def close(self):
        self._session.close()
