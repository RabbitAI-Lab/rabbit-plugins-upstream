---
name: excel-studio
description: "从零生成或美化已有 Excel 工作簿，自动统一主题配色、列宽、数字格式、冻结筛选与打印设置，交付前自动质检。"
version: 1.0.0
---
# Excel Studio — 表格的创作 · 编排 · 美化

把「一份能直接发出去的 Excel」拆成三段可重复执行的工作：**创作**（内容与结构）、
**编排**（多表关系与页面顺序）、**美化**（视觉与可读性）。三段共用一套设计令牌，
由 `scripts/theme_engine.py` 唯一实现——所有颜色、字号、行高、格式、边框都来自这里，
不在建表脚本里散落手写的样式常量。

> `<SKILL_DIR>` 指本 SKILL.md 所在目录（当前安装位置：
> `C:/Users/Administrator${CLAUDE_SKILL_DIR}`）。下文命令中的
> `<SKILL_DIR>` 替换为实际绝对路径。

---

## 0. 先路由：这件事该由谁做

| 用户意图 | 走哪里 |
|---|---|
| 新建一份表、出一份报表、把数据整理成表、做汇总 | **本 skill · 创作链**（A/B） |
| 已有 `.xlsx`，只改版式、配色、列宽、对齐、数字格式、打印 | **本 skill · 美化链**（C） |
| 已有表要改数据、加列、补公式、透视、排序筛选、清洗 | 直接用 openpyxl/ pandas 改数据后回到本 skill |
| 既有文件含图表/图片/透视表，且必须原样保留只做微调 | 在 Excel/WPS 中手动微调（保真，勿用 openpyxl 重存） |
| 先改数据再美化 | 先用脚本改完数据保存 → 回到本 skill 美化链 |
| 产出 docx / pptx / pdf / 图片 | 不归本 skill |

判断口诀：**动数据用脚本，动观感找 excel-studio，动不得原对象就开 Excel/WPS 手动改。**

---

## 1. 美化链（C）：改造已有工作簿

最常用，也最容易出事，所以先讲。

### C1 · 风险体检

```bash
python "<SKILL_DIR>/scripts/beautify.py" "<文件路径>" --dry-run
```

读 JSON 的 `risks`：

- `blocking` 含 `chart` / `image` / `pivot` → **停下来**，不要加 `--force` 硬干。
  改用 Excel/WPS 手动微调，并把原因告诉用户。openpyxl 往返重存会捣烂这些对象。
- `warning` 含 `formula_cache` → 正常，继续，但记下后面必须处理缓存值。
- `warning` 含 `external_link` → 提醒用户外链可能失效。

`--dry-run` 同时会打印探测到的表头行、数据区行数、合计行，以及将要对每列施加的数字格式。
**先扫一眼这几项对不对**——探测错了，后面全都白做。

### C2 · 定改造强度

| 档位 | 改什么 | 什么时候用 |
|---|---|---|
| `conservative` | 只修列宽、数字格式、冻结窗格、打印设置、关网格线 | 用户只想「看起来整齐点」，或表里有刻意设计的配色要保留 |
| `standard`（默认） | 以上 + 标题/表头/正文配色、隔行条纹、边框、筛选、页签色、脚注降级 | 绝大多数场景 |
| `bold` | 以上 + 合计行放大强调 + 图表重配色 | 用于对外汇报、需要突出合计的场合 |

数据条**不自动加**。要加就显式指定列：`--data-bars E,H`。数据条是内容决策，脚本不该猜。

### C3 · 执行

```bash
python "<SKILL_DIR>/scripts/beautify.py" "<文件路径>" --level standard --theme business --recalc
```

- 默认输出 `<原名>_styled.xlsx`，**不动源文件**。
- 只有显式用 `-o` 指到源文件才会覆盖，此时脚本自动备份为 `<原名>.xlsx.bak`。
- `--recalc` 会调用内置重算脚本补齐公式缓存值；找不到时如实报告 `unavailable`。
- `--sheet 名称` 可只处理指定工作表（可重复传）。
- 主题可选 `business`（商务蓝）/ `graphite`（石墨灰）/ `emerald`（松石绿）/ `amber`（琥珀棕）。

### C4 · 质检

```bash
python "<SKILL_DIR>/scripts/qa_check.py" "<输出文件>"
```

读 `status`，**不要看退出码**：

