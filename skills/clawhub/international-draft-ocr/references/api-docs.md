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
    "originalFilename": "国际汇票示例.jpg",
    "cosPath": "scnetAPIService/20260101/d1827ebd51784fa3b24be88730fa8daf.jpg",
    "result": [
      {
        "status": 200,
        "originFilename": "国际汇票示例.jpg",
        "cosPath": "scnetAPIService/20260101/d1827ebd51784fa3b24be88730fa8daf.jpg",
        "fileIndex": 1,
        "cutIndex": 0,
        "coordinate": [],
        "classifyCode": "",
        "confidence": 0.9642,
        "elements": {
          "draftNumber": "BHGX-F201906060606",
          "draftDate": "2019-07-08",
          "amount": "USD187200.00",
          "amountInWords": " US. DOLLARS ONE HUNDRED AND EIGHTY-SEVEN THOUSAND TWO HUNDRED ONLY",
          "payeeName": "CHINA CONSTRUCTION BANK",
          "draweeName": "BKOKKOK BANK PUBLIC COMPANY LIMITED",
          "draftTenor": "At SIGHT  days after Sight of this FIRST of Exchange (Second of exchange being unpaid)",
          "lcNumber": "6261L759051",
          "issueDate": "2019-06-24",
          "issueBank": "BAN BANK BANK PUBLIC COMPANY LIMITED",
          "drawer": "FUJIAN HIGHON HIGH-TECH MATERIAL INDUSTRY CO.,LTD"
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
