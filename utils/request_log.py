import allure
import requests
import json

def log_request_response(response, *args, **kwargs):
    """记录请求和响应信息到 Allure 报告"""
    request = response.request
    url = request.url
    headers = dict(request.headers)
    payload = None

    if request.body:
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except ValueError:
            payload = request.body

    allure.attach(str(url), "URL", allure.attachment_type.TEXT)
    allure.attach(str(headers), "Request headers", allure.attachment_type.JSON)
    allure.attach(str(payload), "Request Body", allure.attachment_type.JSON)
    allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
    allure.attach(response.text, "Response Body", allure.attachment_type.JSON)


def get_logged_session():
    """创建一个带有日志记录功能的 requests 会话"""
    session = requests.Session()
    session.hooks['response'].append(log_request_response)
    return session
