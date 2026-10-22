---
name: vct-report-py2
description: "社媒监测报告全流程自动化生成。使用聆媒洞察_魔方2版 agent获取数据，supervisor转换对齐格式,输出完整8页HTML幻灯片。覆盖整体热度、平台分布、抖音下钻、微博下钻、竞品对比（P7/P8）。适用于LPL/VCT/KPL赛事社媒监测报告周期性生产。"
metadata:
  version: "4.0.0"
  category: productivity
  created: "2026-04-23"
  updated: "2026-05-20"
  changelog: "v4.0.0: 流程重构为6阶段+2介入点，高点事件改为用户从趋势图选点后由Agent查询，初稿/终稿分离，date_label改用真实月日"
---

# VCT 赛事社媒监测报告 全流程生成技能

## 能力概述

端到端自动化生成8页社媒监测报告HTML幻灯片，含两次用户介入点确保数据与高点准确性：

```
[社媒Agent] → 调用MCP取数接口 → 原始数据 + peak_events（模拟占位）
 ↓
[Supervisor验证] → 检查api字段完整性 → 通过才继续
 ↓
[Supervisor] → Transform原始数据 → 标准M1 JSON（含summary，不含高点细节）
 ↓
[M0校验] → 数据完整性 + 非零值校验 → 通过才继续
 ↓
[阶段4] 初稿HTML → 趋势图正常渲染，高点显示占位文字
 ↓
🛑 介入点1：用户检查数据 → 反馈 → 分路修复 → 循环
 ↓
[阶段5] 用户从趋势图选高点日期 → Agent查询高点内容 → 写回peak_events
 ↓
🛑 介入点2：用户确认高点内容
 ↓
[阶段6] 终稿HTML → 含真实高点标注
```

---

## 执行工作流

### ⚠️ 第一步：判断走哪条路

| 用户意图 | 走哪条路 |
|---------|---------|
| 生成新报告 | **全流程**（阶段1→1.5→2→3→4→介入点1→5→介入点2→6） |
| 修改已生成报告的数据 | **回阶段1/2修复** → 重新走到阶段4 |
| 已有验证通过的M1 JSON，只生成幻灯片 | **直接执行阶段4** |
| 高点已确认，只需重新渲染 | **直接执行阶段6** |

---
### 阶段0：执行前准备
**重要：确保Agent能访问聆媒洞察_魔方2版Agent — 取数 Brief v3.0**

由于Agent工作空间隔离，必须在委托前将Brief文档复制到工作空间：

```python
import os
import shutil
import glob

# 动态查找当前技能路径（推荐）
skill_dirs = glob.glob('.skills/*/references/聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md')
if skill_dirs:
    brief_source = skill_dirs[0]  # 找到第一个匹配的Brief文档
    shutil.copy(brief_source, '聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md')
    print(f"✅ Brief文档已复制: {brief_source}")
else:
    print("❌ 未找到Brief文档，请检查技能包结构")

```


### 阶段1：Agent取数（由 DM-聆媒洞察_魔方2版Agent 执行）

#### 🔴 Supervisor委托指令模板（v4.0）

**使用说明**：supervisor 委托时必须包含如下强调信息

【强制约束】
1. 必须完整阅读工作空间中的'聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md'文档
2. 严格按照Brief中的规范执行，不得自行发散
3. 论坛_虎扑（论坛）查询时保留全角括号
4. 任何疑问必须参考Brief，不得擅自决策

【强制输出要求】：
1. ⚠️ 必须输出api字段，包含17个MCP接口的原始返回（main_overview, main_overview_yoy, main_trend, main_platform, main_platform_yoy, dy_overview, dy_overview_yoy, dy_trend, wb_overview, wb_overview_yoy, wb_trend, slot1_overview, slot1_platform, slot1_trend, slot2_overview, slot2_platform, slot2_trend）
2. ⚠️ api字段是Transform阶段的核心数据源，不可遗漏任何一个key
3. ⚠️ api.*的值必须是MCP接口的原始JSON响应，不得做任何重命名、重组或格式化
4. 输出格式必须严格按照Brief第四节"Agent输出格式"执行，顶层只能包含meta、peak_events、api三个字段

