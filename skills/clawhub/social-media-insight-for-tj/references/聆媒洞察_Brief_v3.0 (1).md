# 聆媒洞察_魔方2版Agent — 取数 Brief v2.1

> **用途**：为 VCT 社媒监测报告自动化流程提供完整的 MCP 取数指令
> **执行者**：聆媒洞察_魔方2版Agent
> **产出物**：原始 API 响应 + Agent 文本（JSON 格式）
> **后处理**：Supervisor 将产出物转为标准 M1 JSON
> **版本**：v3.0 | 2026-05-20
> **变更说明**：v3.0高点占位date_label改为真实月日（不填"XX月XX日"），与校验脚本对齐

# 你是数据制作者，最终输出的 JSON 顶层只能包含 meta、peak_events、api 三个字段，严格按照四、输出格式要求搬运你查到的数据
# 重视！！！你产出的高点描述直接关系到最终产出质量
# 你是整个交付最核心的环节！！！
---

## ⭐ 执行清单（Execution Checklist）

- [ ] **高点数量要求**：P2=6, P5=6, P6=6, P7_slot=3, P8_slot=3,P7_main = P8_main= P2 top3 

#### 数据完整性 
- [ ] **api字段**：17个key全部有数据（main_overview, main_trend, ...） 
- [ ] **datasource**：必须使用完整10平台列表（使用预定义常量） 


--- 

## 一、基础配置

### 1.1 赛事 ID 映射表

| 赛事名称 | analysis_target_id | rule_group_id | target_type |
|---------|-------------------|---------------|-------------|
| VCT | 1304380 | 102321 | analysisTargetRule |
| PEL | 1324390 | 102321 | analysisTargetRule |
| 三角洲 | 1324395 | 102321 | analysisTargetRule |

### 1.2 竞品关系与 Slot 映射

> ⚠️ **重要**：PPT 页面固定为 slide7=`compare_slot_1`，slide8=`compare_slot_2`。
> 竞品填入哪个 slot 由主赛事决定，**不是按竞品A/B字面顺序**。

| 主赛事 | compare_slot_1（P7/slide7） | compare_slot_2（P8/slide8） |
|-------|---------------------------|---------------------------|
| VCT | PEL | 三角洲 |

### 1.3 时间范围（运行时由用户输入，不写死）

```
主赛事时间范围：{main_start} 至 {main_end}
竞品A时间范围：{comp_a_start} 至 {comp_a_end}
竞品B时间范围：{comp_b_start} 至 {comp_b_end}
往年赛事同比时间范围：{yoy_start} 至 {yoy_end}
```

时间格式：`YYYY-MM-DD`（例：`2026-03-01`）

### 1.4 固定 datasource 列表（必须完整，顺序和名称精确，"论坛__虎扑（论坛）", 使用全角括号查询（）Unicode: U+FF08, U+FF09）

```python
# ⚠️ 重要：必须保留全角括号查询，直接复制使用，不要手动输入
datasource = [
    "微博", "微博评论", "新闻", "晒单__小红书", "微信",
    "视频__抖音", "视频__哔哩哔哩", "视频__快手",
    "论坛__虎扑（论坛）", # 全角括号（）Unicode: U+FF08, U+FF09
    "问答__知乎"
]
```

---

## 二、高点事件占位规则（v4.0）

> ⚠️ **v4.0变更**：高点事件由用户从趋势图中选取（阶段5），Agent 只需输出占位数据。

### 占位数据生成

对每个需要高点的页面，从分日数据中按声量降序取 Top N 日期，生成占位 peak_events：

| 场景 | N |
|------|---|
| P2（全平台） | 6 |
| P5（抖音） | 6 |
| P6（微博） | 6 |
| P7 竞品 Slot1 | 3 |
| P8 竞品 Slot2 | 3 |

**占位格式**：
```json
{"event_id": "evt_001", "idx": 34, "date_label": "3月15日", "text": "[高点事件待确认]"}
```

- `idx`：该日期在分日数据数组中的 0-based 索引（按声量降序取TopN对应的idx）
- `date_label`：填该日期的真实月日，格式为 `M月D日`（如 `3月15日`、`5月3日`），从分日数据中对应日期直接提取，**不要填 `"XX月XX日"` 等占位符**
- `text`：统一填 `"[高点事件待确认]"`
- **不调用 `query_raw_posts`**，真实高点内容在阶段5由用户选点后查询

### 排序与 ID 分配

按 idx 升序排列，分配 event_id：

