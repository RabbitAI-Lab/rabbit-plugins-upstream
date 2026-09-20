---
name: Insurance Industry Bidding Expert
description: AI-powered insurance bidding expert for China market — covers the complete insurance bid lifecycle including solvency disclosure (C-ROSS Rules II), reinsurance arrangements, regulator compliance, policy clause comparison, risk reserve explanations, and current procurement rules. Built for insurance companies, brokers, and insurtech companies. Keywords: insurance bid, group insurance bid, solvency, reinsurance, NFRA compliance, China insurance, 招投标法修订, 团险投标, 保险标书撰写, C-ROSS合规, 再保险安排, 政府采购, 电子投标, 标书生成, 废标检查, 保费报价, 条款比对, 惠民保, 共保体.
slug: insurance-bidding-pro
version: 5.0.3

capabilities:
  - educational-reference
  - advisory-only
  - requires-human-review
  - no-executable-code
---

# Insurance Industry Bidding Expert (Insurance Bidding Pro) / 保险行业投标专家

> **⚠️ SECURITY NOTICE / 安全声明**
> - **Type:** Educational reference / analytical framework ONLY
> - **No executable code, scripts, or binaries are included in this skill**
> - **No persistent storage, network calls, background execution, or credential collection**
> - **All outputs are for reference only and require human review before real-world application**
> - **This skill does NOT provide financial, legal, or insurance advice**
> - **Users must exercise their own judgment and consult qualified professionals**

> **English:** AI-powered insurance bidding expert — the definitive vertical skill for insurance companies, brokers, and insurtech companies participating in China government and corporate procurement bids. Covers solvency disclosure (C-ROSS), reinsurance arrangements, regulator compliance, policy clause comparison, and risk reserve explanations. Unique to this skill: insurance-specific bid modules that generic tools cannot provide.
>
> **中文:** 保险行业投标专家——保险公司、保险经纪公司、保险科技企业参与招标的必备垂直工具。覆盖偿付能力披露（偿二代规则Ⅱ）、再保险安排、国家金融监督管理总局合规、条款比对、风险准备金说明，以及城市定制型商业医疗险（惠民保）共保体投标等保险特有模块，是通用招标工具无法覆盖的专业场景。

> **术语提示**：保险业监管机构自 2023 年起为国家金融监督管理总局（NFRA），原中国银行保险监督管理委员会（CBIRC / 银保监会）已不再使用。引用历史文件时保留原文机构名，本技能正文统一使用现行名称。

---

## Trigger Keywords / 触发关键词

**English Triggers:** insurance bid, insurance bidding, group insurance bid, insurance tender, solvency disclosure, reinsurance, NFRA compliance, insurance policy comparison, C-ROSS, risk reserve, inclusive insurance co-insurance

**中文触发词（优先）：** 保险投标、团险投标、保险标书、保险公司招标、偿付能力、再保险、保险条款比对、偿二代、风险准备金、国家金融监督管理总局、惠民保、共保体投标、理赔服务承诺、废标检查

> 触发边界：本技能面向**保险机构参与招投标**场景。通用工程/采购招标流程请使用通用招投标工具。

---

## Core Capabilities / 核心能力

### 0. 保险投标监管动态（截至 2026-09-15）

| 时间 | 动态 | 对保险投标的影响 | 投标侧应对 |
|------|------|---------------|-----------|
| **2026年1月1日** | 招标投标领域新规实施 | 招标人主体责任更明确，资格预审标准更规范 | 逐条核对资格预审条件，不留"待补" |
| **2026年** | 《招标投标法》修订推进 | 投标保证金管理、电子化投标要求提升 | 关注保证金形式与退还条款 |
| **2026年** | 金融监管机构改革后续落地 | 投标文件中的监管机构名称需使用现行表述 | 全文检索并替换过时机构名 |
| **2026年** | 数据安全与个人信息保护要求深化 | 投标文件中涉及客户数据的部分需脱敏 | 案例数据去标识化后使用 |
| **2025年** | 政府采购云平台扩大应用 | 保险投标需支持电子投标（PDF + 结构化表单） | 提前确认平台格式与签章要求 |
| **2025年10月** | 第四套生命表发布 | 影响定价基础，技术标中精算说明需更新 | 核对精算假设引用版本 |
| **2025年** | 金融机构联合打击黑灰产 | 招标方对反欺诈能力评估趋严 | 补充反欺诈体系与数据佐证 |
| **持续** | 偿二代规则Ⅱ执行 | 偿付能力披露格式与口径要求稳定 | 使用最新季度披露数据 |

> **数据截止**: 2026-09-15 | 来源：监管公开信息与行业实践整理
> **声明**: 以上动态供参考，具体以官方最新发布为准。

---

### 1. Insurance Bid Document Generation / 保险投标文书生成

#### 技术标模块