【峰值事件要求】：
- 输出35个峰值事件占位（P2=6个，P5=6个，P6=6个，P7_slot=3个，P8_slot=3个，P7_main = P8_main = P2中的top3个）
- **使用模拟日期和模拟text**，格式如下：
  ```json
  {"event_id": "P2_0", "idx": 0, "date_label": "3月15日", "text": "[高点事件待确认]"}
  ```
- date_label 填该日期的真实月日（如"3月15日"），从分日数据中对应日期直接随机提取
- idx 为模拟值（均匀分布），真实高点由用户在阶段5从趋势图中选取后确定

【输出文件】：
- 文件名：stage1_original_output.json
- 保存位置：工作空间根目录

【执行完毕后自检清单】：
在返回控制权给Supervisor前，必须逐项确认：
□ api.main_overview 有数据
□ api.main_overview_yoy 有数据
□ api.main_trend 有数据（数组）
□ api.main_platform 有数据（数组）
□ api.main_platform_yoy 有数据（数组）
□ api.dy_overview 有数据
□ api.dy_overview_yoy 有数据
□ api.dy_trend 有数据（数组）
□ api.wb_overview 有数据
□ api.wb_overview_yoy 有数据
□ api.wb_trend 有数据（数组）
□ api.slot1_overview 有数据
□ api.slot1_platform 有数据（数组）
□ api.slot1_trend 有数据（数组）
□ api.slot2_overview 有数据
□ api.slot2_platform 有数据（数组）
□ api.slot2_trend 有数据（数组）
□ peak_events包含35个占位事件（P2=6, P5=6, P6=6, P7_main=3, P7_slot=3, P8_main=3, P8_slot=3）
□ 每个峰值事件包含event_id、idx、date_label、text四个字段

【完成后立即返回】：
完成后立即返回控制权给Supervisor，附带以下信息：
{"status": "stage1_complete", "output_file": "stage1_original_output.json", "summary": "已完成MCP接口调用、35个峰值事件占位生成"}
不要等待用户确认，不要询问"是否继续"。


#### DM-聆媒洞察_魔方2版Agent 职责：
1. 按 `references/聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md` 执行MCP接口调用
2. 生成peak_events占位（date_label填真实月日+text填占位文字，真实内容待阶段5用户选点后查询）

> ⚠️ **summary 由 Supervisor 在 Transform 阶段生成，Agent 不负责。**

Agent 输出格式（原始格式，非M1）：

```json
{
  "meta": {
    "main_event": "LPL",
    "report_stage": "第一阶段",
    "playoff_start": "2026-04-11",
    "main_time_range": "...",
    "yoy_time_range": "...",
    "slot1_time_range": "...",
    "slot2_time_range": "...",
    "slot1_event_name": "KPL",
    "slot2_event_name": "VCT",
    "generated_at": "2026-05-19"
  },
  "peak_events": {
    "P2": [
      {"event_id": "P2_0", "idx": 0, "date_label": "3月1日", "text": "[高点事件待确认]"},
      {"event_id": "P2_1", "idx": 5, "date_label": "3月8日", "text": "[高点事件待确认]"}
    ],
    "P5": [...],
    "P6": [...],
    "P7_main": [...], "P7_slot": [...],
    "P8_main": [...], "P8_slot": [...]
  },
  "api": {
    "main_overview": { ... },
    "main_overview_yoy": { ... },
    "main_trend": [...],
    "main_platform": [...],
    "main_platform_yoy": [...],
    "dy_overview": { ... },
    "dy_overview_yoy": { ... },
    "dy_trend": [...],
    "wb_overview": { ... },
    "wb_overview_yoy": { ... },
    "wb_trend": [...],
    "slot1_overview": { ... },
    "slot1_platform": [...],
    "slot1_trend": [...],
    "slot2_overview": { ... },
    "slot2_platform": [...],
    "slot2_trend": [...]
  }
}
```

> Agent **不负责**：热度计算、平台名称映射、数值格式化、P4增长率计算、P7/P8数据对齐、**summary生成**、**高点事件真实内容查询**。

取数详细规范见 `references/聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md`。


### ⚠️ 阶段1.5：Supervisor中间验证（强制执行）

**触发条件**：收到Agent的阶段1完成信号

**执行方式**：Supervisor自执行，使用 `validation/validate_agent_output.py` 脚本

```bash
python3 validation/validate_agent_output_v1.1.py stage1_original_output.json
```

