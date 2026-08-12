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
      "traceId": "202604010000021",
      "originalFilename": "网约车行程单示例.png",
      "cosPath": "scnetAPIService/20260101/2941943a4cf2453dacca44d2dc6fa5d3.png",
      "result": [
        {
          "status": 200,
          "originFilename": "网约车行程单示例.png",
          "cosPath": "scnetAPIService/20260101/2941943a4cf2453dacca44d2dc6fa5d3.png",
          "fileIndex": 1,
          "cutIndex": 0,
          "coordinate": [],
          "classifyCode": "",
          "confidence": 0.995,
          "elements": {
            "title": "高德地图—打车——行程单",
            "applyTime": "2024-07-04",
            "tripTime": "2024-07-03 09:17至2024-07-03 19:27",
            "passengerPhone": "15711281128",
            "totalAmountLower": "55.85",
            "pageNo": "1/1",
            "tripDetails": [
              {
                "tripSerialNo": "1",
                "tripServiceProvider": "曹操出行",
                "tripRideType": "曹操经济型",
                "tripPickupTime": "2024-07-03 09:17",
                "tripCity": "上海市",
                "tripStartLocation": "中国曹操银行培训中心",
                "tripEndLocation": "时间银行大厦",
                "tripMileage": "",
                "tripAmt": "35.39元",
                "tripRemark": ""
              },
              {
                "tripSerialNo": "2",
                "tripServiceProvider": "曹操出行",
                "tripRideType": "曹操经济型",
                "tripPickupTime": "2024-07-03 19:09",
                "tripCity": "上海市",
                "tripStartLocation": "时间银行大厦(西北门)",
                "tripEndLocation": "中国曹操银行培训中心",
                "tripMileage": "",
                "tripAmt": "20.46元",
                "tripRemark": ""
              }
            ]
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