| 模块 | 应包含内容 | 评审关注点 | 常见失分点 |
|-----|-----------|-----------|-----------|
| 公司资质 | 保险许可证、营业执照、信用评级 | 许可证在有效期内、业务范围覆盖标的 | 许可证过期或范围不覆盖 |
| 偿付能力 | 核心/综合偿付能力充足率、风险综合评级 | 数据为最新披露期、口径与监管一致 | 使用过期季度数据 |
| 再保险安排 | 比例/非比例分保安排说明 | 危险单位划分合理、分保比例可支撑保额 | 说明笼统，未对应标的规模 |
| 理赔服务 | 全国网点、时效承诺、绿色通道 | 承诺可考核、有数据支撑 | 承诺无依据（如"24小时必赔"） |
| 风控体系 | 核保规则、风控模型、反欺诈 | 有实际案例与数据 | 只讲概念无数据 |
| IT 能力 | 核心系统、线上服务平台 | 与招标要求的对接能力 | 未回应招标指定的接口要求 |
| 服务团队 | 项目负责人、服务人员配置 | 人员资质与投入承诺 | 人员与实际不符 |

#### 商务标模块

| 模块 | 构成 | 报价要点 | 风险提示 |
|-----|------|---------|---------|
| 保费报价 | 纯风险保费 + 费用附加 + 利润附加 | 三部分分别列示，便于评审 | 只报总价，评审无法比对 |
| 免赔设定 | 免赔额或免赔率 | 与风险暴露匹配 | 设定与招标要求冲突 |
| 费率浮动 | 与历史赔付率挂钩 | 写明浮动区间与上下限 | 区间过大被认定不可执行 |
| 增值服务 | 健康管理、风险咨询、理赔协助 | 明确服务内容与频次 | 承诺无法交付 |

**报价结构说明（示例口径）**

| 组成 | 说明 | 常见取值逻辑 |
|-----|------|------------|
| 纯风险保费 | 基于历史赔付与风险暴露测算 | 由精算按险类经验数据测算 |
| 费用附加 | 获取与服务成本 | 按实际费用预算分摊 |
| 利润附加 | 风险对价 | 参照同类业务与竞争情况 |
| 安全边际 | 应对经验波动 | 结合业务年限与波动性确定 |

> **注意**：以上为结构示例，具体取值必须由精算与业务部门按公司实际经验数据确定，并履行内部审批程序。

#### 废标风险检查（保险专属）

| 检查项 | 合格标准 | 风险等级 | 处置 |
|-------|---------|---------|------|
| 保险许可证 | 在有效期且业务范围覆盖 | 高 | 过期立即更换并说明 |
| 分支机构许可 | 服务区域有对应许可 | 高 | 调整服务方案或联营 |
| 偿付能力充足率 | 满足监管要求（核心充足率、综合充足率达标） | 高 | 不符合则不建议投标 |
| 再保险安排 | 危险单位划分与分保比例合规 | 中 | 补充说明材料 |
| 条款合规 | 不含违反强制性规定的内容 | 高 | 逐条排查格式条款 |
| 报价响应度 | 满足招标文件实质性要求 | 高 | 逐项对照答标 |
| 签章完整性 | 法人签字、公章、骑缝章齐全 | 中 | 按招标要求逐页确认 |
| 电子投标格式 | 符合平台要求的文件格式与大小 | 中 | 提前测试上传 |

---

### 2. Insurance Policy Clause Comparison / 保险条款比对

| 比对类型 | 比对要点 | 输出物 |
|---------|---------|-------|
| 主险 vs 附加险 | 保障范围衔接、免责叠加 | 保障缺口清单 |
| 不同公司产品 | 同等保费下的责任差异 | 条款对比表 |
| 新旧条款 | 监管新规下的责任调整 | 变更影响说明 |
| 招标要求 vs 拟投保单 | 逐条响应度 | 响应偏离表 |
| 免赔与限额 | 触发条件、累计口径 | 赔付测算示例 |

**条款比对输出要求**

| 要素 | 要求 |
|-----|------|
| 逐条对应 | 招标条款与响应条款一一对应编号 |
| 偏离标注 | 正偏离/负偏离/完全响应三类明确标注 |
| 差异说明 | 负偏离必须给出替代方案 |
| 免责提示 | 免责条款不得弱化表述 |

---

### 3. Regulatory Compliance Check / 监管合规核对

逐项核对以下要点（结果需由合规部门复核确认）：

- **《保险法》** 相关条款符合性
- **《保险公司偿付能力监管规则》** 披露完整性
- **《再保险业务管理规定》** 分保安排合规性
- **《保险条款和保险费率管理办法》** 条款报备情况
- **保险中介相关监管规定** 经纪机构与代理机构资质
- **数据与个人信息保护要求** 案例数据脱敏情况

**合规核对记录表**

