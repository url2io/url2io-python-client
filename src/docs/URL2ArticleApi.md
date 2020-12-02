# url2io_client.URL2ArticleApi

All URIs are relative to *http://url2api.applinzi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article**](URL2ArticleApi.md#get_article) | **GET** /article | 网页结构智能解析 HTTP Get 接口
[**get_article_by_post**](URL2ArticleApi.md#get_article_by_post) | **POST** /article | 网页结构智能解析 HTTP Post 接口


# **get_article**
> ArticleForResponse get_article(url, fields=fields, param_callback=param_callback)

网页结构智能解析 HTTP Get 接口

用来提取并解析网页中的正文区域，实现网页正文提取、标题提取、发布日期提取、下一页链接提取等。

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 要提取正文网页的网址，参考 [URL Encoding](http://www.w3schools.com/tags/ref_urlencode.asp) | 
 **fields** | [**list[str]**](str.md)| 指示需要额外返回的额外字段，取值为：  - &#x60;next&#x60;: 表示要提取下一页链接。   - &#x60;text&#x60;: 表示要返回正文的纯文字格式。   - &#x60;markdown&#x60;: 表示返回正文的markdown格式。   构造url时多个值通过&#39;,&#39;号隔开，如&#x60;?fields&#x3D;text,next&#x60;。调用sdk时使用列表即可，如fields&#x3D; [&#39;text&#39;, &#39;markdown&#39;]。 | [optional] 
 **param_callback** | **str**| 使用jsonp实现Ajax跨域请求时需要传此参数 | [optional] 

### Return type

[**ArticleForResponse**](ArticleForResponse.md)

### Authorization

[token_in_query](../README.md#token_in_query)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_article_by_post**
> ArticleForResponse get_article_by_post(url, body, fields=fields, param_callback=param_callback)

网页结构智能解析 HTTP Post 接口

用来提取并解析网页中的正文区域，实现网页正文提取、标题提取、发布日期提取、下一页链接提取等。

### Example
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
body = 'body_example' # str | 需要提取的网页的html源码
fields = ['fields_example'] # list[str] | 指示需要额外返回的字段，取值为：  - `next`: 表示要提取下一页链接。   - `text`: 表示要返回正文的纯文字格式。   - `markdown`: 表示返回正文的markdown格式。   构造url时多个值通过','号隔开，如`?fields=text,next`。调用sdk时使用列表即可，如fields= ['text', 'markdown']。 (optional)
param_callback = 'param_callback_example' # str | 使用jsonp实现Ajax跨域请求时需要传此参数 (optional)

try:
    # 网页结构智能解析 HTTP Post 接口
    api_response = api_instance.get_article_by_post(url, body, fields=fields, param_callback=param_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling URL2ArticleApi->get_article_by_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| 要提取正文网页的网址，参考 [URL Encoding](http://www.w3schools.com/tags/ref_urlencode.asp) | 
 **body** | **str**| 需要提取的网页的html源码 | 
 **fields** | [**list[str]**](str.md)| 指示需要额外返回的字段，取值为：  - &#x60;next&#x60;: 表示要提取下一页链接。   - &#x60;text&#x60;: 表示要返回正文的纯文字格式。   - &#x60;markdown&#x60;: 表示返回正文的markdown格式。   构造url时多个值通过&#39;,&#39;号隔开，如&#x60;?fields&#x3D;text,next&#x60;。调用sdk时使用列表即可，如fields&#x3D; [&#39;text&#39;, &#39;markdown&#39;]。 | [optional] 
 **param_callback** | **str**| 使用jsonp实现Ajax跨域请求时需要传此参数 | [optional] 

### Return type

[**ArticleForResponse**](ArticleForResponse.md)

### Authorization

[token_in_query](../README.md#token_in_query)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

