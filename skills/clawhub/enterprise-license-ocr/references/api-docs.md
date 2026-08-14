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
      "originalFilename": "食品经营许可证示例.jpg",
      "cosPath": "scnetAPIService/20260101/71d0320caf3a445486259ea8f41ed1dd.jpg",
      "result": [
        {
          "status": 200,
          "originFilename": "食品经营许可证示例.jpg",
          "cosPath": "scnetAPIService/20260101/71d0320caf3a445486259ea8f41ed1dd.jpg",
          "fileIndex": 1,
          "cutIndex": 0,
          "coordinate": [],
          "classifyCode": "",
          "confidence": 0.6496,
          "elements": {
            "title": "食品经营许可证",
            "copyFlag": "副本",
            "operatorName": "广州市青青源餐饮管理服务有限公司",
            "licenseNumber": "JY14414414414449(1-1)",
            "socialCreditCode": "17711771177177100E",
            "legalRepresentative": "邓勇勇",
            "address": "广州市番禺区番禺街番禺东村番禺南路10号之D15、D16铺",
            "businessPlace": "广州市番禺区番禺街番禺东村番禺南路10号之D15、D16铺",
            "businessType": "餐饮服务经营者(餐饮管理企业)",
            "businessItems": "预包装食品销售(含冷藏冷冻食品)，食品经营管理",
            "dailySupervisionAuthority": "广州市番禺区食品药品监督管理局",
            "dailySupervisionStaff": "蓝企明、师哲等",
            "complaintHotline": "12331",
            "issuingAuthority": "广州市番禺区食品药品监督管理局",
            "signatory": "古业",
            "issueDate": "2017年08月04日",
            "expiryDate": "2022年05月30日"
          },
          "stamps": []
        }
      ]
    }
  ]
}
```

```json
{
    "code": "0",
    "msg": "success",
    "data": [
        {
            "traceId": "202604010000016",
            "originalFilename": "食品生产许可证示例.jpg",
            "cosPath": "scnetAPIService/20260101/a04febbc736d4e888496548cb2e8e7c0.jpg",
            "result": [
                {
                    "status": 200,
                    "originFilename": "食品生产许可证示例.jpg",
                    "cosPath": "scnetAPIService/20260101/a04febbc736d4e888496548cb2e8e7c0.jpg",
                    "fileIndex": 1,
                    "cutIndex": 0,
                    "coordinate": [],
                    "classifyCode": "",
                    "confidence": 0.6979,
                    "elements": {
                      "title": "食品生产许可证",
                      "copyFlag": "副本",
                      "producerName": "合肥卡卡咖啡食品有限公司",
                      "licenseNumber": "SC50485048504848",
                      "socialCreditCode": "91391391391391305G(1-1)",
                      "legalRepresentative": "许雪",
                      "address": "安徽省卡卡经济开发区团结路91号",
                      "productionAddress": "安徽省合肥市卡卡经济开发区团结路91号",
                      "foodCategory": "食品",
                      "dailySupervisionAuthority": "肥东县市场监督管理局直属二分局",
                      "dailySupervisionStaff": "袁团结、丁开发",
                      "complaintHotline": "12331",
                      "issuingAuthority": "合肥市食品药品监督管理局",
                      "signatory": "胡国春",
                      "issueDate": "2015年12月2日",
                      "expiryDate": "2020年12月1日"
                    },
                    "stamps": []
                }
            ]
        }
    ]
}
```

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

```json
{
    "code": "0",
    "msg": "success",
    "data": [
        {
            "traceId": "202604010000016",
            "originalFilename": "金融许可证示例.jpeg",
            "cosPath": "scnetAPIService/20260101/41ba187eeaf14c1abba5c131ccd1d659.jpeg",
            "result": [
                {
                    "status": 200,
                    "originFilename": "金融许可证示例.jpeg",
                    "cosPath": "scnetAPIService/20260101/41ba187eeaf14c1abba5c131ccd1d659.jpeg",
                    "fileIndex": 1,
                    "cutIndex": 0,
                    "coordinate": [],
                    "classifyCode": "",
                    "confidence": 0.987,
                    "elements": {
                      "title": "中华人民共和国金融许可证",
                      "certificateNumber": "11223344",
                      "institutionName": "广东业银农村商业银行股份有限公司",
                      "shortName": "业银农村商业银行",
                      "institutionEnName": "Guangdong Sodong Ruoal Commercial Bank Company Limited",
                      "businessScope": "许可该机构经营银行业监督管理机构依照有关法律、行政法规和其他规定批准的业务，经营范围以批准文件所列的为准。",
                      "approvalDate": "2009年12月21日",
                      "institutionAddress": "佛山市顺德区顺德街道办事处顺德居委会顺德路2号",
                      "institutionCode": "B0001000100010001",
                      "issuingAuthority": "中国银行保险监督管理委员会佛山监管分局",
                      "issueDate": "2024年11月27日"
                    },
                    "stamps": []
                }
            ]
        }
    ]
}
```

```json
{
    "code": "0",
    "msg": "success",
    "data": [
        {
            "traceId": "202604010000016",
            "originalFilename": "金融机构代码证示例.png",
            "cosPath": "scnetAPIService/20260101/f238072fa2f4467fbf80e94e861187a2.png",
            "result": [
                {
                    "status": 200,
                    "originFilename": "金融机构代码证示例.png",
                    "cosPath": "scnetAPIService/20260101/f238072fa2f4467fbf80e94e861187a2.png",
                    "fileIndex": 1,
                    "cutIndex": 0,
                    "coordinate": [],
                    "classifyCode": "",
                    "confidence": 0.8887,
                    "elements": {
                      "title": "金融机构代码证",
                      "certificateNumber": "2001010022001",
                      "code": "C1101101100110",
                      "institutionName": "武汉邮政储蓄银行股份有限公司钱江分行",
                      "address": "湖北省武汉市钱江区河头沟地区潜龙家园3单元202-204号",
                      "legalRepresentative": "赵晋迈",
                      "firstIssueDate": "2014-09-18",
                      "issuingAuthority": "中国人民银行资阳市中心支行",
                      "registrationNumber": "512002000352",
                      "replacementDate": "2017-12-05"
                    },
                    "stamps": []
                }
            ]
        }
    ]
}
```

```json
{
    "code": "0",
    "msg": "success",
    "data": [
        {
            "traceId": "202604010000016",
            "originalFilename": "支付业务许可证示例.jpeg",
            "cosPath": "scnetAPIService/20260101/71d0320caf3a445486259ea8f41ed1dd.jpg",
            "result": [
                {
                    "status": 200,
                    "originFilename": "支付业务许可证示例.jpeg",
                    "cosPath": "scnetAPIService/20260101/71d0320caf3a445486259ea8f41ed1dd.jpg",
                    "fileIndex": 1,
                    "cutIndex": 0,
                    "coordinate": [],
                    "classifyCode": "",
                    "confidence": 0.9222,
                    "elements": {
                      "title": "中华人民共和国支付业务许可证",
                      "copyFlag": "副本",
                      "licenseNumber": "Z2008200820082",
                      "companyName": "北京卡卡发宝通支付服务有限公司",
                      "legalRepresentative": "徐京胜",
                      "address": "北京市卡卡区卡卡口东大街14号308室",
                      "businessType": "预付卡发行与受理",
                      "businessCoverage": "北京市",
                      "issueDate": "2026年12月22日",
                      "expiryDate": "二〇二一年十二月二十一日"
                    },
                    "stamps": []
                }
            ]
        }
    ]
}
```

```json
{
    "code": "0",
    "msg": "success",
    "data": [
        {
            "traceId": "202604010000016",
            "originalFilename": "开户许可证示例.jpg",
            "cosPath": "scnetAPIService/20260101/8242e6a7e4a849ebb576e9ffe38ea2d5.jpg",
            "result": [
                {
                    "status": 200,
                    "originFilename": "开户许可证示例.jpg",
                    "cosPath": "scnetAPIService/20260101/8242e6a7e4a849ebb576e9ffe38ea2d5.jpg",
                    "fileIndex": 1,
                    "cutIndex": 0,
                    "coordinate": [],
                    "classifyCode": "",
                    "confidence": 0.6667,
                    "elements": {
                      "title": "开户许可证",
                      "approvalNumber": "J19827410913413",
                      "licenseNumber": "4910-00009200",
                      "companyName": "新乡市新新头头有限公司",
                      "legalRepresentative": "苗林林",
                      "bankName": "中国工商银行嘉嘉县支行",
                      "bankAccount": "89000919364391898314",
                      "issueDate": "2009年11月19日"
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