**验证内容**：
- ✅ 文件存在且可解析
- ✅ 顶层字段完整：meta、peak_events、api（无summaries）
- ✅ 每个api.*的值非空且为有效JSON
- ✅ peak_events数量正确（P2=6, P5=6, P6=6, P7_main=3, P7_slot=3, P8_main=3, P8_slot=3）
- ✅ 峰值事件结构完整（event_id、idx、date_label、text），date_label格式为M月D日

**如果验证失败**：
- 打印详细错误报告，指出缺失的api字段或结构问题
- **必须返回Agent重新取数，不能跳过验证直接进入Transform**

**验证通过后**：
- 自动进入阶段2（Transform），无需用户确认

---

### 阶段2：Transform（由 Supervisor 执行）

触发条件: 阶段1.5验证通过，自动开始，无需用户确认

将Agent原始输出转换为标准M1 JSON，严格仿照 `test_data/m1_template.json` 和 `references/M1_data_contract.md`：

1. **字段映射**：将API原始字段映射到M1标准字段
2. **热度计算**：`热度指数 = 声量 × 49.704 + 互动量 × 0.542`
3. **平台名称映射**：`视频-抖音` → `抖音`，`晒单-小红书` → `小红书`，`视频-哔哩哔哩` → `B站`，`视频-快手` → `快手`，`论坛-虎扑（论坛）` → `虎扑`，`问答-知乎` → `知乎`
4. **格式化**：数值K/M/百分比**取整**（不保留小数，如 `94K`、`8M`、`+45%`）
5. **P4增长率计算**：基于 channel_heat 计算各平台同比增长率 `(now-yoy)/yoy×100%`
6. **P7/P8数据对齐**：主赛事数据与竞品数据对齐到相同日期范围
7. **P3平台分布**：计算声量/互动量/热度的平台占比（5平台：微博/抖音/B站/小红书/其他），确保总和=100%
8. **P7/P8平台分布**：计算竞品平台占比（6平台：微博/抖音/B站/小红书/快手/其他），快手单独列出
9. **Summary生成**：Transform完成后，按 `references/M1_data_contract.md` 各页面字段定义中的 `summary` 公式逐页生成 P2-P8，写入 M1 JSON。格式要求（K/M/百分比取整、禁用词）以 contract 为准。**Summary只描述数据层面（声量、互动量、同比增长等），禁止自由发散**，高点事件待阶段5确认。
10. **Peak_events传递**：将阶段1的占位peak_events原样写入M1 JSON，等待阶段5替换为真实内容


| api.xx 字段 | 数据形态 | Transform操作 |
|---|---|---|
| `main_trend` / `slot1_trend` / `slot2_trend` | **日期×多平台多行**（N天×P平台=N×P条，平台数不固定） | **必须按日期group by加总**声量/互动数 → 得到N个值的数组 |
| `dy_trend` / `wb_trend` | 单平台，每天1条 | 直接取声量/互动数数组，无需聚合 |
| `main_platform` / `main_platform_yoy` / `slot1_platform` / `slot2_platform` | 按平台分行（每行一个平台） | 映射平台名 → 取声量/互动数值 |
| `main_overview` / `*_overview` / `*_overview_yoy` | **list类型，长度=1**（非dict） | 取值用 `v[0]['声量']`，不是 `v['声量']` |

> ⚠️ trend类多平台字段平台数不固定（不同赛事可能7或8个），必须动态group by，不能硬编码平台数。

**⚠️ 关键要求（防零值）：**
- 所有平台占比不得为0，如果某平台数据为0，需返回Agent重新取数
- `total_volume`、`total_interaction`、`heat_index` 不得为0
- `channel_heat` 的 `heat_now` 和 `heat_yoy` 不得为0
- P5 抖音、P6 微博核心指标不得为0

---

### 阶段3：M0数据校验（由 Supervisor 执行，必须通过才能继续）

```bash
python3 validation/validate_m1_data_v3.0.py <M1数据.json>
```

**校验内容：**
- ✅ 结构完整性：所有必需字段存在（含 P8、playoff_start）
- ✅ 数据类型：字段类型正确
- ✅ 格式规范：K/M/百分比为整数格式
- ✅ 数组长度：各页面趋势数组等长
- ✅ **非零值校验**：声量、互动、热度、平台占比均不为0
- ✅ 峰值事件：P2=6个/P5=6个/P6=6个/P7&P8各3个主赛事+3个竞品（允许占位text）
- ✅ summary：P2-P8各页存在且非空，K/M/百分比取整，无禁用词
- ✅ 跨页面一致性：P2/P3同比数据一致，P7/P8主赛事数据一致

