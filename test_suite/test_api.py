import requests

class TestAPIs:
    base_url = "c"

    def test_get_posts(self):
        """测试获取所有文章列表"""
        response = requests.get(f"{self.base_url}/posts")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_create_post(self):
        """测试创建新文章"""
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.base_url}/posts", json=payload)
        assert response.status_code == 201
        assert response.json()["title"] == "foo"

    def test_update_post(self):
        """测试更新文章"""
        payload = {"title": "updated title"}
        response = requests.patch(f"{self.base_url}/posts/1", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == "updated title"

    def test_delete_post(self):
        """测试删除文章"""
        response = requests.delete(f"{self.base_url}/posts/1")
        assert response.status_code == 200