| 核对项 | 依据 | 结论 | 复核人 | 复核日期 |
|-------|------|------|-------|---------|
| 偿付能力披露 | 监管规则 | 通过/需补充 | 合规岗 | 待填 |
| 条款报备 | 产品管理办法 | 通过/需补充 | 产品岗 | 待填 |
| 再保安排 | 再保险规定 | 通过/需补充 | 精算岗 | 待填 |
| 数据脱敏 | 数据保护要求 | 通过/需补充 | 数据岗 | 待填 |

---

### 4. Group Insurance Specialization / 团险与政府统保专项能力

| 场景 | 方案要点 | 投标侧重点 |
|-----|---------|-----------|
| 团体健康险 | 重疾、医疗、意外组合 | 既往赔付数据与控费能力 |
| 企业年金/补充养老 | 方案设计、收益测算 | 投资管理能力与历史业绩 |
| 关键人员保险 | 董责险、关键人寿险 | 承保能力与全球服务网络 |
| 员工福利计划 | 弹性福利、自选套餐 | 平台与运营支持能力 |
| 城市定制型商业医疗险（惠民保） | 共保体分工、带病体与健康体定价、政府协同服务 | 共保体角色与份额、既往承办经验、医保数据对接能力 |

**惠民保 / 政府统保类投标特别提示**

| 关注点 | 说明 |
|-------|------|
| 共保体结构 | 首席承保人与共保成员份额、结算规则需在投标文件中明确 |
| 定价基础 | 带病体与健康体参保结构影响赔付，需说明定价假设与再保支持 |
| 政府协同 | 参保动员、数据对接、服务承诺需可落地 |
| 既往经验 | 承办历史、赔付率、续保率是核心评分项 |
| 服务能力 | 一键理赔、线上服务、咨询响应时效 |

---

## Workflow / 工作流程

```
阶段一：需求解析
  → 识别招标类型（企业团险 / 政府统保 / 经纪招标 / 共保体）
  → 提取保险责任范围、保额、免赔额等关键参数
  → 识别投标人资质要求（注册资本、分支机构、偿付能力）

阶段二：文书编制
  → 按机构既有模板库结构填写保险行业特有内容
  → 根据招标要求填入偿付能力、再保险等特有内容
  → 形成技术标、商务标、资格证明文件三个分册

阶段三：风险核对
  → 逐项核对监管合规要点
  → 核对报价响应度与实质性要求
  → 检查签字盖章完整性

阶段四：优化建议
  → 基于历史承办数据给出报价优化方向
  → 识别竞争差异化亮点
  → 给出增值服务组合建议
```

**投标时间倒排表（建议）**

| 距投标截止 | 应完成事项 | 责任方 |
|-----------|-----------|-------|
| T-15 日 | 招标文件逐条解读、问答澄清提交 | 业务 + 投标牵头 |
| T-12 日 | 技术标初稿、偿付能力数据取数 | 业务 + 精算 |
| T-10 日 | 商务标报价测算、内部审批启动 | 精算 + 财务 |
| T-7 日 | 条款响应偏离表完成 | 产品 + 法律 |
| T-5 日 | 合规核对与数据脱敏确认 | 合规 + 数据 |
| T-3 日 | 全套文件内部复核、签章 | 投标牵头 |
| T-1 日 | 电子平台上传测试、纸质材料装订 | 投标牵头 |
| T 日 | 按平台要求提交 | 投标牵头 |

---

## 常见废标原因与处置 / Common Disqualification Causes

| 原因 | 典型表现 | 预防动作 |
|-----|---------|---------|
| 资格不符 | 分支机构或经营范围不覆盖 | 资格预审阶段先行核对 |
| 实质性偏离 | 报价或保障范围不满足要求 | 逐条对照答标 |
| 签章缺失 | 漏签、漏盖、骑缝章不全 | 按页码清单逐项打勾 |
| 数据过期 | 偿付能力数据未用最新披露期 | 取数时记录披露期 |
| 格式不符 | 文件格式或份数不符合要求 | 提前在平台测试上传 |
| 承诺无依据 | 时效承诺无法考核 | 改为可考核的表述 |

---

## Synergy with Other Skills / 与其他技能配合

以下技能由使用者按需自行选用，本技能不代为执行：

- **tender-bidding-assistant**：通用招标流程与文书规范
- **docx / xlsx / pdf 类技能**：文档排版、报价明细表、扫描件合并
- **insurance-solvency-reporter**：偿付能力披露的深度内容
- **insurance-actuarial-cn**：保费测算与定价假设核对

---

## Disclaimer

This skill provides insurance bidding frameworks and analytical reference material for
educational purposes. It does not execute code, does not access external systems, and does not
constitute financial, legal, insurance, or bidding advice. All compliance conclusions, pricing
assumptions, and bid documents produced with its help must be reviewed by the responsible
business, actuarial, legal, and compliance functions before submission.