- `pass` → 交付。
- `warn` → 逐条看 `issues`，能修就回 C3 修（例：调 `--level`、改列宽、补重算），
  修不了的在交付话术里说明。
- `fail` → **不得交付**。`formula_error` / `header_missing` / `duplicate_header` /
  `bad_sheet_name` 属于硬缺陷，必须修掉。

### C5 · 交付话术

```
已美化 <输出路径>：<N> 个工作表，统一为<主题名>主题（<档位> 档）。
改动：列宽重算、货币/百分比/日期格式统一、表头着色、隔行条纹、冻结表头、A4 横向打印。
未动：数据与公式原值、原有合并单元格。
注意：<risks 或 qa 里尚未消除的问题>
```

---

## 2. 创作链（A：单表 / B：多表编排）

### A1 · 定题与落盘（不反问用户）

从用户原话或附件名推断标题，推断不出来就用 `workbook_<YYYYMMDD_HHMMSS>`。
用户给的是目录就只当目录用，标题独立推断；给的是完整文件名才拆出目录与标题。
`~` 先展开。输出文件已存在时加时间戳，**不覆盖、不询问**。

工作目录 `<work_dir>` = 输出文件同目录下的 `.<输出文件名去扩展名>.ref/`，
用来放参考素材抽取结果和 `build.py`。

### A2 · 参考素材

| 来源 | 动作 |
|---|---|
| 本地 xlsx / xls / csv / tsv | 只读其数据，用 openpyxl 逐表读出即可；**绝不写回源文件** |
| 本地 pdf / docx / pptx | 需要时先用对应技能抽取文本，再进入设计 |
| 在线文档（docs.qq.com / file_id） | 用腾讯文档技能读取数据与样式作为参考 |
| 无参考 | 直接进 A3 |

### A3 · 读规范（动笔前必读）

1. **`references/design_system.md`** —— 颜色、字号、行高、列宽、边框、数字格式、对齐、
   打印、图表、反模式。所有数值都在这里，不要自己发明。
2. **`references/layout_patterns.md`** —— 按场景选版式蓝图（哪几个页签、字段顺序、
   区块布局、公式锚点、图表建议）。
3. 若同目录还装了 `xlsx` 技能，其参考文档是**结构正确性**层面的权威（坐标锚点、公式防错、除零保护）；
   本 skill 的设计系统负责**视觉与版式**。两者冲突时，正确性优先。

### A4 · 写 `build.py`

用 openpyxl 一次性建完整份工作簿，**末尾一次性套主题**，不要在每个单元格上手工刷样式。
骨架见 `references/design_system.md` §12，照抄后改。

记住三件事：

- 颜色字面量只能出现在 `xl()` 调用里，静态色一律先转成 `XL_` 常量再复用。
- 公式写成 Excel 公式字符串交给 openpyxl 落格，不在 Python 里算好写死；
  除法一律带分母空值与零值保护。
- 算好行号锚点再写公式，不要假设表头永远在第 1 行。

```bash
python "<work_dir>/build.py"
```

exit≠0 就读 stderr 改脚本重跑；不要盲目 `pip install`，骨架里已做「先 import、缺了才装」
的兜底。

### A5 · 校验

含公式时**先补缓存值，再质检**（顺序不能反，否则质检必然报一片空白）：

```bash
python "<SKILL_DIR>/scripts/beautify.py" "<输出文件>" --recalc-only
python "<SKILL_DIR>/scripts/qa_check.py" "<输出文件>"
```

`--recalc-only` 只补公式缓存，不改任何样式、不另存文件。
若返回 `unavailable`（找不到重算引擎），如实告诉用户「Excel/WPS 打开会自动计算，
但微信、邮件等第三方预览会看到空白」，不要假装没问题。

质检按 C4 的判定标准处理。

### A6 · 交付

```
已生成 <输出路径>，包含 <N> 个工作表：<页签列表>。
结构：<一句话说明每张表做什么>
视觉：<主题名> 主题，<关键设计决策：表头着色/隔行条纹/数字格式/冻结/打印>
```

---

## 3. 脚本契约

三个脚本都以 JSON 输出到 stdout，**判定读 JSON 字段，不读退出码**。

### `scripts/theme_engine.py`

主题与样式的唯一实现，作为库被 `build.py` 和 `beautify.py` 共用。