| 场景 | event_id 格式 |
|------|-------------|
| P2 | `evt_001` ~ `evt_006` |
| P5 | `evt_p5_001` ~ `evt_p5_006` |
| P6 | `evt_p6_001` ~ `evt_p6_006` |
| P7 竞品 | `evt_p7_001` ~ `evt_p7_003` |
| P8 竞品 | `evt_p8_001` ~ `evt_p8_003` |

**P7/P8 主赛事高点复用，不用额外拉数**：从 P2 的 6 个事件中按综合得分选 Top 3 → `peak_events.P7_main` / `peak_events.P8_main`

---

## 三、调用清单 - 过程文件用规则+平台命名

> **关于单独重跑**：本清单中每个 Call 均可独立执行。当用户或 Supervisor 指定重跑某个 Call 时，只需执行对应 Call，将新结果更新到 `stage1_original_output.json` 的对应 api 字段，不需要重跑全部 Call。
>
> **核心原则**：Agent 只需取数并将原始响应放入对应 key，**不做任何字段重命名、格式化或计算**。
> 热度指数、平台映射、K/M格式化、增长率计算全部由 Transform 层处理。

### 【Call 1】主赛事整体概览（当期）- 过程文件用规则+平台命名


**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}",
    end_time="{main_end}",
    datasource=[完整10平台],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```
**→ 放入** `api.main_overview`

### 【Call 1b】主赛事整体概览（同比期）- 过程文件用规则+平台命名


```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{yoy_start}",
    end_time="{yoy_end}",
    datasource=[完整10平台],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```
**→ 放入** `api.main_overview_yoy`

### 【Call 2】主赛事分日数据


**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}", end_time="{main_end}",
    datasource=[完整10平台],
    dimension="date"
)
```
**→ 放入** `api.main_trend`


### 【Call 2b】主赛事高点占位
**高点占位**：从分日数据中按声量降序取 Top 6 日期 → 生成占位 peak_events → 放入 `peak_events.P2`
**注意**：不调用 query_raw_posts，date_label 填该日期的真实月日（如"3月15日"），text 填"[高点事件待确认]"

**复用**：P7/P8 主赛事高点从 P2 的 6 个中选 Top 3 → `peak_events.P7_main` / `peak_events.P8_main`


### 【Call 3a】主赛事平台分布（当期）- 过程文件用规则+平台命名

**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}", end_time="{main_end}",
    datasource=[完整10平台],
    dimensions=["平台"],
    metrics=["声量", "互动数"]
)
```
**→ 放入** `api.main_platform`

### 【Call 3b】主赛事平台分布（同比期）- 过程文件用规则+平台命名


参数同 Call 3a，时间换为 `{yoy_start}` / `{yoy_end}`。
**→ 放入** `api.main_platform_yoy`

### 【Call 4a】主赛事抖音分日数据 - 过程文件用规则+平台命名


**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}", end_time="{main_end}",
    datasource=["视频__抖音"],
    dimension="date"
)
```
**→ 放入** `api.dy_trend`

### 【Call 4a.1】抖音高点占位
**高点占位**：从抖音分日数据中按声量降序取 Top 6 日期 → 生成占位 peak_events → 放入 `peak_events.P5`
**注意**：不调用 query_raw_posts，date_label 填该日期的真实月日（如"3月15日"），text 填"[高点事件待确认]"



### 【Call 4b】主赛事抖音概览（当期）- 过程文件用规则+平台命名


**工具**：`query_analysis_data`

```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}",
    end_time="{main_end}",
    datasource=["视频__抖音"],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```

**→ 放入** `api.dy_overview`

### 【Call 4c】主赛事抖音概览（同比期）- 过程文件用规则+平台命名


参数同 Call 4b，时间换为 `{yoy_start}` / `{yoy_end}`。
**→ 放入** `api.dy_overview_yoy`

### 【Call 5a】主赛事微博分日数据- 过程文件用规则+平台命名


**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}", end_time="{main_end}",
    datasource=["微博", "微博评论"],
    dimension="date"
)
```
**→ 放入** `api.wb_trend`


### 【Call 5a.1】微博高点占位
**高点占位**：从微博分日数据中按声量降序取 Top 6 日期 → 生成占位 peak_events → 放入 `peak_events.P6`
**注意**：不调用 query_raw_posts，date_label 填该日期的真实月日（如"3月15日"），text 填"[高点事件待确认]"



### 【Call 5b】主赛事微博概览（当期）- 过程文件用规则+平台命名


**工具**：`query_analysis_data`
```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{主赛事ID}",
    start_time="{main_start}",
    end_time="{main_end}",
    datasource=["微博", "微博评论"],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```
**→ 放入** `api.wb_overview`

### 【Call 5c】主赛事微博概览（同比期）- 过程文件用规则+平台命名


参数同 Call 5b，时间换为 `{yoy_start}` / `{yoy_end}`。
**→ 放入** `api.wb_overview_yoy`

### 【Call 6】竞品 Slot1 整体概览 - 过程文件用规则+平台命名


```python

