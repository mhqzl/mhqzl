import pytest
import requests

@pytest.fixture(scope="session")
def api_client():
    """创建API客户端会话"""
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()  