```python
import sys
sys.path.insert(0, r"<SKILL_DIR>/scripts")
from theme_engine import apply_theme

apply_theme(wb, theme="business")     # 整本套主题，自动探测每张表的结构
```

常用函数：

| 函数 | 用途 |
|---|---|
| `apply_theme(wb, theme=..., **opts)` | 整本套主题，返回每表摘要 |
| `style_sheet(ws, theme, **opts)` | 单表套主题 |
| `detect_layout(ws) -> Layout` | 探测表头行 / 数据区 / 合计行 / 标题行 |
| `get_theme(name) -> Theme` | 取主题令牌（`.accent` `.surface` `.rise` 等） |
| `xl("#1F4E79")` | CSS 色转 openpyxl ARGB |
| `chart_rgb("#1F4E79")` | CSS 色转图表六位 RGB |
| `add_data_bar(ws, "E2:E50")` | 显式加数据条 |
| `add_color_scale(ws, "F2:F50")` | 显式加色阶 |
| `kpi_card(ws, "B2", 标签, 值, delta=..., number_format=...)` | 画概览/看板用的 KPI 卡片 |
| `mark_total_row(ws, row, layout)` | 合计行不以「合计」开头时手工标记 |

命令行：`python theme_engine.py --list-themes` / `--show business`。

### `scripts/beautify.py`

```
python beautify.py INPUT [-o OUT] [--theme T] [--level L] [--sheet NAME]...
                        [--data-bars E,H] [--dry-run] [--force] [--recalc]
                        [--recalc-only] [--report J]
```

`status` 取值：`ok` / `dry_run` / `blocked` / `success`（仅 `--recalc-only`）/ `error`。
退出码：0 = 成功或 dry_run，1 = 脚本错误或重算失败，2 = 风险闸门拦截。

### `scripts/qa_check.py`

```
python qa_check.py FILE [--report J]
```

`status` 取值 `pass` / `warn` / `fail`；退出码固定 0（除非脚本自身读不了文件）。
检查项：错误值、数字存成文本、空表头、重复表头、数据区合并单元格、列宽不足、
缺冻结、缺筛选、缺打印标题、公式无缓存值、长文本未换行、非法工作表名。
每条 issue 带 `code`、`sheet`、`cell`、`message`、`fix`。

---

## 4. 红线

1. **不覆盖源文件。** 美化默认另存，覆盖前必须备份并告知用户备份路径。
2. **数据正确性高于美观。** 不改值、不改公式语义、不删行列。只动样式、列宽、格式、
   对齐、冻结、筛选、打印设置。
3. **不静默降级。** 任何被跳过、被保守处理、被保留原样的部分，都要在交付话术里说清楚。
4. **含图表/图片/透视表的既有文件不用 openpyxl 往返。** 这是硬约束，不是建议。
5. **公式必须有缓存值才交付。** 否则用户在微信、邮件、飞书里预览会看到一片空白。
6. **`qa_check` 的 `fail` 不交付。**
7. **中文业务语境**：涨用红、跌用绿（与 A 股一致，非欧美习惯）；金额用 `¥`；
   日期 `yyyy-mm-dd`；数字右对齐、文本左对齐、日期居中。
8. **数据条、色阶、图标集只在用户确实要突出单一指标时加**，不为「看起来丰富」而加。

---

## 5. 错误处理

| 现象 | 处理 |
|---|---|
| `beautify.py` 返回 `blocked` | 改走 local-office-edit；用户坚持要重排则说明会丢失图表后加 `--force` |
| 探测的 `header_row` 明显不对 | 加 `--sheet` 限定单表重试；仍不对就改用 `conservative` 只调列宽与格式，并告知用户 |
| `qa_check` 报 `formula_cache_missing` | 加 `--recalc` 重跑；重算不可用时如实告知「Excel/WPS 打开会自动计算，第三方预览可能空白」 |
| `qa_check` 报 `number_as_text` | 说明会破坏 SUM/排序，建议回源修正；不要擅自改数据类型 |
| `qa_check` 报 `column_too_narrow` | 用 `beautify.py` 重算列宽；`--keep-widths` 会保留原宽，别在这个场景用 |
| `build.py` exit≠0 | 读 stderr 定位 openpyxl API 或坐标问题，改脚本重跑 |
| 主题名不认识 | 跑 `theme_engine.py --list-themes` 取合法值 |
