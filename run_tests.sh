#!/bin/bash

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 执行测试（同时生成Allure和HTML报告）
pytest -m "api" --alluredir=./allure-results --html=./report.html

# 生成Allure报告
if [ -x "$(command -v allure)" ]; then
    allure generate allure-results -o allure-report --clean
    echo "Allure报告已生成，请使用以下命令查看："
    echo "allure open allure-report"
else
    echo "未找到Allure命令行工具，请手动生成报告"
fi

echo "HTML报告已生成：report.html"