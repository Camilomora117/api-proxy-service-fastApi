import requests
from requests.exceptions import RequestException
from app.utils.logger import get_logger

logger = get_logger("HttpRequest")

class HttpRequest:
    """
    Class to handle http methods
    """

    def _make_request(self, method: str, endpoint: str, **kwargs):
        try:
            response = requests.request(method, endpoint, **kwargs)
            response.raise_for_status()
            return response.json()
        except RequestException as error:
            self._handle_error(error)

    def get(self, endpoint: str, headers: dict = None, params: dict = None):
        return self._make_request("GET", endpoint, headers=headers, params=params)

    def post(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        return self._make_request("POST", endpoint, headers=headers, data=data, json=json)

    def put(self, endpoint: str, data: dict = None, json: dict = None, headers: dict = None):
        return self._make_request("PUT", endpoint, headers=headers, data=data, json=json)

    def delete(self, endpoint: str, headers: dict = None):
        return self._make_request("DELETE", endpoint, headers=headers)

    def _handle_error(self, error: RequestException):
        """ Manejo centralizado de errores """
        logger(f"HTTP Request Error: {error}")
        raise Exception(f"Request failed: {error}")
