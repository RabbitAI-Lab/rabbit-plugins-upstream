# 设计系统（Excel Studio）

本文件是**视觉与版式的权威口径**，`scripts/theme_engine.py` 是它的唯一实现。
写建表脚本时不要另造数值——所有颜色、字号、行高、边框都从本文件取，
或直接调 `apply_theme()` 让引擎套上去。

---

## 1. 三条原则

**① 信息密度优先，留白服务于对齐。**
不加无意义的整行留白、不把行高撑到 30 以上。让 40 行数据一屏看完，比每行都松松垮垮
更有专业感。留白只用在三处：标题与表头之间、表格与脚注之间、页边距。

**② 单轴对齐。**
一列只允许一种对齐方式。数字右对齐、文本左对齐、日期居中——这条被打破时，
表格立刻显得业余，比配色难看更致命。公式列要按该列的数字格式判断它是数字还是文本，
不能因为「值是字符串 `=SUM(...)`」就当文本左对齐。

**③ 色不过三。**
一份工作簿里同时出现的颜色（不含黑灰白）不超过三种：主色 + 语义色（涨/跌/预警）。
表头一个主色块，其余靠留白与细线分隔。渐变、阴影、立体感一律不用。

---

## 2. 色彩

### 2.1 四套主题

| 主题 | accent 主色 | 适用 |
|---|---|---|
| `business` 商务蓝 | `#1F4E79` | 默认。对外汇报、管理层周报、财务 |
| `graphite` 石墨灰 | `#334155` | 低饱和，适合排版密集的运营台账 |
| `emerald` 松石绿 | `#0F5132` | 生产、库存、质量、供应链制造侧 |
| `amber` 琥珀棕 | `#92400E` | 项目计划、进度跟踪、人力预算 |

每套主题包含以下令牌（`theme_engine.THEMES` 为完整定义）：

| 令牌 | 用途 |
|---|---|
| `accent` | 表头底色、标题下划线、合计行上下边线、页签色 |
| `accent_light` | 数据条、色阶端点、图表次要系列 |
| `accent_text` | 表头文字（恒为白） |
| `surface` | 合计行底色、KPI 卡片底 |
| `band` | 隔行条纹底色 |
| `grid` | 边框线色 |
| `text` | 正文色 |
| `muted` | 次要文字：副标题、脚注、单位、说明 |
| `rise` / `fall` | **涨 / 跌**（见 2.2） |
| `warn` / `info` | 预警 / 提示 |

### 2.2 语义色方向：涨红跌绿

按中国业务习惯（与 A 股一致）：

- `rise` = 红色（`#C0392B` 系）：增长、超目标、有利差异
- `fall` = 绿色（`#1E8449` 系）：下降、未达标、不利差异

若用户明确要求国际习惯（红=坏、绿=好）或其他配色体系，以用户要求为准，并在交付话术中
说明已切换。

负值单元格的负数着色用数字格式自带能力（`[Red]-¥#,##0.00`），不要另设字体颜色——
两者叠加会出现双色冲突。

### 2.3 色值写法

设计稿里统一写 CSS `#RRGGBB`。落代码时：

```python
from theme_engine import xl, chart_rgb

XL_PRIMARY = xl("#1F4E79")      # → "FF1F4E79"，用于单元格样式
CHART_BLUE = chart_rgb("#1F4E79")  # → "1F4E79"，用于图表 API
```

不要在调用点重复转换，不要手工补 `00` 透明度前缀。

---

## 3. 字体与字号

西文与中文统一用 **Microsoft YaHei**（微软雅黑）。不混用宋体、Calibri、苹方。

| 层 | 字号 | 字重 | 颜色 | 行高 |
|---|---|---|---|---|
| 标题（表名） | 16 | Bold | `text` | 34 |
| 副标题 / 口径说明 | 10 | Regular | `muted` | 20 |
| 表头 | 11 | Bold | `accent_text`（白） | 30 |
| 正文 | 10 | Regular | `text` | 22 |
| 合计行 | 10（bold 档 11） | Bold | `text` | 22（强调档 28） |
| 脚注 | 9 | Regular | `muted` | 18 |

