# M1 数据格式规范文档 (Data Contract)

> **版本**: v3.1
> **更新日期**: 2026-05-20
> **用途**: 定义 M1 JSON 数据的完整格式规范，确保上下游模块数据契约一致性

---

## 零、Transform 操作指南（新增）- 使用必读⭐

### 0.1 核心转换规则

#### 规则1: 平台名称映射（必须）
**问题**: Agent 输出的平台名称带有分类前缀，M1 需要简化名称

**映射字典**:
```python
PLATFORM_MAPPING = {
    "视频-抖音": "抖音",
    "视频-哔哩哔哩": "哔哩哔哩",
    "视频-快手": "快手",
    "晒单-小红书": "小红书",
    "论坛-虎扑（论坛）": "虎扑",
    "问答-知乎": "知乎",
    "微博": "微博",
    "微博评论": "微博评论",
    "新闻": "新闻",
    "微信": "微信"
}
```
应用场景:

P3 平台分布计算
P4 渠道热度值提取
所有涉及平台名称的字段

#### 规则2: trend 数据按日期聚合（必须）⭐

问题: main_trend/slot1_trend/slot2_trend 返回的是 日期×平台 的多维数组

| api.xx 字段 | 数据形态 | Transform操作 |
|---|---|---|
| `main_trend` / `slot1_trend` / `slot2_trend` | **日期×多平台多行**（N天×P平台=N×P条，平台数不固定） | **必须按日期group by加总**声量/互动数 → 得到N个值的数组 |
| `dy_trend` / `wb_trend` | 单平台，每天1条 | 直接取声量/互动数数组，无需聚合 |
| `main_platform` / `main_platform_yoy` / `slot1_platform` / `slot2_platform` | 按平台分行（每行一个平台） | 映射平台名 → 取声量/互动数值 |
| `main_overview`| **list类型，长度=1**（非dict） | 取值用 `v[0]['声量']`，不是 `v['声量']` |
| `slot*_overview`/`*_overview_yoy`| 平台维度 | 核验：对所有平台求和 ❌ 只取第一条 | ✅ sum(所有记录) |


影响范围:

P2: vol_data, inter_data, date_labels
P5: dy_vol_data, dy_inter_data, dy_date_labels
P6: wb_vol_data, wb_inter_data, wb_date_labels
P7: main_heat_data, slot_heat_data, date_labels
P8: main_heat_data, slot_heat_data, date_labels
注意: dy_trend 和 wb_trend 是单平台数据，每天1条，无需聚合，直接提取即可




## 一、文档说明

本文档定义了社媒监测报告 PPT 生成流程中 M1 阶段输出的 JSON 数据格式规范。

**数据契约原则**:
1. **明确性**: 所有字段的类型、格式、取值范围必须明确定义
2. **完整性**: 必需字段不得缺失，数组长度必须符合要求
3. **一致性**: 相关字段之间的数据必须保持逻辑一致
4. **可验证性**: 所有规则都可通过自动化脚本验证


---

## 二、顶层结构

M1 JSON 必须包含以下顶层字段：

```json
{
    "meta": { /* 元数据对象 */ },
    "P2": { /* P2页面数据对象 */ },
    "P3": { /* P3页面数据对象 */ },
    "P4": { /* P4页面数据对象 */ },
    "P5": { /* P5页面数据对象 */ },
    "P6": { /* P6页面数据对象（微博）*/ },
    "P7": { /* P7页面数据对象（竞品Slot1）*/ },
    "P8": { /* P8页面数据对象（竞品Slot2）*/ }
}
```

**验证规则**:
- ✅ 必须包含所有 8 个顶层字段 (meta, P2-P8)
- ✅ 每个字段的值必须是对象类型 (object)
- ❌ 不允许缺失任何顶层字段

---

## 三、meta 元数据规范

