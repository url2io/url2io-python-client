# coding: utf-8

"""
    URL2io API

    URL2io API 包含 URL2Article 和 URL2NLP 两个服务，实现网页结构智能解析和文本信息智能处理。  当前文档包含所有可用的 API 及使用方法([详细文档](http://url2io.applinzi.com/docs))。  API使用 `token`进行认证，[注册](http://url2io.applinzi.com/accounts/register)后可得。[点此查看token](http://url2io.applinzi.com/console/user/profile)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: url2#sina.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "url2io-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
    

setup(
    name=NAME,
    version=VERSION,
    description="URL2io API",
    author_email="url2#sina.com",
    url="https://github.com/url2io/url2io-python-client",
    keywords=["Swagger", "URL2io API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    URL2io API 包含 URL2Article 和 URL2NLP 两个服务，实现网页结构智能解析和文本信息智能处理。  当前文档包含所有可用的 API 及使用方法([详细文档](http://url2io.applinzi.com/docs))。  API使用 &#x60;token&#x60;进行认证，[注册](http://url2io.applinzi.com/accounts/register)后可得。[点此查看token](http://url2io.applinzi.com/console/user/profile)  # noqa: E501
    """
)
