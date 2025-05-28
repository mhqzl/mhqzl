import allure
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and hasattr(item, 'callspec'):
        with allure.step("接口详情"):
            allure.attach(
                name="请求参数",
                body=str(item.callspec.params),
                attachment_type=allure.attachment_type.JSON
            )