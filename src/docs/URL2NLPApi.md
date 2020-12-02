# url2io_client.URL2NLPApi

All URIs are relative to *http://url2api.applinzi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_keywords**](URL2NLPApi.md#get_keywords) | **POST** /v1/nlp/keywords | 关键词提取接口
[**get_word_cut**](URL2NLPApi.md#get_word_cut) | **POST** /v1/nlp/word/cut | 中文分词和词性注解接口


# **get_keywords**
> list[NlpKeywordsItemForResponse] get_keywords(body, top_k=top_k, with_weight=with_weight, allow_pos=allow_pos)

关键词提取接口

支持提取出文本中最有代表性的关键词，并给出对应的权重。

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
api_instance = url2io_client.URL2NLPApi(url2io_client.ApiClient(configuration))
body = 'body_example' # str | 需要分词的文本
top_k = 10 # int | 返回关键词的个数，默认10，最大50 (optional) (default to 10)
with_weight = false # bool | 是否返回每个关键词的权重，默认:不返回。 (optional) (default to false)
allow_pos = '' # str | 允许的关键词词性列表，如只返回动词和名词可以表示为 v,n，默认:允许全部词性。有关词性标签和词性描述，请访问[词性标注](http://url2io.applinzi.com/#url2nlp_pos_tagging)。 (optional) (default to )

try:
    # 关键词提取接口
    api_response = api_instance.get_keywords(body, top_k=top_k, with_weight=with_weight, allow_pos=allow_pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling URL2NLPApi->get_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| 需要分词的文本 | 
 **top_k** | **int**| 返回关键词的个数，默认10，最大50 | [optional] [default to 10]
 **with_weight** | **bool**| 是否返回每个关键词的权重，默认:不返回。 | [optional] [default to false]
 **allow_pos** | **str**| 允许的关键词词性列表，如只返回动词和名词可以表示为 v,n，默认:允许全部词性。有关词性标签和词性描述，请访问[词性标注](http://url2io.applinzi.com/#url2nlp_pos_tagging)。 | [optional] [default to ]

### Return type

[**list[NlpKeywordsItemForResponse]**](NlpKeywordsItemForResponse.md)

### Authorization

[token_in_query](../README.md#token_in_query)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_word_cut**
> list[NlpWordCutItemForResponse] get_word_cut(body, keep_stopwords=keep_stopwords, symbols=symbols, dict=dict, custom_dict=custom_dict, with_flag=with_flag, hmm=hmm)

中文分词和词性注解接口

支持中文分词、去停用词、新词发现、词性注解等功能。

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
api_instance = url2io_client.URL2NLPApi(url2io_client.ApiClient(configuration))
body = 'body_example' # str | 需要分词的文本
keep_stopwords = true # bool | 是否保留停用词 (optional) (default to true)
symbols = true # bool | 是否返回特殊字符 (optional) (default to true)
dict = false # bool | 是否使用领域词典(预留) (optional) (default to false)
custom_dict = false # bool | 是否使用自定义词典（预留） (optional) (default to false)
with_flag = true # bool | 是否返回词性标注 (optional) (default to true)
hmm = true # bool | 是否使用新词发现 (optional) (default to true)

try:
    # 中文分词和词性注解接口
    api_response = api_instance.get_word_cut(body, keep_stopwords=keep_stopwords, symbols=symbols, dict=dict, custom_dict=custom_dict, with_flag=with_flag, hmm=hmm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling URL2NLPApi->get_word_cut: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| 需要分词的文本 | 
 **keep_stopwords** | **bool**| 是否保留停用词 | [optional] [default to true]
 **symbols** | **bool**| 是否返回特殊字符 | [optional] [default to true]
 **dict** | **bool**| 是否使用领域词典(预留) | [optional] [default to false]
 **custom_dict** | **bool**| 是否使用自定义词典（预留） | [optional] [default to false]
 **with_flag** | **bool**| 是否返回词性标注 | [optional] [default to true]
 **hmm** | **bool**| 是否使用新词发现 | [optional] [default to true]

### Return type

[**list[NlpWordCutItemForResponse]**](NlpWordCutItemForResponse.md)

### Authorization

[token_in_query](../README.md#token_in_query)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