规则：

- 正文字号不要小于 9。9 号已是「能读」的下限。
- 同一张表只允许出现两级字重（Regular / Bold）。Medium、Semibold 在 Excel 里表现不稳定。
- 保留源表已有的加粗与斜体（那是用户的强调意图），只统一字体族、字号、字色。

---

## 4. 行高与列宽

- 行高按 §3 表固定，不做逐行自适应。
- 列宽由内容决定：`max(表头宽, 内容最大显示宽, 公式列估算宽) + 3`（带数字格式的列 + 4）。
- 列宽区间 **8 ~ 42**。超过 42 说明这列该换行或该拆列，而不是继续加宽。
- 东亚字符按 2 个宽度计（`theme_engine.display_width` 已处理）。
- 内容宽度 > 34 的文本列开启 `wrap_text`，行高按内容行数调整。
- 公式列读不到结果值，按格式估算：货币 13、百分比 8、整数 10、小数 11 字符。
  这一步不能省——漏了就会出现合计行满屏 `###`。

---

## 5. 边框与分隔

只画必要线，靠留白分隔区块。

| 位置 | 线型 | 颜色 |
|---|---|---|
| 标题下缘 | medium（2px） | `accent` |
| 表头下缘 | medium | `accent` |
| 数据行之间 | thin（≤60 行）或 hair（>60 行） | `grid` |
| 数据列之间 | 默认不画；列数 ≥ 12 时用 thin | `grid` |
| 合计行上缘 | thin | `accent` |
| 合计行下缘 | medium | `accent` |
| 无合计行时的表尾 | medium | `accent` |

- 不做全包围网格。外框只在需要「表格感」时用，且只用主色。
- 合并单元格只允许出现在标题区，不进数据区。

---

## 6. 数字格式决策表

按**表头语义**优先，样本值兜底。

| 表头关键词 | 格式串 | 说明 |
|---|---|---|
| 率 / 占比 / 比例 / 同比 / 环比 / 增长 | `0.0%` | 值须为 0–1 的小数；若是 85 表示 85%，先除以 100 |
| 金额 / 单价 / 价 / 额 / 成本 / 收入 / 费用 / 利润 / 预算 / 应收 / 应付 / 余额 | `¥#,##0.00;[Red]-¥#,##0.00` | 负数自动红字，不再设字体色 |
| 数量 / 件数 / 个数 / 人数 / 次数 / 天数 / 工时 / 产量 / 销量 | `#,##0` | 整数千分位 |
| 日期 / 时间（值为 date/datetime） | `yyyy-mm-dd`；带时分则 `yyyy-mm-dd hh:mm` | 值必须是 `datetime` 对象，不能是字符串 |
| 单号 / 编号 / 编码 / 代码 / 料号 / 批次 / 序列号 | `@`（文本） | 保持文本，避免前导零丢失与科学计数 |
| 其余数值 | 全整数 `#,##0`，含小数 `#,##0.00` | |

纪律：

- 已有自定义格式（用户手工设过的）**一律保留**，只覆盖 `General` 与日期类格式。
- 数字存成文本是硬伤：`SUM`、排序、条件格式全会失效。发现就报，不要偷偷转类型。
- 单位不要塞进数字格式（如 `0.0"%"`），用独立表头或脚注写单位。

---

## 7. 对齐

| 类型 | 水平 | 垂直 | 换行 |
|---|---|---|---|
| 表头 | 居中 | 居中 | 是 |
| 数字（含公式产出的数字） | 右 | 居中 | 否 |
| 文本 | 左 | 居中 | 长文本是 |
| 日期 | 居中 | 居中 | 否 |
| 合计行 | 跟随该列类型 | 居中 | 否 |

**公式单元格的对齐取决于它产出的类型，不取决于它当前是字符串。** 判断依据：该列推断出的
数字格式。有数字格式 → 右对齐；无 → 左对齐。

---

## 8. 冻结、筛选、打印

