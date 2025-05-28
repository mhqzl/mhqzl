import requests

class BaseApi:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, headers=None, data=None, json=None):
        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                data=data,
                json=json
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None