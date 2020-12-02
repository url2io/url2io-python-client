# ArticleForResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | 网页正文的标题 | 
**url** | **str** | 要提取正文网页的网址 | 
**_date** | **str** | 文章的发布日期。ISO 8601格式，2014-01-01 01:01:01。如果没有则返回null | 
**content** | **str** | 网页正文 | 
**text** | **str** | 网页正文的纯文字格式。在请求的fields中指定text时，返回此字段。 | [optional] 
**markdown** | **str** | 网页正文的 markdown 格式。在请求的fields中指定markdown时，返回此字段。 | [optional] 
**next** | **str** | 网页的下一页链接。在请求的fields中指定markdown时，返回此字段。若没有则返回null | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


