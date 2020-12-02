# coding: utf-8

"""
    URL2io API

    URL2io API 包含 URL2Article 和 URL2NLP 两个服务，实现网页结构智能解析和文本信息智能处理。  当前文档包含所有可用的 API 及使用方法([详细文档](http://url2io.applinzi.com/docs))。  API使用 `token`进行认证，[注册](http://url2io.applinzi.com/accounts/register)后可得。[点此查看token](http://url2io.applinzi.com/console/user/profile)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: url2#sina.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import url2io_client
from url2io_client.models.nlp_keywords_item_for_response import NlpKeywordsItemForResponse  # noqa: E501
from url2io_client.rest import ApiException


class TestNlpKeywordsItemForResponse(unittest.TestCase):
    """NlpKeywordsItemForResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNlpKeywordsItemForResponse(self):
        """Test NlpKeywordsItemForResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = url2io_client.models.nlp_keywords_item_for_response.NlpKeywordsItemForResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
