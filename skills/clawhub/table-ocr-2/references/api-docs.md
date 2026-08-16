# Sugon-Scnet OCR API 文档摘要

## 接口地址
`POST https://api.scnet.cn/api/llm/v1/ocr/recognize`

## 请求头
- `Content-Type: multipart/form-data`
- `Authorization: Bearer <你的 API Key>`

## 请求参数（表单）
| 参数名  | 类型 | 必填 | 描述                                   |
| ------- | ---- | ---- | -------------------------------------- |
| file    | File | 是   | 需要识别的图片文件                     |
| ocrType | str  | 是   | 识别类型枚举，详见 SKILL.md 参数说明   |

## 响应结构
```json
{
  "code": "0",
  "msg": "success",
  "data": {
    "traceId": "12345678909",
    "originalFilename": "表格示例.jpg",
    "cosPath": "scnetAPIService/20260101/a83da56fc4db4c6ba605cd206b83ec78.jpg",
    "result": [
      {
        "status": 200,
        "originFilename": "表格示例.jpg",
        "cosPath": "scnetAPIService/20260101/a83da56fc4db4c6ba605cd206b83ec78_cut_1.jpg",
        "fileIndex": 1,
        "cutIndex": 1,
        "coordinate": [16, 565, 16, 29, 876, 29, 876, 565],
        "classifyCode": "",
        "confidence": 0.9864,
        "elements": {
          "tables": [
            {
              "type": "wired_table",
              "bbox": [14, 101, 839, 484],
              "html": "<html><body><table><tr><td rowspan=2 colspan=1>学期科目</td><td rowspan=1 colspan=2>初一</td><td rowspan=1 colspan=2>初 二</td><td rowspan=1 colspan=2>初 三</td></tr><tr><td rowspan=1 colspan=1>第一学期</td><td rowspan=1 colspan=1>第二学期</td><td rowspan=1 colspan=1>第一学期</td><td rowspan=1 colspan=1>第二学期</td><td rowspan=1 colspan=1>第一学期</td><td rowspan=1 colspan=1>第二学期</td></tr><tr><td rowspan=1 colspan=1>语文</td><td rowspan=1 colspan=1>86</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1>87</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>81</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>数学</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>87</td><td rowspan=1 colspan=1>79</td></tr><tr><td rowspan=1 colspan=1>英语</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>90</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>95</td><td rowspan=1 colspan=1>94</td></tr><tr><td rowspan=1 colspan=1>物理</td><td rowspan=1 colspan=1>86</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1>88</td><td rowspan=1 colspan=1>84</td><td rowspan=1 colspan=1>89</td></tr><tr><td rowspan=1 colspan=1>化学</td><td rowspan=1 colspan=1>86</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>91</td></tr><tr><td rowspan=1 colspan=1>生物</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>95</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>政治</td><td rowspan=1 colspan=1>85</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>79</td></tr><tr><td rowspan=1 colspan=1>历史</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>90</td></tr><tr><td rowspan=1 colspan=1>地理</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>92</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>89</td><td rowspan=1 colspan=1>91</td><td rowspan=1 colspan=1>79</td></tr></table></body></html>"
            }
          ]
        },
        "stamps": []
      }
    ]
  }
}
```


## 错误码
- `401 / 403: Token 无效或过期`
- `其他 4xx/5xx: 请检查请求参数或联系服务商`
- `业务错误码（如 code 非 0）：见返回的 msg 字段`

## 注意事项
- `支持单张图片、PDF 或多页压缩包（自动解压识别）`
- `识别结果位于 data[0].result[0].elements 中`
- `不同 ocrType 返回的 elements 字段不同，详见 assets/templates/fields-summary.md`
- `识别结果位于 data[0].result[0].stamps 中`
- `不同 ocrType 返回的 stamps 字段不同，详见 assets/templates/fields-summary.md`