### 3.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 |
|--------|------|------|----------|------|
| `main_event` | string | ✅ | 非空字符串 | 主赛事名称 (如 "LPL") |
| `report_stage` | string | ✅ | 非空字符串 | 赛事阶段 (如 "启点赛") |
| `main_time_range` | string | ✅ | `YYYY-MM-DD ~ YYYY-MM-DD` | 主赛事时间范围 |
| `slot1_time_range` | string | ✅ | 同上 | 竞品1时间范围 |
| `slot2_time_range` | string | ✅ | 同上 | 竞品2时间范围 |
| `yoy_time_range` | string | ✅ | 同上 | 同比时间范围 |
| `generated_at` | string | ✅ | `YYYY-MM-DD` | 数据生成时间 |
| `playoff_start` | string | ✅ | `YYYY-MM-DD` | 淘汰赛开始日期，由用户运行时输入，透传至HTML渲染层，与MCP取数无关 |

### 3.2 验证规则

```python
# 时间范围格式验证
pattern = r'^\d{4}-\d{2}-\d{2} ~ \d{4}-\d{2}-\d{2}$'

# 生成时间格式验证
pattern = r'^\d{4}-\d{2}-\d{2}$'
```

---

## 四、P2 页面数据规范

### 4.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范 |
|--------|------|------|----------|------|------|
| `total_volume` | string | ✅ | `整数K` 或 `整数M` | 总声量 (如 "107K") |`api.main_overview.声量`|
| `total_interaction` | string | ✅ | 同上 | 总互动量 (如 "10M") |`api.main_overview.互动数`|
| `heat_index` | string | ✅ | 同上 | 热度指数 (如 "11M") |`total_volume`×49.704 + `total_interaction`×0.542|
| `yoy_volume` | string | ✅ | 同上 | 去年总声量(如 "100K") |`api.main_overview_yoy.声量`|
| `yoy_interaction` | string | ✅ | 同上 | 去年总互动量(如 "9M") |`api.main_overview_yoy.互动数`|
| `yoy_heat_index` | string | ✅ | 同上 | 去年总热度 (如 "90K")|`yoy_volume`×49.704 + `yoy_interaction`×0.542|
| `time_range_label` | string | ✅ | `数据时间覆盖：YYYY.M.D - YYYY.M.D` | 时间范围标签 |
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** |"2026`main_event``report_stage`总声量为`total_volume`，互动量为`total_interaction`，热度指数为`heat_index`。"|
 |
| `vol_data` | array[number] | ✅ | 长度 ≥ 5 | 声量数据数组 |`api.main_trend.声量`|
| `inter_data` | array[number] | ✅ | 长度 ≥ 5 | 互动量数据数组 |`api.main_trend.互动数`|
| `date_labels` | array[string] | ✅ | 长度 ≥ 5 | 日期标签数组 (如 ["2.1", "2.2"]) | 对应日期 |
| `peak_events` | array[object] | ✅ | 长度 = 6 | 峰值事件数组 | 见下方peak_events对象规范 |



### 4.2 peak_events 对象规范

每个峰值事件对象必须包含：

| 字段名 | 类型 | 必需 | 格式要求 | 说明 |
|--------|------|------|----------|------|
| `event_id` | string | ✅ | `evt_001` ~ `evt_006` | 事件唯一标识 |
| `idx` | number | ✅ | 0 ≤ idx < len(vol_data) | 数据数组索引 |
| `date_label` | string | ✅ | `M月D日` | 日期标签 (如 "2月1日") |
| `text` | string | ✅ | 日期 + 高点占位 | 日期 + 高点占位 |



### 4.3 验证规则

```python
# 数组长度一致性
assert len(vol_data) == len(inter_data) == len(date_labels)

# peak_events 必须恰好 6 个
assert len(peak_events) == 6

# event_id 必须唯一且按顺序
event_ids = [e['event_id'] for e in peak_events]
assert event_ids == ['evt_001', 'evt_002', 'evt_003', 'evt_004', 'evt_005', 'evt_006']

# idx 必须在有效范围内
for event in peak_events:
    assert 0 <= event['idx'] < len(vol_data)
```


