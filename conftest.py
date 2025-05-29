import allure
import pytest
import sys
import os

# 添加项目根目录到Python路径，确保所有测试文件都能导入项目模块
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)


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