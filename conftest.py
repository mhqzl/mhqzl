import pytest
from api.user_api import UserApi
from req_data.test_data import TestData


@pytest.fixture(scope="session")
def auth_token():
    user_api = UserApi()
    response = user_api.login(TestData.LOGIN_SUCCESS)
    if response and response.status_code == 200:
        return response.json().get("token")
    pytest.fail("登录失败，无法获取token")