---

## 五、P3 页面数据规范

### 5.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范 |
|--------|------|------|----------|------|------|
| `yoy_volume_change` | string | ✅ | `+整数%` 或 `-整数%` ||基于 `api.main_overview.声量` 和 `api.main_overview_yoy.声量` 原始数值计算：`(声量_now - 声量_yoy) / 声量_yoy × 100%`|
| `yoy_interaction_change` | string | ✅ | 同上 | |基于 `api.main_overview.互动数` 和 `api.main_overview_yoy.互动数` 原始数值计算：`(互动数_now - 互动数_yoy) / 互动数_yoy × 100%`|
| `yoy_heat_change` | string | ✅ | 同上 | |基于 `api.*` 原始数值先算热度：`heat_now = 声量_now×49.704 + 互动数_now×0.542`，`heat_yoy = 声量_yoy×49.704 + 互动数_yoy×0.542`，再计算 `(heat_now - heat_yoy) / heat_yoy × 100%`|
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** |"与去年`report_stage`相比，声量提升了`yoy_volume_change`，互动量提升了`yoy_interaction_change`，热度值提升了`yoy_heat_change`。"|
| `platform_dist` | object | ✅ | 见下方 | 当期平台分布 |见下方platform_dist对象规范 |

### 5.2 platform_dist 对象规范
#### 5.2.1 平台分布占比计算
> ⚠️ **平台分布规则（P3 vs P7/P8 不同）**：
> - **P3（主赛事）**：固定 5 平台：微博/抖音/B站/小红书/其他
>   「其他」= 全部剩余平台加总（含快手、新闻、微信、知乎、虎扑等）
> - **P7/P8（竞品）**：固定 6 平台：微博/抖音/B站/小红书/快手/其他
>   快手从「其他」中单独拆出，「其他」= 快手以外的剩余平台加总

**字段**: platform_dist

**公式**:平台占比 = (当期平台数值 / 当期所有平台数值总和) × 100%

**数据来源**:

当期分平台: `api.main_platform`（数组，包含各平台的声量/互动量）
当期所有平台数据总和：`api.main_overview`

**平台映射规则（5平台）**:

微博 → 微博
视频-抖音 → 抖音
视频-哔哩哔哩 → B站
晒单-小红书 → 小红书
其他所有平台 → 其他（包含快手、新闻、微信、知乎、虎扑等）

**计算步骤**:
1. 从API数组中提取各平台数据
2. 应用平台名称映射规则，将相同平台的数据合并
3. 平台总和从`api.main_overview`中提取
4. 计算各平台占比 = 平台数值 / 平台总和 × 100%
5. 四舍五入取整
6. 确保总和=100%（如有偏差，调整最大占比平台）

**热度占比计算**:
先计算各平台热度值 = 平台声量 × 49.704 + 平台互动量 × 0.542
再按上述步骤计算占比




#### 5.2.2 数据产出要求

```json
{
    "volume": {
        "微博": number,   // 0-100 的百分比数值
        "抖音": number,
        "B站": number,
        "小红书": number,
        "其他": number    // P3专用：含快手在内的所有剩余平台
    },
    "interaction": { /* 同上结构 */ },
    "heat": { /* 同上结构 */ }
}
```


### 5.3 验证规则

```python
# P3 平台名称必须完整（5平台）
required_platforms = ["微博", "抖音", "B站", "小红书", "其他"]

for metric in ["volume", "interaction", "heat"]:
    platforms = list(platform_dist[metric].keys())
    assert set(platforms) == set(required_platforms)

    # 百分比总和应接近 100 (允许 ±1 误差)
    total = sum(platform_dist[metric].values())
    assert 99 <= total <= 101
```

---

## 六、P4 页面数据规范

