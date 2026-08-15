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
      "originalFilename": "组织机构代码证示例.jpeg",
      "cosPath": "scnetAPIService/20260101/aeb4333e4e494d6c87a13f125765f79f.jpeg",
      "result": [
        {
          "status": 200,
          "originFilename": "组织机构代码证示例.jpeg",
          "cosPath": "scnetAPIService/20260101/aeb4333e4e494d6c87a13f125765f79f.jpeg",
          "fileIndex": 1,
          "cutIndex": 0,
          "coordinate": [],
          "classifyCode": "",
          "confidence": 0.9415,
          "elements": {
            "title": "中华人民共和国组织机构代码证",
            "copyFlag": "副本",
            "certificateNumber": "20109898983",
            "code": "57575757-8",
            "organizationName": "金电市冶东自动化设备有限公司",
            "organizationType": "企业法人",
            "legalRepresentative": "金东",
            "address": "广东省金电市金电镇横坑东莞市百业五金电子城内五街313号",
            "validityPeriod": "自2011年04月13日至2015年04月13日",
            "issuingAuthority": "广东省金电市质量技术监督局",
            "registrationNumber": "组代管441441-441441-1"
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
