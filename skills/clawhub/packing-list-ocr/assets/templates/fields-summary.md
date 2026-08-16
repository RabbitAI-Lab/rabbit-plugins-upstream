# 各识别类型的字段说明（elements 内容）

根据 ocrType 不同，返回的 `elements` 对象包含以下字段：

## PACKING_LIST (装箱单)
- `packingListNo`: 装箱单号
- `invoiceNo`: 发票号
- `issueDate`: 签单日期
- `exporterName`: 出单方
- `exporterAddress`: 出单方地址
- `consigneeName`: 收货人
- `consigneeAddress`: 收货人地址
- `notifyParty`: 通知方
- `loadingPort`: 起运港
- `dischargePort`: 卸货港
- `vesselNo`: 航次号
- `containerNo`: 箱号
- `totalNetWeight`: 总净重
- `totalGrossWeight`: 总毛重
- `totalMeasurement`: 总体积
- `priceTerm`: 成交方式
- `contractNumber`: 合同号
- `lcNumber`: 信用证编号