### 6.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 |来源与计算规范 |
|--------|------|------|----------|------|------|
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** |"从分渠道数据来看，抖音增长率为`channel_growth[抖音].growth_rate`%，微博增长率为`channel_growth[微博].growth_rate`%"|
| `channel_heat` | array[object] | ✅ | 长度 = 4 | 渠道热度值数据 |见下方channel_heat对象规范 |
| `channel_growth` | array[object] | ✅ | 长度 = 4 | 渠道增长率数据 |见下方channel_growth对象规范 |


### 6.2 channel_heat 计算规范

数据来源：
- 当期：`api.main_platform`（数组，每项含 "平台"/"声量"/"互动数"）
- 同比：`api.main_platform_yoy`（结构相同）

平台名称映射（API返回 → channel字段）：
- "微博" → "微博"
- "视频-抖音" → "抖音"
- "视频-哔哩哔哩" → "B站"
- "晒单-小红书" → "小红书"

计算步骤（对4个平台分别执行）：
1. 从 api.main_platform 数组中找到 "平台" == 对应API名称 的那条记录
2. heat_now = 该记录["声量"] × 49.704 + 该记录["互动数"] × 0.542
3. 从 api.main_platform_yoy 数组中同样方式找到对应记录
4. heat_yoy = 该记录["声量"] × 49.704 + 该记录["互动数"] × 0.542

示例（微博）：
输入：{"平台": "微博", "声量": 118689, "互动数": 7538431}
heat_now = 118689 × 49.704 + 7538431 × 0.542 = 5900,xxx + 4,087,xxx ≈ 9.99M

```json
{
    "channel": string,   // "微博" | "抖音" | "B站" | "小红书"
    "heat_now": number,  // 当期热度值 (正数)
    "heat_yoy": number   // yoy期热度值 (正数)
}
```


### 6.3 channel_growth 对象规范

数据来源：直接复用 channel_heat 中已计算的 heat_now 和 heat_yoy，不重新取 API 数据。

计算步骤（对4个平台分别执行）：
1. 从 channel_heat 中取该平台的 heat_now 和 heat_yoy
2. growth_rate = round((heat_now - heat_yoy) / heat_yoy × 100)（取整，不保留小数）

示例（微博）：
heat_now = 9,999,000, heat_yoy = 8,500,000
growth_rate = round((9999000 - 8500000) / 8500000 × 100) = round(17.6) = 18
→ 输出：{"channel": "微博", "growth_rate": 18}

⚠️ 注意：
- growth_rate 是纯数字（number），不带 % 符号
- 可为负数（同比下降时）
- heat_yoy 为 0 时跳过该平台并报错，不做除法


```json
{
    "channel": string,   // "微博" | "抖音" | "B站" | "小红书"
    "growth_rate": number  // 增长率数值 (可为负数)
}
```

**计算基准说明**:
- **必须基于热度值计算**: `growth_rate = (heat_now - heat_yoy) / heat_yoy × 100%`
- ⚠️ **注意**: 不是基于互动数或声量，而是严格以各重点平台的**热度值**为基准进行同比计算



### 6.4 验证规则

```python
# channel_growth 验证
assert len(channel_growth) == 4
required_channels = ["微博", "抖音", "B站", "小红书"]
channels = [item['channel'] for item in channel_growth]
assert set(channels) == set(required_channels)

# channel_heat 验证
assert len(channel_heat) == 4
heat_channels = [item['channel'] for item in channel_heat]
assert set(heat_channels) == set(required_channels)

for item in channel_heat:
    assert item['heat_now'] >= 0
    assert item['heat_yoy'] >= 0

# 渠道顺序一致性
assert channels == heat_channels
```

---

## 七、P5 页面数据规范（抖音）