**如果校验失败**：
- 打印详细错误报告
- **必须返回阶段1重新取数，不能跳过校验直接生成**

---

### 阶段4：生成初稿HTML（由 Supervisor 执行）

**前提：M0校验必须通过。**

初稿HTML包含完整的趋势图渲染，高点位置显示占位文字（如"[高点事件待确认]"），供用户检查数据和选取高点日期。

#### 步骤1：加载技能，进入技能目录

```python
skill_loader(skill_id="<skill_id>", skill_name="vct-report")
```

```bash
cd /path/to/vct-report
```

#### 步骤2：一键生成

```bash
python3 scripts/generate_slides.py \
  --data <M1数据.json路径> \
  --output <输出目录>
```

#### 步骤3：检查输出

确认输出目录中存在7个HTML文件：
```
output/
├── p1.html — 封面页
├── p2.html — 整体热度概览
├── p3.html — 整体热度分析
├── p4.html — 重点平台表现
├── p5.html — 抖音平台热度分析
├── p7.html — 竞品1对比（KPL）
└── p8.html — 竞品2对比（VCT）
```

#### 步骤4：交付用户检查

将初稿HTML交付用户，等待用户反馈。

---

### 🛑 介入点1：用户检查数据与反馈

**触发条件**：初稿HTML已交付用户

**用户可能的反馈及分路修复**：

- 用户可直接 @聆媒洞察Agent 指定重跑某个 Call（如"重跑 Call 4a"），Agent 只执行该 Call 并更新对应 api 字段
- 也可通过 Supervisor 中转，Supervisor 根据用户反馈判断需重跑的 Call

| api字段 | 重跑Call |
|---------|---------|
| main_overview | Call 1 |
| main_overview_yoy | Call 1b |
| main_trend | Call 2 |
| main_platform | Call 3a |
| main_platform_yoy | Call 3b |
| dy_overview | Call 4b |
| dy_overview_yoy | Call 4c |
| dy_trend | Call 4a |
| wb_overview | Call 5b |
| wb_overview_yoy | Call 5c |
| wb_trend | Call 5a |
| slot1_overview | Call 6 |
| slot1_platform | Call 6b |
| slot1_trend | Call 7 |
| slot2_overview | Call 8 |
| slot2_platform | Call 8b |
| slot2_trend | Call 9 |

| 反馈类型 | 修复路径 | 执行者 |
|---------|---------|--------|
| Agent数据取错（某接口返回异常） | → 重跑对应 Call，更新 api 字段 | Agent |
| Supervisor Transform算错（热度/占比/格式有误） | → 回**阶段2**，修正Transform逻辑 | Supervisor |
| 其他数据问题 | → 视具体情况回阶段1或2 | 对应执行者 |

**循环规则**：
- 修复后：若重跑了 api 字段则回到**阶段2**重新 Transform → 阶段3 → 阶段4；若仅修 Transform 逻辑则直接**阶段2**→ 阶段3 → 阶段4，直到用户确认数据无误
- 用户确认数据正确后，进入阶段5

---

### 阶段5：用户选高点 → Agent查询高点内容

**触发条件**：介入点1通过，用户确认数据无误

**执行步骤**：

1. **用户从趋势图选取高点日期**：用户查看各页面（P2/P5/P6/P7/P8）趋势图，指定每个页面的峰值日期及对应idx
2. **Agent查询高点内容**：Supervisor委托Agent，对用户选定的日期执行高点事件查询（调用对应MCP接口），获取真实事件描述
3. **写回peak_events**：Agent返回高点内容后，Supervisor将真实事件替换M1 JSON中的占位数据，更新idx、date_label、text

**高点数量要求**：
- P2：6个
- P5：6个
- P6：6个
- P7_main：3个（与P8_main共享，取P2的top3）
- P7_slot：3个
- P8_main：3个（与P7_main共享）
- P8_slot：3个
- 合计：35个（其中P7_main = P8_main = P2的top3）

**Agent高点查询委托模板**：

【强制约束】
1. 根据用户指定的高点日期，查询对应日期的社媒热点事件
2. 返回格式：`{"event_id": "P2_0", "idx": 实际idx, "date_label": "3月15日", "text": "事件描述"}`
3. text需简明扼要（15-30字），描述该日期的关键事件
4. 按页面分组返回，便于Supervisor写回M1 JSON

