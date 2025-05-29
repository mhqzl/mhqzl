import allure
from utils.request_log import get_logged_session


class TestAPIs:

    def test_user_login(self):
        """测试用户登录接口"""
        with allure.step("Step1: 执行用户登录请求"):
            payload = {
                "account": "admin",
                "password": "123456"
            }
            # 注意：此处需根据实际情况调整请求头（若接口需要）
            headers = {
                "Content-Type": "application/json"
            }
            url = "http://dev.dan-social.glor.cn/api/user/login"

            session = get_logged_session()
            response = session.post(
                url=url,
                json=payload,
                headers=headers
            )

            # 断言响应状态码
            assert response.status_code == 200, \
                f"预期状态码 200，实际收到 {response.status_code}"
            response_data = response.json()
            assert response_data.get("success") == True, "登录账号不匹配"

