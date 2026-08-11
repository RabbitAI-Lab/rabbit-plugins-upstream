# 各识别类型的字段说明（elements 内容）

根据 ocrType 不同，返回的 `elements` 对象包含以下字段：

## RIDE_HAILING_ITINERARY (网约车行程单)
- `title`: 标题
- `applyTime`: 申请时间
- `tripTime`: 行程时间
- `passengerPhone`: 行程人手机号
- `totalAmountLower`: 合计金额(小写)
- `pageNo`: 页码
- `tripDetails`: 行程明细（数组）
  - `tripSerialNo`: 序号
  - `tripServiceProvider`: 服务商
  - `tripRideType`: 车型
  - `tripPickupTime`: 上车时间
  - `tripCity`: 城市
  - `tripStartLocation`: 起点
  - `tripEndLocation`: 终点
  - `tripMileage`: 里程
  - `tripAmt`: 金额
  - `tripRemark`: 备注

