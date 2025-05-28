import pytest
from api.user_api import UserApi

@pytest.mark.api
class TestUser:
    def test_login_success(self):
        user_api = UserApi()
        response = user_api.login({
            "account": "admin",
            "password": "123456"
        })
        assert response.status_code == 200
        assert "token" in response.json()

    @pytest.mark.usefixtures("auth_token")
    def test_get_user_info(self, auth_token):
        user_api = UserApi()
        response = user_api.get_user_info(auth_token)
        assert response.status_code == 200
        assert "username" in response.json()