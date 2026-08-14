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
  "data": [
    {
      "traceId": "202604010000016",
      "originalFilename": "卫生许可证示例.jpg",
      "cosPath": "scnetAPIService/20260101/7fd9d6780dc6454eaf11699244f46ef3.jpg",
      "result": [
        {
          "status": 200,
          "originFilename": "卫生许可证示例.jpg",
          "cosPath": "scnetAPIService/20260101/7fd9d6780dc6454eaf11699244f46ef3.jpg",
          "fileIndex": 1,
          "cutIndex": 0,
          "coordinate": [],
          "classifyCode": "",
          "confidence": 0.8814,
          "elements": {
            "title": "卫生许可证",
            "licenseNumber": "北京卫监字(2018)第12091号",
            "operatorName": "北京来来碗餐饮有限公司",
            "address": "北京市朝阳区来广营地区奥北中心大厦B1-1002",
            "legalRepresentative": "李卫东",
            "placeCategory": "餐饮",
            "permittedItems": "餐饮",
            "issuingAuthority": "朝阳区行政审批局",
            "issueDate": "2018年12月12日",
            "expiryDate": "2018年12月12日至2023年12月12日"
          },
          "stamps": []
        }
      ]
    }
  ]
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