query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_1赛事ID}",
    start_time="{slot_1_start}",
    end_time="{slot_1_end}",
    datasource=[完整10平台],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```
**→ 放入** `api.slot1_overview`

### 【Call 6b】竞品 Slot1 平台分布 - 过程文件用规则+平台命名


```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_1赛事ID}",
    start_time="{slot_1_start}", end_time="{slot_1_end}",
    datasource=[完整10平台],
    dimensions=["平台"],
    metrics=["声量", "互动数"]
)
```
**→ 放入** `api.slot1_platform`

### 【Call 7】竞品 Slot1 分日数据- 过程文件用规则+平台命名


```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_1赛事ID}",
    start_time="{slot_1_start}", end_time="{slot_1_end}",
    datasource=[完整10平台],
    dimension="date"
)
```
**→ 放入** `api.slot1_trend`



### 【Call 7a】slot1高点占位
**高点占位**：从 slot1 分日数据中按声量降序取 Top 3 日期 → 生成占位 peak_events → 放入 `peak_events.P7_slot`
**注意**：不调用 query_raw_posts，date_label 填该日期的真实月日（如"3月15日"），text 填"[高点事件待确认]"


### 【Call 8】竞品 Slot2 整体概览- 过程文件用规则+平台命名

```python

query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_2赛事ID}",
    start_time="{slot_2_start}",
    end_time="{slot_2_end}",
    datasource=[完整10平台],
    metrics=["声量", "互动数"],
    dimensions=[]  # 空列表,不分组,返回整体汇总值
)
```

**→ 放入** `api.slot2_overview`

### 【Call 8b】竞品 Slot2 平台分布- 过程文件用规则+平台命名

```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_2赛事ID}",
    start_time="{slot_2_start}", end_time="{slot_2_end}",
    datasource=[完整10平台],
    dimensions=["平台"],
    metrics=["声量", "互动数"]
)
```

**→ 放入** `api.slot2_platform`

### 【Call 9】竞品 Slot2 分日数据- 过程文件用规则+平台命名

```python
query_analysis_data(
    target_type="analysisTargetRule",
    analysis_target_id="{slot_2赛事ID}",
    start_time="{slot_2_start}", end_time="{slot_2_end}",
    datasource=[完整10平台],
    dimension="date"
)
```

**→ 放入** `api.slot2_trend`



### 【Call 9a】slot2高点占位
**高点占位**：从 slot2 分日数据中按声量降序取 Top 3 日期 → 生成占位 peak_events → 放入 `peak_events.P8_slot`
**注意**：不调用 query_raw_posts，date_label 填该日期的真实月日（如"3月15日"），text 填"[高点事件待确认]"

---

## 四、Agent 输出格式 -- 严格执行

> ⚠️ **核心原则**：Agent 不再生成 M1 JSON，而是输出以下结构。
> Transform 层会将此格式自动转为标准 M1 JSON。

```json
{
    "meta": {
        "main_event": "LPL",
        "report_stage": "第一赛段",
        "main_time_range": "{main_start} ~ {main_end}",
        "yoy_time_range": "{yoy_start} ~ {yoy_end}",
        "slot1_time_range": "{slot_1_start} ~ {slot_1_end}",
        "slot2_time_range": "{slot_2_start} ~ {slot_2_end}",
        "slot1_event_name": "KPL",
        "slot2_event_name": "VCT",
        "playoff_start": "由用户输入_格式YYYY-MM-DD",
        "generated_at": "2026-05-06"
    },

    "peak_events": {
        "P2": [
            {"event_id": "evt_001", "idx": 34, "date_label": "3月15日", "text": "[高点事件待确认]"},
            {"event_id": "evt_002", "idx": 5,  "date_label": "3月22日", "text": "[高点事件待确认]"},
            {"event_id": "evt_003", "idx": 0,  "date_label": "3月1日", "text": "[高点事件待确认]"},
            {"event_id": "evt_004", "idx": 35, "date_label": "3月16日", "text": "[高点事件待确认]"},
            {"event_id": "evt_005", "idx": 7,  "date_label": "3月8日", "text": "[高点事件待确认]"},
            {"event_id": "evt_006", "idx": 10, "date_label": "3月11日", "text": "[高点事件待确认]"}
        ],
        "P5": [
            {"event_id": "evt_p5_001", "idx": 34, "date_label": "3月15日", "text": "[高点事件待确认]"}
            /* 共6个 */
        ],
        "P6": [
            {"event_id": "evt_p6_001", "idx": 34, "date_label": "3月15日", "text": "[高点事件待确认]"}
            /* 共6个 */
        ],
        "P7_main": [
            /* P2的Top3，直接引用event_id，共3个 */
        ],
        "P7_slot": [
            /* Slot1赛事高点占位，共3个 */
        ],
        "P8_main": [
            /* P2的Top3，共3个 */
        ],
        "P8_slot": [
            /* Slot2赛事高点占位，共3个 */
        ]
    },

    "api": {
        "main_overview":     "/* Call 1 原始返回 */",
        "main_overview_yoy": "/* Call 1b 原始返回 */",
        "main_trend":        "/* Call 2 原始返回（分日数组）*/",
        "main_platform":     "/* Call 3a 原始返回（平台维度数组）*/",
        "main_platform_yoy": "/* Call 3b 原始返回 */",
        "dy_overview":       "/* Call 4b 原始返回 */",
        "dy_overview_yoy":   "/* Call 4c 原始返回 */",
        "dy_trend":          "/* Call 4a 原始返回（抖音分日数组）*/",
        "wb_overview":       "/* Call 5b 原始返回 */",
        "wb_overview_yoy":   "/* Call 5c 原始返回 */",
        "wb_trend":          "/* Call 5a 原始返回（微博分日数组）*/",
        "slot1_overview":    "/* Call 6 原始返回 */",
        "slot1_platform":    "/* Call 6b 原始返回 */",
        "slot1_trend":       "/* Call 7 原始返回 */",
        "slot2_overview":    "/* Call 8 原始返回 */",
        "slot2_platform":    "/* Call 8b 原始返回 */",
        "slot2_trend":       "/* Call 9 原始返回 */"
    }
}
```

### 关键规则 - 严格执行

1. **`api.*` 字段**：直接粘贴接口原始返回，**不做任何改名、重组、格式化**
2. **`peak_events`**：包含 `event_id` / `idx` / `date_label` / `text`，其中 date_label 和 text 为占位值（真实内容在阶段5由用户选点后查询填入）
3. **`meta`**：Agent 填入用户提供的参数，字段名固定不可改。其中 `playoff_start` 由用户运行时直接输入，无需 MCP 查询。
4. **不调用 `query_raw_posts`**：高点事件的查询在阶段5执行，阶段1只生成占位数据

> ⚠️ **summaries 由 Supervisor 在 Transform 阶段生成，Agent 不负责。**

---

## 五、交付要求

### Agent 必须确保

1. **`api.*` 全部 20 个 key 都有数据**，不得遗漏
2. **`peak_events` 数量正确**：P2=6, P5=6, P6=6, P7_main=3, P7_slot=3, P8_main=3, P8_slot=3
3. **高点文本**：date_label 填该日期的真实月日（如"3月15日"，从分日数据中提取），text 填"[高点事件待确认]"（占位格式）
4. **`meta` 字段完整**：main_event / report_stage / 所有 time_range / event_name / generated_at

### Agent 不需要关心

- ~~热度指数计算~~（Transform 处理）
- ~~平台名称映射~~（Transform 处理）
- ~~数值 K/M 格式化~~（Transform 处理）
- ~~P4 增长率计算~~（Transform 处理）
- ~~P7/P8 数据对齐~~（Transform 处理）
- ~~M1 JSON 结构~~（Transform 处理）
- ~~数据验证~~（M0 验证脚本处理）

---

## 七、常见错误清单

| ❌ 错误 | ✅ 正确 |
|--------|--------|
| `"论坛__虎扑(论坛)"` 半角括号 | `"论坛__虎扑（论坛）"` 全角括号 |
| `"视频__bilibili"` | `"视频__哔哩哔哩"` |
| datasource 只用3-4个平台 | 必须完整10个平台 |
| 时间格式 `"2026-03-01"` | 必须 `"2026-03-01 00:00:00"` |
| 对 API 返回做重命名/重组 | 原样粘贴到 `api.*` 对应 key |
| 遗漏某个key | 全部 20 个 API 响应都要有 |
| 自行计算热度/格式化数值 | 交给 Transform 处理 |

---

## 八、高点事件交付后修改（已废弃）

> ⚠️ v4.0 起高点事件由阶段5处理，本节不再适用。如需修改高点，回到阶段5重新选点查询。

~~HTML 生成后需要修改高点标注时，无需重跑全流程：~~

```bash
# 以下命令已废弃
# python3 M5_pipeline/patch_peaks.py \
#     --pptx  已生成的报告.pptx \
#     --data  原始M1数据.json \
#     --patches 高点修改.json \
#     --output 修改后报告.pptx
```

---

## 九、Agent自检清单（执行完毕后必须逐项确认）

> **用途**：Agent执行完毕后，在返回控制权给Supervisor前，必须逐项确认以下清单
> **强制性**：所有项目必须100%通过，任何一项未通过都必须修复后再返回

### 🔴 MCP调用字段完整性检查（20个key，缺一不可）

- [ ] `api.main_overview` 存在且有数据（非空对象）
- [ ] `api.main_overview_yoy` 存在且有数据（非空对象）
- [ ] `api.main_trend` 存在且有数据（非空数组）
- [ ] `peak_events.P2` 存在且有数据（非空数组）
- [ ] `api.main_platform` 存在且有数据（非空数组）
- [ ] `api.main_platform_yoy` 存在且有数据（非空数组）
- [ ] `api.dy_overview` 存在且有数据（非空对象）
- [ ] `api.dy_overview_yoy` 存在且有数据（非空对象）
- [ ] `api.dy_trend` 存在且有数据（非空数组）
- [ ] `peak_events.P5` 存在且有数据（非空数组）
- [ ] `api.wb_overview` 存在且有数据（非空对象）
- [ ] `api.wb_overview_yoy` 存在且有数据（非空对象）
- [ ] `api.wb_trend` 存在且有数据（非空数组）
- [ ] `peak_events.P6` 存在且有数据（非空数组）
- [ ] `api.slot1_overview` 存在且有数据（非空对象）
- [ ] `api.slot1_platform` 存在且有数据（非空数组）
- [ ] `api.slot1_trend` 存在且有数据（非空数组）
- [ ] `peak_events.P7_main` 存在且有数据（非空数组，3个事件）
- [ ] `peak_events.P7_slot` 存在且有数据（非空数组，3个事件）
- [ ] `api.slot2_overview` 存在且有数据（非空对象）
- [ ] `api.slot2_platform` 存在且有数据（非空数组）
- [ ] `api.slot2_trend` 存在且有数据（非空数组）
- [ ] `peak_events.P8_main` 存在且有数据（非空数组，3个事件）
- [ ] `peak_events.P8_slot` 存在且有数据（非空数组，3个事件）

### 🔴 顶层结构检查

- [ ] JSON顶层只包含3个字段：`meta`、`peak_events`、`api`
- [ ] 没有其他额外字段（如`summaries`、`statistics`等）

### 🔴 peak_events字段检查

- [ ] `peak_events.P2` 包含6个事件
- [ ] `peak_events.P5` 包含6个事件
- [ ] `peak_events.P6` 包含6个事件
- [ ] `peak_events.P7_main` 包含3个事件
- [ ] `peak_events.P7_slot` 包含3个事件
- [ ] `peak_events.P8_main` 包含3个事件
- [ ] `peak_events.P8_slot` 包含3个事件
- [ ] 每个高点事件包含4个字段：`event_id`、`idx`、`date_label`、`text`
- [ ] 高点事件 date_label 填真实月日（如"3月15日"），text 允许占位值（"[高点事件待确认]"）

### 🔴 meta字段检查

- [ ] `meta.main_event` 存在
- [ ] `meta.report_stage` 存在
- [ ] `meta.main_time_range` 存在
- [ ] `meta.yoy_time_range` 存在
- [ ] `meta.slot1_time_range` 存在
- [ ] `meta.slot2_time_range` 存在
- [ ] `meta.slot1_event_name` 存在
- [ ] `meta.slot2_event_name` 存在
- [ ] `meta.playoff_start` 存在且格式为YYYY-MM-DD
- [ ] `meta.generated_at` 存在

### 🔴 数据质量检查

- [ ] 所有api.*的值是MCP接口的原始JSON响应，未做任何重命名或格式化
- [ ] 所有数组类型的api字段（trend、platform）长度>0
- [ ] 所有对象类型的api字段（overview）包含声量和互动数字段

### ✅ 自检通过标准

**只有当以上所有项目都打勾通过后，才能返回控制权给Supervisor。**

如果任何一项未通过：
1. 立即修复该项
2. 重新执行完整自检清单
3. 直到所有项目100%通过

---

*Brief 版本：v3.0 | 更新：2026-05-19 | 对应 SKILL.md v4.0*
*v3.0变更：高点事件改为占位输出，不调用query_raw_posts，P7/P8自检拆分为main+slot*
