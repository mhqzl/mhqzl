from config.urls import ApiUrls
from .base_api import BaseApi

class UserApi(BaseApi):
    def login(self, credentials):
        return self.send_request(
            method="POST",
            url=ApiUrls.LOGIN,
            headers={"Content-Type": "application/json"},
            json=credentials
        )

    def get_user_info(self, token):
        return self.send_request(
            method="GET",
            url=ApiUrls.USER_INFO,
            headers={"Authorization": f"Bearer {token}"}
        )