import requests
import pytest


class TestAPIs:
    base_url = "https://jsonplaceholder.typicode.com"
    created_post_id = None

    def test_create_post(self):
        """测试创建新文章"""
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        response = requests.post(f"{self.base_url}/posts", json=payload)

        # 断言响应状态码
        assert response.status_code == 201, f"预期状态码 201，实际收到 {response.status_code}"

        # 保存创建的文章 ID 用于后续测试
        response_data = response.json()
        self.__class__.created_post_id = response_data.get("id")

        # 断言响应数据
        assert response_data["title"] == "foo", "创建的文章标题不匹配"
        assert response_data["body"] == "bar", "创建的文章内容不匹配"
        assert response_data["userId"] == 1, "创建的文章用户 ID 不匹配"

    @pytest.mark.dependency(depends=["TestAPIs::test_create_post"])
    def test_update_post(self):
        """测试更新文章"""
        if not self.created_post_id:
            pytest.skip("没有可更新的文章")

        payload = {"title": "updated title"}
        response = requests.patch(f"{self.base_url}/posts/{self.created_post_id}", json=payload)

        # 断言响应状态码
        assert response.status_code == 200, f"预期状态码 200，实际收到 {response.status_code}"

        # 断言响应数据
        response_data = response.json()
        assert response_data["title"] == "updated title", "更新后的文章标题不匹配"

    # @pytest.mark.dependency(depends=["TestAPIs::test_create_post"])
    # def test_delete_post(self):
    #     """测试删除文章"""
    #     if not self.created_post_id:
    #         pytest.skip("没有可删除的文章")
    #
    #     response = requests.delete(f"{self.base_url}/posts/{self.created_post_id}")
    #
    #     # 断言响应状态码
    #     assert response.status_code == 200, f"预期状态码 200，实际收到 {response.status_code}"
    #
    #     # 验证文章已被删除
    #     verify_response = requests.get(f"{self.base_url}/posts/{self.created_post_id}")
    #     assert verify_response.status_code == 404, "文章未被成功删除"

    def test_get_posts(self):
        """测试获取所有文章列表"""
        response = requests.get(f"{self.base_url}/posts")

        # 断言响应状态码
        assert response.status_code == 200, f"预期状态码 200，实际收到 {response.status_code}"

        # 断言响应数据
        posts = response.json()
        assert isinstance(posts, list), "获取的文章列表不是列表类型"
        assert len(posts) > 0, "文章列表为空"