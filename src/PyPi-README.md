# url2io-client

URL2io API SDK包含 URL2Article 和 URL2NLP 两个服务，实现网页结构智能解析和文本信息智能处理。
SDK 使用文档，见 https://github.com/url2io/url2io-python-client 。
SDK 涉及的 Rest API，见 http://url2io.applinzi.com/docs

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install url2io-client
```

or

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/url2io/url2io-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/url2io/url2io-python-client.git`)

Then import the package:
```python
import url2io_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import url2io_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import url2io_client
from url2io_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token_in_query
configuration = url2io_client.Configuration()
configuration.host = 'YOUR_API_SERVICE_URL' # 你申请的服务地址，默认为体验版地址：http://url2api.applinzi.com
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = url2io_client.URL2ArticleApi(url2io_client.ApiClient(configuration))
url = 'url_example' # str | 要提取正文网页的网址，参考 [URL Encoding](http://www.w3schools.com/tags/ref_urlencode.asp)
fields = ['fields_example'] # list[str] | 指示需要额外返回的额外字段，取值为：  - `next`: 表示要提取下一页链接。   - `text`: 表示要返回正文的纯文字格式。   - `markdown`: 表示返回正文的markdown格式。   构造url时多个值通过','号隔开，如`?fields=text,next`。调用sdk时使用列表即可，如fields= ['text', 'markdown']。 (optional)
param_callback = 'param_callback_example' # str | 使用jsonp实现Ajax跨域请求时需要传此参数 (optional)

try:
    # 网页结构智能解析 HTTP Get 接口
    api_response = api_instance.get_article(url, fields=fields, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling URL2ArticleApi->get_article: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://url2api.applinzi.com* or your `API_SERVICE_URL`

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*URL2ArticleApi* | get_article | **GET** /article | 网页结构智能解析 HTTP Get 接口
*URL2ArticleApi* | get_article_by_post | **POST** /article | 网页结构智能解析 HTTP Post 接口
*URL2NLPApi* | get_keywords | **POST** /v1/nlp/keywords | 关键词提取接口
*URL2NLPApi* | get_word_cut | **POST** /v1/nlp/word/cut | 中文分词和词性注解接口

more details: https://github.com/url2io/url2io-python-client/tree/master/src#documentation-for-api-endpoints

## Documentation For Models

 - ArticleForResponse
 - NlpKeywordsItemForResponse
 - NlpWordCutItemForResponse

more details: https://github.com/url2io/url2io-python-client/tree/master/src#documentation-for-models


## Documentation For Authorization


## token_in_query

- **Type**: API key
- **API key parameter name**: token
- **Location**: URL query string


## Author

url2#sina.com