- **冻结**：数据行 > 0 时冻在表头下方。列数 ≥ 7 且首列是文本标识（单号/客户/物料）时，
  同时冻结首列。
- **筛选**：数据行 > 20 且数据区没有合并单元格时，在表头行加 AutoFilter。
  合计行必须在筛选范围之外。
- **打印**：
  - 列数 > 6 → 横向，否则纵向；A4。
  - `fitToWidth=1`，`fitToHeight=0`（按页宽压缩，纵向不限页）。
  - 表头行设为 `print_title_rows`，跨页重复。
  - 页边距 左右 0.4"、上下 0.75"、页眉 0.3"、页脚 0.35"。
  - 页脚左 `&A`（表名）、右 `&P / &N`（页码）。
  - 水平居中。
- **网格线**：关闭工作表网格线（`showGridLines = False`），靠边框表达结构。
- **页签色**：设为 `accent`，多表时给不同页签用不同主题色区分层级。

---

## 9. 图表

只在「趋势」与「对比」两种意图下加图。明细表不配图。

| 意图 | 图型 | 注意 |
|---|---|---|
| 时间趋势 | 折线图 | 不超过 3 条系列；关闭数据点标记；X 轴按时间排序 |
| 类别对比 | 条形图（横向） | 类别 > 6 个时用横向，标签才不会挤 |
| 占比构成 | 环形图 | 类别 ≤ 5；其余归入「其他」 |
| 目标达成 | 条形图 + 目标线 | 目标线用 `fall`/`warn` 色虚线 |

样式口径：

- 系列色按主题 `series` 顺序取，第一个系列用 `accent`。
- 图例：系列 > 1 时放底部；单系列不要图例。
- 标题写明「指标 + 口径 + 时间范围」，不要只写「图表1」。
- 关闭纵向网格线；保留横向浅色网格线。
- 数据标签只在系列 ≤ 12 个数据点时开。
- 图表锚点放在数据区右侧或下方，不与表格重叠，不遮表头。

---

## 10. KPI 卡片

概览页与看板页的核心组件，用 `theme_engine.kpi_card()` 画，不要手工拼合并单元格。

```python
kpi_card(ws, "B2", "在制工单", 128, delta="+12 环比", theme="emerald")
kpi_card(ws, "F2", "本月完成", 4392, delta="-3.2% 环比", theme="emerald")
kpi_card(ws, "B6", "齐套率", 0.964, delta="+1.8pt", number_format="0.0%")
```

结构（占 `span` 列 × 3 行，默认 span=3）：

| 行 | 内容 | 字号 | 高 |
|---|---|---|---|
| 1 | 标签 | 9 muted | 20 |
| 2 | 数值 | 24 Bold text | 40 |
| 3 | 变化幅 | 10 rise/fall | 18 |

口径：

- 卡片底色 `surface`，左侧一条 `accent` 竖线作视觉锚点，其余三边 `grid` 细线。
- 变化幅按首字符判方向：`+` → `rise`（红），`-` → `fall`（绿），否则 `muted`。
- **一个概览页 4–6 张卡，不要超过 6 张**。超过就说明没想清楚哪个指标最重要。
- 卡片之间留 1 列空列，不要紧贴。
- 一张卡片只放一个数字。放两个数字等于没放。

---

## 11. 反模式

以下做法会让表「看起来做了很多，实际更难读」，一律避免：

- ❌ 每个单元格都加边框，形成蜘蛛网
- ❌ 表头用渐变填充或多色块
- ❌ 正文用 11 号以上，一屏只看得到 15 行
- ❌ 隔行条纹与数据条同时用在同一列
- ❌ 金额列不给货币格式，只靠表头写「(元)」
- ❌ 合并单元格跨越数据区
- ❌ 用空格对齐，不用单元格对齐
- ❌ 空表头列（透视和筛选都会失效）
- ❌ 合计行放在筛选范围内
- ❌ 一张表塞 20 列还硬要 A4 纵向
- ❌ 全列居中对齐（数字居中最难扫读）
- ❌ 给每个数字加数据条