### 7.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范 |
|--------|------|------|----------|------|------|
| `dy_total_volume` | string | ✅ | `整数K` 或 `整数M` | 抖音总声量 |`api.dy_overview.声量`|
| `dy_total_interaction` | string | ✅ | 同上 | 抖音总互动量 |`api.dy_overview.互动数`|
| `dy_heat_index` | string | ✅ | 同上 | 抖音热度指数 |`dy_total_volume`×49.704 + `dy_total_interaction`×0.542|
| `dy_yoy_volume` | string | ✅ | 同上 | 去年抖音声量 |`api.dy_overview_yoy.声量`|
| `dy_yoy_interaction` | string | ✅ | 同上 | 去年抖音互动量 |`api.dy_overview_yoy.互动数`|
| `dy_yoy_heat_index` | string | ✅ | 同上 | 去年抖音热度 |`dy_yoy_volume`×49.704 + `dy_yoy_interaction`×0.542|
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** | 抖音整体热度`dy_heat_index`，声量`dy_total_volume`，互动量`dy_total_interaction`|
| `dy_vol_data` | array[number] | ✅ | 长度 ≥ 5 | 声量数据数组 |`api.dy_trend.声量`|
| `dy_inter_data` | array[number] | ✅ | 长度 ≥ 5 | 互动量数据数组 |`api.dy_trend.互动数`|
| `dy_date_labels` | array[string] | ✅ | 长度 ≥ 5 | 日期标签数组 |对应日期 |
| `dy_peak_events` | array[object] | ✅ | 长度 = 6 | 峰值事件数组 |见下方dy_peak_events对象规范 |

### 7.2 dy_peak_events 对象规范

```json
{
    "event_id": string,   // "evt_p5_001" ~ "evt_p5_006"
    "idx": number,        // 0 ≤ idx < len(dy_vol_data)
    "date_label": string, // "M月D日"
    "text": string        // 占位阶段填"[高点事件待确认]"，终稿阶段 8-50字符真实描述
}
```

### 7.3 验证规则

```python
# 数组长度一致性
assert len(dy_vol_data) == len(dy_inter_data) == len(dy_date_labels)

# peak_events 必须恰好 6 个
assert len(dy_peak_events) == 6

# event_id 格式验证
for event in dy_peak_events:
    assert re.match(r'^evt_p5_\d{3}$', event['event_id'])
```

---

## 八、P6 页面数据规范（微博）

### 8.1 字段定义

与 P5 结构相同，字段名替换为 `wb` 相关：

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范|
|--------|------|------|----------|------|------|
| `wb_total_volume` | string | ✅ | `整数K` 或 `整数M` | 微博总声量 |
| `wb_total_interaction` | string | ✅ | 同上 | 微博总互动量 |
| `wb_heat_index` | string | ✅ | 同上 | 微博热度指数 |
| `wb_yoy_volume` | string | ✅ | 同上 | 去年微博声量 |
| `wb_yoy_interaction` | string | ✅ | 同上 | 去年微博互动量 |
| `wb_yoy_heat_index` | string | ✅ | 同上 | 去年微博热度 |
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** | 微博整体热度`wb_heat_index`，声量`wb_total_volume`，互动量`wb_total_interaction` |
| `wb_vol_data` | array[number] | ✅ | 长度 ≥ 5 | 声量数据数组 |
| `wb_inter_data` | array[number] | ✅ | 长度 ≥ 5 | 互动量数据数组 |
| `wb_date_labels` | array[string] | ✅ | 长度 ≥ 5 | 日期标签数组 |
| `wb_peak_events` | array[object] | ✅ | 长度 = 6 | 峰值事件数组 |

### 8.2 wb_peak_events 对象规范

```json
{
    "event_id": string,   // "evt_p6_001" ~ "evt_p6_006"
    "idx": number,        // 0 ≤ idx < len(wb_vol_data)
    "date_label": string, // "M月D日"
    "text": string        // 占位阶段填"[高点事件待确认]"，终稿阶段 8-50字符真实描述
}
```

### 8.3 验证规则

```python
# 数组长度一致性
assert len(wb_vol_data) == len(wb_inter_data) == len(wb_date_labels)

# peak_events 必须恰好 6 个
assert len(wb_peak_events) == 6

# event_id 格式验证
for event in wb_peak_events:
    assert re.match(r'^evt_p6_\d{3}$', event['event_id'])
```

