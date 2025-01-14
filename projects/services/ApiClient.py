from typing import Dict, Optional

import requests
from requests import Response
from enum import Enum
from projects.services.Service import Service

class ApiClient(Service):
    _headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1, WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.2840.99 Safari/537.36'}
    _timeout = 3 * 60   #Number of seconds for the HTTP request to die
    _retry = 3
    class HTTP(Enum):
        GET = 'GET'
        POST = 'POST'
        PUSH = 'DELETE'

    def __init__(self):
        super().__init__()

    def get(self, url=str, data: Dict = None, headers: Dict = None, retry: int = 3, auth = None)->Optional[Response]:
        return self.send_request(url, self.HTTP.GET, data, None, headers, retry, auth)

    def post(self, url=str, data: Dict = None, json: Dict = None, headers: Dict = None, retry: int = 3, auth = None)->Optional[Response]:
        return self.send_request(url, self.HTTP.POST, data, None, headers, retry, auth)

    def delete(self, url=str, data: Dict = None, json: Dict = None, headers: Dict = None, retry: int = 3, auth = None)->Optional[Response]:
        return self.send_request(url, self.HTTP.DELETE, data, None, headers, retry, auth)



    def send_request(self, url: str, http_method : HTTP = HTTP.GET, data: Dict = None, json: Dict = None, headers: Dict = None, retry: int = 3, auth = None)-> Optional[Response]:
        response = None
        try:
            if retry<0:
                return None

            if headers:
                self._headers.update(headers)
            if http_method == self.HTTP.GET:
                response = requests.get(url, params=data, headers=self._headers, timeout=self._timeout, auth=auth)
            elif http_method==self.HTTP.POST:
                response = requests.post(url, data=data, json=json, headers=self._headers, timeout=self._timeout, auth=auth)
            elif http_method == self.HTTP.DELETE:
                response = requests.delete(url, data=data, json=json, headers=self._headers, timeout=self._timeout, auth=auth)
            return response
        except Exception as error:
            return self.send_request(url, data=data, json=json, http_method=http_method,headers=headers, retry=retry - 1, auth=auth)
