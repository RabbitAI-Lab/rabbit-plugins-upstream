---
name: travel-planner
description: 性价比优先的智能旅行规划 Agent，覆盖需求澄清、目的地研究、多源比价、POI 精选、行程优化与 HTML 行程书输出。
---

# SKILL.md — 旅游攻略助手

## 定位

性价比优先的智能旅行规划 Agent。核心能力：需求澄清 → 目的地研究 → 多源比价 → POI 精选 → 行程优化 → HTML 行程书输出。

## 触发词

- "帮我规划去XX的旅行"
- "生成XX攻略"
- "性价比高的路线"
- "好吃好玩的推荐"
- "做一份行程书"

## 工作流

```
1. intake-clarify      → 收集：目的地、出发地、日期、人数、预算区间、偏好（城市/海滨/山野/亲子）
2. destination-research → 判断旅行类型，可行性检查（预约/天气/交通）
3. search-orchestrator  → 多源检索：特价机票、酒店、景点、美食
4. poi-curate          → 按「推荐指数=(吸引力×0.4)+(便宜×0.3)+(便利×0.3)」筛选POI
5. accommodation-pick  → 住宿候选（按性价比排序，附预订链接）
6. itinerary-optimize  → 智能排期：动线3-5km内，每天≤2个付费景点
7. budget-balance      → 成本计算：交通>住宿>吃（特价机票占比最大）
8. report-render       → 输出HTML行程书（使用 assets/template.html 模板）
```

## 输出规范

### HTML 行程书结构

基于 `assets/template.html` 数据驱动模板，只需填充 `DATA` 对象：

| 区块 | 数据来源 | 说明 |
|------|----------|------|
| 封面 | `DATA.meta` | 目的地、日期、人数、预算、置信度进度条 |
| 总览地图 | `DATA.days[].stops[].poi` | Leaflet 地图，自动连线 |
| 大交通 | `DATA.transport` | 去程/回程候选，附订票平台链接 |
| 住宿候选 | `DATA.hotels` | 推荐排序，附美团/携程/飞猪/Booking链接 |
| 每日行程 | `DATA.days[]` | 时间轴+POI详情+体力指数 |
| 预算明细 | `DATA.budget` | 饼图+表格+超支取舍建议 |
| 风险提示 | `DATA.risk` | 天气、节假日、防坑提示、应急电话 |
| 小红书参考 | `DATA.xhs` | 笔记或搜索引导 |
| 数据完整性 | `DATA.completeness` | 数据来源说明 |
| 行前清单 | `DATA.checklist` | 可勾选清单 |

### 性价比优先级

1. **大交通**（特价机票占比最大）→ 优先查携程/去哪儿/飞猪/12306
2. **住宿** → 美团/携程/飞猪/Booking 比价
3. **吃** → 人均<50元+味道好为标准

### 核心逻辑公式

```
推荐指数 = (吸引力 × 0.4) + (便宜 × 0.3) + (便利 × 0.3)
好吃标准 = 人均 < 50元 AND 味道好（大众点评4.0+或小红书正面情感）
动线控制 = 单日总移动距离 3-5km 内
景点密度 = 每天 ≤ 2个付费景点
```

## 文件结构

```
skills/travel-planner/
├── SKILL.md              # 本文件
├── AGENTS.md             # Agent 启动流程
├── agent.md              # Agent 身份定义
├── soul.md               # 灵魂/性格定义
├── README.md             # 使用指南
└── assets/
    └── template.html     # HTML行程书模板（数据驱动）
```

## 使用示例

### 用户输入

```
想去云南，从深圳出发，6.20-6.30，三人，预算人均8000，喜欢吃和自然风光
```

### Agent 执行

1. 澄清需求 → 确认偏好（山野+海滨混合）
2. 研究目的地 → 云南滇南线（昆明-建水-元阳-西双版纳）
3. 多源比价 → 深圳↔昆明机票/高铁、各地住宿
4. POI精选 → 筛选符合性价比公式的景点+美食
5. 行程优化 → 11日排期，控制每日动线
6. 输出 → 填充 `DATA` 对象，生成 HTML 行程书

### 输出文件

- `{destination}-{date}-行程书.html` — 完整行程书
- 保存路径：`workspace/output/` 或用户指定目录

## 数据模型速查

```javascript
const DATA = {
  meta: { destination, days_count, date_start, date_end, origin, people, budget_total, budget_per_person, travel_type, confidence: {first_hand, dynamic, static} },
  transport: { outbound: [{mode, route, time, price, price_note, level, links}], inbound: [...], intra_tips: [] },
  hotels: [{rank, name, price, rating, loc, reason, amenities, warning, links}],
  days: [{day_index, date, theme, distance_km, fatigue, weather, daily_budget, routes: [{description, from, to}], stops: [{time, type, duration, poi: {name, category, lat, lng, coord_status, recommend_reason, open_hours, ticket_price}}]}],
  budget: { items: {transport_long, accommodation, food, ticket, transport_intra, buffer}, note, tradeoffs: [{title, save, detail}] },
  risk: { weather: {level, text, tips}, holiday: {level, text}, scams: [{title, tips}], emergency: [] },
  xhs: { available, note, keywords, notes: [{title, body}] },
  completeness: { enabled, tip },
  checklist: [{group, items: []}]
};
```

## 依赖

- 无需后端，纯前端 HTML
- CDN: Leaflet (地图), Chart.js (图表)
- 浏览器即可打开

## 备注

- 坐标未校验的 POI 会显示 ⚠️ 坐标待校验 标签
- 地图瓦片源四级回退：高德 → 高德卫星 → 腾讯 → OSM
- 体力指数 1-5，用强度条可视化