---

## 九、P7 页面数据规范（竞品Slot1）

### 9.1 字段定义

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范|
|--------|------|------|----------|------|------|
| `slot` | string | ✅ | `"compare_slot_1"` | 固定值 |
| `slot_event_name` | string | ✅ | 非空字符串 | 竞品1名称 (如 "KPL") |
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** | `main_event`热度值为`main_heat_data`，`slot_event_name`热度值为`slot1_heat_data`|
| `main_summary` | object | ✅ | 见下方 | 主赛事汇总数据 |`api.main_overview`|
| `slot1_summary` | object | ✅ | 见下方 | 竞品1汇总数据 |`api.slot1_overview`|
| `slot1_platform_dist` | object | ✅ | 见下方（6平台）三大指标占比 | 竞品1平台分布 | 见下方 slot1_platform_dist 对象规范|
| `main_heat_data` | array[number] | ✅ | 长度 ≥ 5 | `api.main_trend`数组计算热度 | 声量×49.704 + 互动数×0.542|
| `slot1_heat_data` | array[number] | ✅ | 长度 ≥ 5 | `slot1_trend`数组计算热度 |声量×49.704 + 互动数×0.542|
| `date_labels` | array[string] | ✅ | 长度 ≥ 5 | 日期标签数组 |对应日期|
| `main_peaks` | array[object] | ✅ | 长度 = 3 | 主赛事前三峰值事件 |
| `slot1_peaks` | array[object] | ✅ | 长度 = 3 | 竞品1峰值事件 |

### 9.2 slot1_platform_dist 对象规范

#### 9.2.1 平台分布占比计算

> ⚠️ 竞品页平台分布为 **6 平台**，快手单独列出，不归入「其他」。
**字段**: slot1_platform_dist

**公式**: 平台占比 = (当期平台数值 / 当期所有平台数值总和) × 100%

**平台映射规则（6平台）**:

微博 → 微博
视频-抖音 → 抖音
视频-哔哩哔哩 → B站
晒单-小红书 → 小红书
视频-快手 → 快手（竞品页专属，单独拆出）
其他所有平台 → 其他（快手以外的剩余平台）


**计算步骤**:
1. 从API数组中提取各平台数据
2. 应用平台名称映射规则，将相同平台的数据合并
3. 平台总和从`api.slot1_overview` 中提取
4. 计算各平台占比 = 平台数值 / 平台总和 × 100%
5. 四舍五入取整
6. 确保总和=100%（如有偏差，调整最大占比平台）

**热度占比计算**:
先计算各平台热度值 = 平台声量 × 49.704 + 平台互动量 × 0.542
再按上述步骤计算占比



#### 9.2.2 数据输出规范
```json
{
    "volume": {
        "微博": number,
        "抖音": number,
        "B站": number,
        "小红书": number,
        "快手": number,   // 竞品页专属，单独拆出
        "其他": number    // 快手以外的剩余平台加总
    },
    "interaction": { /* 同上结构 */ },
    "heat": { /* 同上结构 */ }
}
```

```python
# P7/P8 竞品平台名称必须完整（6平台）
required_platforms_slot = ["微博", "抖音", "B站", "小红书", "快手", "其他"]

for metric in ["volume", "interaction", "heat"]:
    platforms = list(slot_platform_dist[metric].keys())
    assert set(platforms) == set(required_platforms_slot)
    total = sum(slot_platform_dist[metric].values())
    assert 99 <= total <= 101
```

### 9.3 summary 对象规范

```json
{
    "volume": string,      // "整数K" 或 "整数M"
    "interaction": string, // 同上
    "heat_index": string   // 同上
}
```

### 9.3 验证规则