---

### 🛑 介入点2：用户确认高点内容

**触发条件**：高点内容已查询并写回M1 JSON

**用户可能的操作**：
- ✅ 确认高点内容无误 → 进入阶段6生成终稿
- 🔄 修改某高点事件描述 → Supervisor直接修改M1 JSON中的text字段
- 🔄 调整高点日期 → 回阶段5重新查询对应日期的事件

---

### 阶段6：生成终稿HTML（由 Supervisor 执行）

**前提**：介入点2通过，用户确认高点内容。

#### 步骤1：使用更新后的M1 JSON生成终稿

```bash
python3 scripts/generate_slides.py \
  --data <更新后的M1数据.json路径> \
  --output <输出目录>
```

#### 步骤2：检查输出

确认输出目录中存在8个HTML文件，且高点标注显示真实事件内容。

#### 步骤3：交付终稿

将终稿HTML交付用户。

---

## 各页内容说明

| 页面 | 标题 | 核心内容 |
|------|------|---------|
| P1 | 封面 | 赛事名称、阶段、报告日期、数据周期 |
| P2 | 整体热度概览 | 声量/互动/热度数据卡 + 双Y轴趋势折线图 + 高点事件列表（6个） |
| P3 | 整体热度分析 | 同比柱状图（声量/互动/热度）+ 平台分布圆环图×3（5平台） |
| P4 | 重点平台表现 | 微博/抖音/B站/小红书热度同比柱状图 |
| P5 | 抖音平台热度分析 | 数据卡 + 折线图 + 6个高点标注（hover交互） |
| P7 | 竞品1对比（KPL） | PEL vs VCT对比表 + PEL平台分布圆环图（6平台含快手）+ 趋势对比折线图 |
| P8 | 竞品2对比（VCT） | 三角洲 vs VCT对比表 + 三角洲平台分布圆环图（6平台含快手）+ 趋势对比折线图 |

---

## 技术说明

**图表库：**
- Chart.js：`https://static-oss.deepminingai.com/web/static/js/chart.umd.min.js`
- datalabels（P3/P7/P8圆环图标签）：`https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2`

**inter_data说明：**
- P2的 `inter_data`、P5的 `dy_inter_data`、P6的 `wb_inter_data` 为绝对值
- 脚本内部自动转换为万单位在Y轴显示

**数值格式：**
- K/M/百分比均为整数，不保留小数（如 `94K`、`8M`、`+45%`）

**平台分布：**
- P3（主赛事）：5平台（微博/抖音/B站/小红书/其他）
- P7/P8（竞品）：6平台（微博/抖音/B站/小红书/快手/其他）

**高点排序：**
- 所有页面（P2/P5/P6/P7/P8）高点事件均按日期 idx 正序排列显示

**高点占位规则（初稿）**：
- 阶段4初稿中，peak_events的date_label使用从分日数据提取的真实月日（如"3月15日"），text显示"[高点事件待确认]"
- 趋势图高点标注位置正常渲染，显示占位文字
- 阶段5确认高点后，占位数据替换为真实内容

---

## 技能包结构

```
vct-report/
├── SKILL.md ← 本文件（完整流程说明）
├── scripts/
│   └── generate_slides.py ← 幻灯片生成脚本
├── validation/
│   ├── validate_m1_data_v3.0.py ← M0数据校验脚本 v3.0
│   └── validate_agent_output_v1.1.py ← Agent产出验证脚本 v1.1
├── assets/
│   ├── fonts/
│   │   └── 腾讯体-W7_副本.OTF
│   └── images/
│       ├── cover_bg.png
│       ├── cover_bg_left.jpg
│       ├── logo.png
│       ├── VCT_top.png
│       ├── music.png
│       ├── engage.png
│       ├── heart.png
│       ├── bilibili_icon.png
│       ├── douyin_icon.png
│       ├── weibo_icon.png
│       └── xiaohongshu_icon.png
├── test_data/
│   ├── mock_m1_data.json
│   └── m1_template.json ← M1 JSON模板（Transform参考）
└── references/
    ├── 聆媒洞察_魔方2版Agent — 取数 Brief v3.0.md ← MCP取数规范
    └── M1_data_contract_v3.0.md ← M1数据格式规范 v3.0
```
