# 旅游攻略助手

性价比优先的智能旅行规划 Agent。

## 快速开始

### 使用 Agent

```
@旅游攻略助手 我想去云南，从深圳出发，6月20日到30日，三个人，预算人均8000，喜欢吃和自然风光
```

Agent 会：
1. 澄清需求（确认偏好、特殊要求）
2. 多源比价（机票、酒店、景点）
3. 生成 HTML 行程书

### 输出示例

生成文件：`云南滇南-2026-08-26-行程书.html`

包含：
- 🗺️ 总览地图（Leaflet 交互地图）
- 🚉 大交通（去程/回程候选，附订票链接）
- 🏨 住宿候选（2-3个推荐，附预订链接）
- 📅 每日行程（时间轴+POI详情+体力指数）
- 💰 预算明细（饼图+表格+超支建议）
- ⚠️ 风险提示（天气、节假日、防坑提示）
- 📕 小红书参考
- 🎒 行前清单

## 核心逻辑

```
推荐指数 = (吸引力 × 0.4) + (便宜 × 0.3) + (便利 × 0.3)

好吃标准 = 人均 < 50元 AND 味道好
动线控制 = 单日移动距离 3-5km
景点密度 = 每天 ≤ 2个付费景点
```

## 性价比优先级

1. **大交通**（特价机票占比最大）
2. **住宿**
3. **吃**

## 文件结构

```
travel-planner/
├── SKILL.md          # 技能定义、工作流、数据模型
├── AGENTS.md         # Agent 启动流程
├── agent.md          # 身份定义
├── soul.md           # 价值观、决策逻辑
├── README.md         # 本文件
└── assets/
    └── template.html # HTML 行程书模板
```

## 数据模型

行程书基于数据驱动模板，只需填充 `DATA` 对象：

```javascript
const DATA = {
  meta: { destination, days_count, date_start, date_end, people, budget_total, confidence },
  transport: { outbound, inbound, intra_tips },
  hotels: [...],
  days: [...],
  budget: { items, note, tradeoffs },
  risk: { weather, holiday, scams, emergency },
  xhs: { available, keywords, notes },
  completeness: { enabled, tip },
  checklist: [...]
};
```

详见 `SKILL.md` 数据模型速查部分。

## 技术说明

- 纯前端 HTML，无需后端
- CDN 依赖：Leaflet（地图）、Chart.js（图表）
- 浏览器即可打开，手机/电脑自适应
- 地图瓦片四级回退：高德 → 高德卫星 → 腾讯 → OSM

## 更新日志

- 2026-08-23: 初始版本，基于云南滇南行程书模板构建
