# Open API · 资讯与 AI 点评

> 根地址、`API_BASE`、统一响应与鉴权见 [api.md](./api.md)。
> 本组接口**与交易环境无关**：`sim` / `live` 返回同一份市场资讯，但请求头 `X-Trading-Env` 仍需按规范带上。

## 1. 资讯列表

```
GET /open/v1/news/list?page=1&pageSize=10&goodsName=
Headers: Authorization: Bearer ${SLZQ_OPENCLAW_API_KEY}
         X-Trading-Env: sim|live
```

**Query**

| 参数 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `page` | 否 | 1 | 页码，从 1 开始 |
| `pageSize` | 否 | 10 | 每页条数 |
| `goodsName` | 否 | — | 按期货品种筛选。**精确匹配**，见下方警告 |

> ⚠️ **`goodsName` 是精确匹配，不是模糊搜索。** 服务端按逗号分隔项逐一比对，传「银」**不会**命中「白银」，传「螺纹」**不会**命中「螺纹钢」。
> 要按品种筛就传完整品种名；拿不准就先调 `GET /open/v1/catalog/goods` 看服务端用的是哪个名字，不要自己猜。
> 该参数**仅在服务端配置 `news.source` 为 `wscn` 或 `tushare` 时生效**；数据源是 `jin10` 时传了会被忽略——筛不出来不代表没有资讯，别据此断言"该品种无新闻"。

**响应 `data`（统一分页形状，与 `/catalog/goods` 一致）**

| 字段 | 类型 | 说明 |
|------|------|------|
| `list` | array | 资讯数组，见下 |
| `currentPage` / `pageSize` | int | 当前页 / 每页条数 |
| `totalCount` / `totalPage` | int | 总条数 / 总页数 |

**`list[]` 每条：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | number | 本地主键 |
| `flashId` | string | 数据源侧的快讯 ID |
| `publishTime` | string | 发布时间 |
| `type` | int | 资讯类型（随数据源而异） |
| `important` | int | 重要程度标记，非 0 表示重点 |
| `goods` | string | 关联品种，**逗号分隔**（如 `白银,黄金`） |
| `dataJson` | string | **正文与标题的 JSON 字符串**，需二次 `JSON.parse` |
| `tagsJson` / `channelJson` / `remarkJson` | string | 标签 / 频道 / 备注，同样是 JSON 字符串 |
| `aiAnalysisJson` | string | 该条资讯的 AI 分析，JSON 字符串；为空表示还没分析 |

> **`*Json` 字段是字符串不是对象**，直接当对象取字段会拿到 `undefined`。解析失败要当作"该字段缺失"处理，不要整条丢弃。

## 2. 资讯 AI 点评

```
GET /open/v1/news/ai-analysis?page=1
```

**Query**

| 参数 | 必填 | 默认 | 说明 |
|------|------|------|------|
| `page` | 否 | 1 | 页码，从 1 开始 |

> **每页固定 10 条**，服务端不接受 `pageSize`，传了也没用。

**`list[]` 每条：**

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | number | 分析记录 ID |
| `newsId` | number | 对应的资讯 ID（可与上一接口的 `id` 关联） |
| `newsDataJson` | string | 被分析的资讯原文快照，JSON 字符串 |
| `analysisJson` | string | **AI 分析结果**，JSON 字符串，含关联品种、影响方向等结构化字段 |
| `createTime` / `updateTime` | string | 生成 / 更新时间 |

## 3. 该用哪个

| 你要做的事 | 用哪个 |
|------------|--------|
| 给用户播报"今天有什么消息" | `/news/list` |
| 解释某个品种为什么涨跌 / 找驱动因素 | **先** `/news/ai-analysis`，`analysisJson` 已经把品种与影响方向结构化了，比自己读原文省轮次 |
| 只关心某个品种 | `/news/list` 带 `goodsName`（注意精确匹配） |

## 4. 使用约束

- 资讯是**公开市场信息**，可作判断材料。你可以据此形成自己的多空与价位判断；不要把单条 AI 点评原文当成必须执行的操作指令。
- `aiAnalysisJson` / `analysisJson` 是模型生成的，**可能过时或有误**。用它做归因、形成建议可以；真正下单必须有用户的明确指令。
- 不要因为某品种查不到资讯就断言"没有消息面影响"，这只说明当前数据源没抓到。