```python
# slot 必须是固定值
assert slot == "compare_slot_1"

# 数组长度一致性
assert len(main_heat_data) == len(slot1_heat_data) == len(date_labels)

# main_peaks 必须恰好 3 个，event_id 引用 P2 的事件
assert len(main_peaks) == 3
for event in main_peaks:
    assert re.match(r'^evt_00[1-6]$', event['event_id'])

# slot1_peaks 必须恰好 3 个
assert len(slot1_peaks) == 3
```

---

## 十、P8 页面数据规范（竞品Slot2）

### 10.1 字段定义

与 P7 结构相同，字段名替换为 `slot2` 相关：

| 字段名 | 类型 | 必需 | 格式要求 | 说明 | 来源与计算规范|
|--------|------|------|----------|------|------|
| `slot` | string | ✅ | `"compare_slot_2"` | 固定值 |
| `slot_event_name` | string | ✅ | 非空字符串 | 竞品2名称 |
| `summary` | string | ✅ | 非空字符串 | 页面总结，**严格按照来源于计算规范，禁止发散** |`main_event`热度值为`main_heat_data`，`slot_event_name`热度值为`slot2_heat_data` |
| `main_summary` | object | ✅ | 同P7 | 主赛事汇总数据 |`api.main_overview`|
| `slot2_summary` | object | ✅ | 同P7 | 竞品2汇总数据 |`api.slot2_overview`|
| `slot2_platform_dist` | object | ✅ | 见P7（6平台） | 竞品2平台分布 |参考 slot1_platform_dist 对象规范|
| `main_heat_data` | array[number] | ✅ | 长度 ≥ 5 | P7一致| 声量×49.704 + 互动数×0.542|
| `slot2_heat_data` | array[number] | ✅ | 长度 ≥ 5 | `slot1_trend`数组计算热度 |声量×49.704 + 互动数×0.542|
| `date_labels` | array[string] | ✅ | 长度 ≥ 5 | 日期标签数组 |对应日期|
| `main_peaks` | array[object] | ✅ | 长度 = 3 | 主赛事前三峰值事件 = P7|
| `slot2_peaks` | array[object] | ✅ | 长度 = 3 | 竞品2峰值事件 |

### 10.2 验证规则

```python
# slot 必须是固定值
assert slot == "compare_slot_2"

# 平台分布规则同 P7（6平台）
# 其他验证规则同 P7
```

---

## 十一、跨页面一致性验证

### 11.1 P2 与 P3 数据一致性

```python
# P3 的同比数据必须与 P2 一致
assert P3['yoy_volume_change'] == P2['yoy_volume_change']
assert P3['yoy_interaction_change'] == P2['yoy_interaction_change']

```

### 11.2 P7/P8 主赛事数据一致性

```python
# P7 和 P8 的 main_summary 必须一致
assert P7['main_summary'] == P8['main_summary']

# P7 和 P8 的 main_vol_data 必须一致
assert P7['main_heat_data'] == P8['main_heat_data']

# P7 和 P8 的 date_labels 必须一致
assert P7['date_labels'] == P8['date_labels']
```

### 11.3 峰值事件覆盖完整性

```python
# P2 的 6 个峰值事件，P7/P8 各取 Top3，合计覆盖所有 P2 事件
p2_event_ids = {e['event_id'] for e in P2['peak_events']}
p7_event_ids = {e['event_id'] for e in P7['main_peaks']}
p8_event_ids = {e['event_id'] for e in P8['main_peaks']}

# P7 和 P8 合计应覆盖所有 P2 事件
assert p7_event_ids.union(p8_event_ids) == p2_event_ids
```

---

## 十二、summary 字段通用规范

每个页面的 `summary` 字段遵守以下规则：

| 规则 | 要求 |
|------|------|
| 数据驱动 | 必须基于实际查询的统计数据，禁止推测 |
| 数值格式 | 引用的声量、互动量、热度数值必须使用 K/M 整数格式（如 `94K`、`8M`） |
| 内容要素 | 见M1_data_contract各页面summary公式，**严格按照来源于计算规范，禁止发散** |
| 不引用高点 | summary 只描述数据层面（声量、互动量、热度、增长率等），不引用具体高点事件 |

