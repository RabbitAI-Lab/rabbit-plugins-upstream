# US Tech Giant Analyst — Analysis Framework

Use this template as the exact output skeleton for every company analysis. Replace bracketed cues with sourced facts and a clear judgment. Keep each section tight: 3-6 bullet points plus one sentence of verdict.

## Report Template

```
# [公司名] ([TICKER]) 分析报告
数据日期：YYYY-MM-DD

## 一句话结论
[该公司当前的核心判断：优势 + 主要隐忧，一句话。]

## 1. 商业模式 (Business Model)
- 营收结构：按业务板块拆分（如云 / 设备 / 服务 / 广告），标注各板块占比与增速。
- 赚钱逻辑：高毛利订阅/抽成 vs 低毛利硬件；近期结构性变化。
- 判断：[商业模式是否稳健、是否有新增长引擎。]

## 2. 市场占额 (Market Share)
- 所在赛道：[赛道名] 全球规模与增速。
- 份额：本公司约 X%（来源），同比 [升/降]；最近对手 [对手] 约 Y%。
- 判断：[份额趋势与护城河信号。]

## 3. 发展前景 (Growth Prospects)
- 2-3 年主线：[如 AI 资本开支、云迁移、换机周期]。
- 上行驱动：[列出 1-2 个]。
- 下行风险：[列出 1-2 个]。
- 判断：[增长确定性高/中/低。]

## 4. 技术壁垒 (Technology Moat)
- 壁垒类型：规模效应 / 网络效应 / 专利与 IP / 软硬一体 / 数据飞轮（可多选）。
- 证据：[最新产品、R&D 投入、生态锁定、供应链控制等]。
- 判断：[壁垒是否可被侵蚀，时间窗口。]

## 5. 财报表现 (Financial Reports)
- 最新季：营收 [X]（同比 [+/-]%）、净利润 [X]、毛利率 [X]%、自由现金流 [X]。
- 对比预期：营收/利润 [beat / miss] 共识。
- 资产负债表：现金 [X]、净债务 [X]、回购/分红 [X]。
- 判断：[财务健康度与可持续性。]

## 6. 股价走势 (Stock Price Trend)
- 近期表现：[区间涨跌幅]；52 周区间 [低-高]；当前约 [价格]。
- 催化/压制： [近期关键事件]。
- 共识：分析师目标价中位数 [X]，评级分布 [X 买 / Y 持 / Z 卖]。
- 判断：[仅作背景，非投资建议。]

## 主要风险 (Key Risks)
- [监管 / 竞争 / 估值 / 宏观 / 单一客户依赖 等，列 3-5 条。]

## 数据来源与日期 (Sources & Dates)
- [来源 1 名称 + URL]（抓取日期）
- [来源 2 名称 + URL]（抓取日期）
```

## Source Checklist (prefer primary)

- SEC filings: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company= [TICKER]
- Company investor relations: [ir.company.com] → Quarterly Results / SEC Filings
- Market share: IDC, Canalys, StatCounter, Gartner, Omdia (segment-specific)
- Stock & estimates: Nasdaq, Reuters, the company IR page, analyst consensus aggregates
- News catalysts: Reuters, Bloomberg, CNBC, The Information (verify date)

## Worked Example (skeleton only — fill with live data at run time)

Company: NVIDIA (NVDA)
- Business model: 数据中心 GPU + 网络 + 软件栈；数据中心营收占比已超 80%，毛利率高位。
- Market share: 数据中心 AI 加速卡全球份额约 80%+（vs AMD / 自研 ASIC）。
- Prospects: 云厂与主权 AI 资本开支上行；风险在供给与对手自研。
- Moat: CUDA 软件生态 + 制程与互联领先 + 客户迁移成本极高。
- Financials: 营收同比高增，毛利率 ~70%+，自由现金流强劲（填最新季）。
- Stock: 一年内大幅上行后高位震荡；估值反映高预期（填最新价与区间）。
- Risks: 估值、地缘政治（对华出口）、客户自研芯片、需求节奏。
- Sources: SEC 10-K/Q, NVIDIA IR, Reuters/Bloomberg, IDC（填 URL 与日期）。
```
