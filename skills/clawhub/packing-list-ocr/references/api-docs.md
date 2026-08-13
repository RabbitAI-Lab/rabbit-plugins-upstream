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
    "originalFilename": "装箱单示例.jpg",
    "cosPath": "scnetAPIService/20260101/5b88c72177ce4bd0bb873ed6069f56a4.jpg",
    "result": [
      {
        "status": 200,
        "originFilename": "装箱单示例.jpg",
        "cosPath": "scnetAPIService/20260101/5b88c72177ce4bd0bb873ed6069f56a4.jpg",
        "fileIndex": 1,
        "cutIndex": 0,
        "coordinate": [],
        "classifyCode": "",
        "confidence": 0.9907,
        "elements": {
          "packingListNo": "BHGX-W200404040404",
          "invoiceNo": " INV989813091",
          "issueDate": "MAY 26, 2019",
          "exporterName": "FUJIAN UJLLION HUJH-TETE MATERIAL INDUSTRY CO., LTD",
          "exporterAddress": "JINLON INDUSTRIAL AREA,LONLON TOWN,JINJIANG CITY,FUJIAN,CHINA",
          "consigneeName": "SKYSKY NETWORKS",
          "consigneeAddress": "1964, GYEONGCHUNG-DAERO, GYEWOL-GYEON, GYEON-SI, GYEONGGI-DO, GYEUBLIC OF KOREA",
          "notifyParty": "SR.DGM/Material SERVICE, BHEL ROAD 6TH FLOOR. UIU FERI BUILDING NO 123 ANNA FORORIDA US",
          "loadingPort": " XIAMEN,CHINA",
          "dischargePort": " INCHON, REPUBLIC OF KOREA",
          "vesselNo": " SM TOKYO 0404E",
          "containerNo": "SMCU1072120 SMCU1095655",
          "totalNetWeight": "39084.0",
          "totalGrossWeight": "40670.0",
          "totalMeasurement": "60.648",
          "priceTerm": " CIF INCHON, REPUBLIC OF KOREA",
          "contractNumber": " BHGX-W2020202020B",
          "lcNumber": " M04EU2005NU202020"
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
