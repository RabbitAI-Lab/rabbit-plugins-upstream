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
      "originalFilename": "商标注册证示例.jpg",
      "cosPath": "scnetAPIService/20260101/536655ca029c4cbd9cf37e3b211c6798.jpg",
      "result": [
        {
          "status": 200,
          "originFilename": "商标注册证示例.jpg",
          "cosPath": "scnetAPIService/20260101/536655ca029c4cbd9cf37e3b211c6798.jpg",
          "fileIndex": 1,
          "cutIndex": 0,
          "coordinate": [],
          "classifyCode": "",
          "confidence": 0.9548,
          "elements": {
            "title": "商标注册证",
            "certificateNumber": "49994999",
            "trademarkName": "存得存",
            "serviceType": "第38类",
            "approvedServices": "安全咨询；安全及防盗系统的监控；工厂安全检查；知识产权咨询；版权管理；知识产权许可；四送服务；计算机软件许可(法律服务)；域名注册(截至)",
            "registrantName": "河北银行股份有限公司",
            "registrantAddress": "河北省唐山市唐山西道20号",
            "registrationDate": "2016年10月28日",
            "expiryDate": "2026年10月27日"
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