---

## 12. 建表脚本骨架

照抄后替换 `build_sheets()` 的内容。这份骨架已经把「先 import 缺了才装」「颜色归一」
「末尾一次性套主题」三件事处理好，不要重写。

```python
import subprocess
import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "openpyxl>=3.1.0"])
    import openpyxl

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

SKILL_DIR = Path(r"<SKILL_DIR>")
sys.path.insert(0, str(SKILL_DIR / "scripts"))
from theme_engine import apply_theme, get_theme  # noqa: E402

THEME = get_theme("business")
OUT = Path(r"<output_xlsx>")


def build_sheets(wb: Workbook) -> None:
    """按 layout_patterns.md 的蓝图建表。只写内容与结构，不刷样式。"""
    ws = wb.active
    ws.title = "明细"

    # 1) 标题区
    ws["A1"] = "2026年11月 生产工单执行明细"
    ws.merge_cells("A1:H1")

    # 2) 表头（行号先算好，作为后续所有公式的锚点）
    headers = ["工单号", "产品名称", "计划数量", "完成数量", "完成率", "计划完成日期", "单位成本", "工单金额"]
    HEADER_ROW = 3
    for i, h in enumerate(headers, start=1):
        ws.cell(row=HEADER_ROW, column=i, value=h)

    # 3) 数据区
    rows = [
        ("MO-001", "伺服电机壳体", 1200, 1180, "2026-11-08", 36.5),
        ("MO-002", "减速机端盖", 800, 800, "2026-11-09", 52.0),
    ]
    FIRST = HEADER_ROW + 1
    for offset, (code, name, plan, done, due, cost) in enumerate(rows):
        r = FIRST + offset
        ws.cell(row=r, column=1, value=code)
        ws.cell(row=r, column=2, value=name)
        ws.cell(row=r, column=3, value=plan)
        ws.cell(row=r, column=4, value=done)
        # 除法一律带零值保护，不要只在注释里写
        ws.cell(row=r, column=5, value=f'=IF(C{r}=0,"",D{r}/C{r})')
        ws.cell(row=r, column=6, value=due)
        ws.cell(row=r, column=7, value=cost)
        ws.cell(row=r, column=8, value=f"=D{r}*G{r}")

    # 4) 合计行（由锚点推导，不写死行号）
    TOTAL = FIRST + len(rows)
    ws.cell(row=TOTAL, column=1, value="合计")
    ws.cell(row=TOTAL, column=3, value=f"=SUM(C{FIRST}:C{TOTAL - 1})")
    ws.cell(row=TOTAL, column=4, value=f"=SUM(D{FIRST}:D{TOTAL - 1})")
    ws.cell(row=TOTAL, column=5, value=f'=IF(C{TOTAL}=0,"",D{TOTAL}/C{TOTAL})')
    ws.cell(row=TOTAL, column=8, value=f"=SUM(H{FIRST}:H{TOTAL - 1})")

    # 5) 脚注（引擎会自动降级为 9 号灰字）
    ws.cell(row=TOTAL + 2, column=1,
            value="注：完成率 = 完成数量 / 计划数量；工单金额 = 完成数量 × 单位成本。")


def main() -> None:
    wb = Workbook()
    build_sheets(wb)
    wb.properties.title = OUT.stem
    apply_theme(wb, theme=THEME)          # 关键：样式只在这一处落地
    OUT.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT)
    print(f"written: {OUT}")


if __name__ == "__main__":
    main()
```

要点：

- 不要在 `build_sheets()` 里写 `Font(...)` / `PatternFill(...)`。写了会被 `apply_theme`
  覆盖，白费功夫；需要例外样式时用引擎暴露的 `add_data_bar` / `mark_total_row` 等函数。
- `apply_theme` 会自己探测表头行、合计行、脚注行，所以不要求固定行号，
  但**你的公式必须和真实行号一致**——锚点还是得自己算。
- 日期写成 `datetime` 对象（`datetime(2026, 11, 8)`），不要写字符串，
  否则数字格式不起作用。
