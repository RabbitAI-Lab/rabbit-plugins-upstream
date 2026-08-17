# 各识别类型的字段说明（elements 内容）

根据 ocrType 不同，返回的 `elements` 对象包含以下字段：

## FOOD_BUSINESS_LICENSE (食品经营许可证)

- `title`: 标题
- `copyFlag`: 副本标识
- `operatorName`: 经营者名称
- `licenseNumber`: 许可证编号
- `socialCreditCode`: 社会信用代码
- `legalRepresentative`: 法定代表人
- `address`: 住所
- `businessPlace`: 经营场所
- `businessType`: 主体业态
- `businessItems`: 经营项目
- `dailySupervisionAuthority`: 日常监督管理机构
- `dailySupervisionStaff`: 日常监督管理人员
- `complaintHotline`: 投诉举报电话
- `issuingAuthority`: 发证机关
- `signatory`: 签发人
- `issueDate`: 发证日期
- `expiryDate`: 有效期至

## FOOD_PRODUCTION_LICENSE (食品生产许可证)

- `title`: 标题
- `copyFlag`: 副本标识
- `producerName`: 生产者名称
- `licenseNumber`: 许可证编号
- `socialCreditCode`: 社会信用代码
- `legalRepresentative`: 法定代表人
- `address`: 住所
- `productionAddress`: 生产地址
- `foodCategory`: 食品类别
- `dailySupervisionAuthority`: 日常监督管理机构
- `dailySupervisionStaff`: 日常监督管理人员
- `complaintHotline`: 投诉举报电话
- `issuingAuthority`: 发证机关
- `signatory`: 签发人
- `issueDate`: 发证日期
- `expiryDate`: 有效期至

## HYGIENE_LICENSE (卫生许可证)

- `title`: 标题
- `licenseNumber`: 许可证编号
- `operatorName`: 单位名称
- `address`: 单位地址
- `legalRepresentative`: 法定代表人
- `placeCategory`: 场所类别
- `permittedItems`: 许可项目
- `issuingAuthority`: 发证机关
- `issueDate`: 发证日期
- `expiryDate`: 有效期

## FINANCIAL_LICENSE (金融许可证)

- `title`: 标题
- `certificateNumber`: 证件编号
- `institutionName`: 机构名称
- `shortName`: 简称
- `institutionEnName`: 英文名称
- `businessScope`: 业务范围
- `approvalDate`: 批准日期
- `institutionAddress`: 机构住所
- `institutionCode`: 机构编码
- `issuingAuthority`: 发证机关
- `issueDate`: 发证日期

## FINANCIAL_INSTITUTION_CODE_CERT (金融机构代码证)

- `title`: 标题
- `certificateNumber`: 证件编号
- `code`: 代码
- `institutionName`: 机构名称
- `address`: 地址
- `legalRepresentative`: 法定代表人
- `firstIssueDate`: 首次颁发日期
- `issuingAuthority`: 颁发机关
- `registrationNumber`: 登记号
- `replacementDate`: 更换日期

## PAYMENT_BUSINESS_LICENSE (支付业务许可证)

- `title`: 标题
- `copyFlag`: 副本标识
- `licenseNumber`: 许可证编号
- `companyName`: 公司名称
- `legalRepresentative`: 法定代表人
- `address`: 住所
- `businessType`: 业务类型
- `businessCoverage`: 业务覆盖范围
- `issueDate`: 发证日期
- `expiryDate`: 有效期至

## ACCOUNT_OPENING_LICENSE (开户许可证)

- `title`: 标题
- `approvalNumber`: 核准号
- `licenseNumber`: 编号
- `companyName`: 公司名称
- `legalRepresentative`: 法定代表人
- `bankName`: 开户银行
- `bankAccount`: 开户银行账号
- `issueDate`: 发证日期