```python
# 验证规则
for page in ["P2", "P3", "P4", "P5", "P6", "P7", "P8"]:
    summary = data[page].get("summary", "")
    assert summary and summary.strip(), f"{page}.summary 不能为空"
```

---

## 十三、数值格式规范

### 12.1 数量级格式

| 数值范围 | 格式 | 示例 |
|----------|------|------|
| 1,000 ~ 999,999 | `XK` | `21K` |
| 1,000,000+ | `XM` | `10M` |

### 12.2 百分比格式

```
格式: +X% 或 -X%
示例: +45%, -14%
```

### 12.3 日期格式

```
date_labels: "M.D" (如 "2.1", "2.10")
date_label (峰值事件): "M月D日" (如 "2月1日")
```

---

## 十四、常见错误清单

| ❌ 错误 | ✅ 正确 |
|--------|--------|
| `peak_events` 数组为空 `[]` | 必须包含指定数量的事件对象 |
| `slot2_peaks` 字段缺失 | P8 必须包含 `slot2_peaks` 字段 |
| `event_id` 重复或乱序 | P2 必须是 `evt_001` ~ `evt_006` 按顺序 |
| `idx` 超出数组范围 | `idx` 必须 < `len(vol_data)` |
| 平台分布百分比总和 ≠ 100 | 各平台占比总和应为 100 (±1) |
| `summary` 字段为空 | 必须非空且包含有效总结 |
| 峰值描述少于 8 字 | 严格 8-50 字 |
| 时间格式不一致 | 严格遵循 `YYYY-MM-DD` 格式 |

---

## 十五、峰值质量检查

**初稿阶段（阶段4）**：peak_events 的 date_label 为"XX月XX日"，text 为"[高点事件待确认]"，允许占位
**终稿阶段（阶段6）**：peak_events 的 text 必须为 8-50 字真实事件描述，date_label 为真实日期（如"3月7日"）

---

## 十六、验证检查点总结

在数据传递给下游模块前，必须通过以下所有检查点：

### ✅ 结构完整性
- [ ] 包含所有 8 个顶层字段 (meta, P2-P8)
- [ ] 每个页面包含所有必需字段
- [ ] 所有数组字段非空

### ✅ 数据类型正确性
- [ ] 字符串字段为 string 类型
- [ ] 数值数组为 array[number] 类型
- [ ] 对象字段为 object 类型

### ✅ 格式规范性
- [ ] 时间格式符合规范
- [ ] 数量级格式符合规范 (K/M)
- [ ] 百分比格式符合规范 (+/-X%)

### ✅ 数组长度一致性
- [ ] P2: `len(vol_data) == len(inter_data) == len(date_labels)`
- [ ] P5: `len(dy_vol_data) == len(dy_inter_data) == len(dy_date_labels)`
- [ ] P6: `len(wb_vol_data) == len(wb_inter_data) == len(wb_date_labels)`
- [ ] P7/P8: `len(main_heat_data) == len(slot_heat_data) == len(date_labels)`

### ✅ 峰值事件完整性
- [ ] P2: 恰好 6 个峰值事件
- [ ] P5: 恰好 6 个峰值事件
- [ ] P6: 恰好 6 个峰值事件
- [ ] P7/P8: 各 3 个主赛事峰值 + 3 个竞品峰值

### ✅ 跨页面一致性
- [ ] P3 同比数据与 P2 一致
- [ ] P7/P8 主赛事数据一致
- [ ] P7/P8 峰值事件覆盖 P2 所有事件

---

**文档版本**: v3.0
**最后更新**: 2026-05-19
**维护者**: 社媒监测报告技能团队
**变更说明**: v3.0 对应 SKILL.md v4.0，summary不引用高点、删除字数硬限制、峰值分初稿/终稿两阶段质量要求
