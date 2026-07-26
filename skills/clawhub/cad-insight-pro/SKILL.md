---
slug: cad-insight-pro
name: cad-insight-pro
version: "1.0.0"
displayName: CAD洞察专家
summary: 同时解析 PDF 与 DWG 工程图，可配置标题栏模板、多比例检测、工程量自动统计。
license: MIT
description: |-
  CAD 洞察专家为 AI Agent 提供工程图纸智能分析能力，支持 PDF 与 DWG 两种格式，可提取标题栏、尺寸、标注、符号、比例并生成质量检查报告与工程量统计。它通过可配置的标题栏模板适配不同公司/标准的图框，通过多比例检测处理一张图多比例的情况，通过 OCR 管线处理扫描件，通过尺寸上下文关联还原尺寸与构件的对应关系。

  核心能力：PDF+DWG 双格式解析、可配置标题栏模板、多比例检测、符号库（可扩展）、OCR 扫描件支持、尺寸上下文关联、工程量自动统计、图纸索引生成、质量合规检查、Markdown 分析报告。

  适用场景：施工图算量、图纸质量审查、设计合规校验、项目图纸数字化归档、BIM 数据前置采集、一人公司承接设计审查。

  差异化：相比原始仅支持 PDF 且标题栏正则硬编码的方案，本技能新增 DWG 格式支持（via ezdxf）、可配置标题栏模板（适配各公司图框）、多比例检测（一张图多个 detail 不同比例）、符号库扩展机制、扫描件 OCR 管线、尺寸-构件关联、工程量自动统计、图纸集交叉索引。从"能解析单张 PDF"升级为"工程图纸全流程分析"。

  触发关键词：图纸分析, CAD, 施工图, 标题栏, 尺寸, 工程量, DWG, PDF, 算量, drawing, construction, takeoff, dimension
tags:
- 自动化
- 图纸分析
- 工程造价
tools:
- read
- exec
---

# CAD 洞察专家

把工程图纸里的标题栏、尺寸、标注、符号变成结构化数据，自动算量、查合规、出报告。本技能解决六个核心痛点：**格式单一**（原始只支持 PDF，DWG 是行业主流）、**标题栏不通用**（每家公司图框格式不同，硬编码正则必挂）、**多比例漏检**（一张图主图 1:100、详图 1:20，只取一个比例全错）、**符号库僵化**（原始只识别 schedule 表格，符号图例无法识别）、**扫描件无解**（光栅 PDF 无文字层，原始方案直接失效）、**算量缺失**（原始只提取不统计，无法直接用于造价）。

## 双格式支持（核心差异化）

| 格式 | 解析方式 | 依赖 | 适用 |
|:-----|:---------|:-----|:-----|
| PDF（矢量） | pdfplumber 提取文字层+表格 | pdfplumber | 原生数字图纸 |
| PDF（扫描） | OCR 提取文字 | pdfplumber + pytesseract | 老旧扫描归档 |
| DWG/DXF | ezdxf 读取实体与块 | ezdxf | AutoCAD 原文件 |

```python
from cad_insight import CadAnalyzer

analyzer = CadAnalyzer()

# 自动识别格式
result = analyzer.analyze("A101_Floor_Plan.pdf")    # PDF
result = analyzer.analyze("S200_Structural.dwg")    # DWG
result = analyzer.analyze("scanned_old.pdf", ocr=True)  # 扫描件
```

## 可配置标题栏模板（核心差异化）

原始方案用一套硬编码正则匹配标题栏，换家公司图框就失效。本技能支持模板配置：

### 内置标准模板

```python
# ANSI/美国标准
analyzer.load_titleblock_template("ansi")

# ISO/国际标准
analyzer.load_titleblock_template("iso")

# 中国国标
analyzer.load_titleblock_template("gb")
```

### 自定义模板

```json
// templates/company-a.json
{
  "name": "company-a",
  "regions": [
    {
      "field": "project_name",
      "keyword": "PROJECT",
      "pattern": "PROJECT(?:\\s*NAME)?:\\s*(.+?)(?:\\n|$)",
      "region": "top-right"
    },
    {
      "field": "sheet_number",
      "keyword": "SHEET",
      "pattern": "SHEET(?:\\s*NO)?\\.?:\\s*([A-Z]?\\d+(?:\\.\\d+)?)",
      "region": "bottom-right"
    },
    {
      "field": "scale",
      "keyword": "SCALE",
      "pattern": "SCALE:\\s*(.+?)(?:\\n|$)",
      "region": "bottom-left"
    }
  ],
  "discipline_map": {
    "A": "Architectural", "S": "Structural", "M": "Mechanical",
    "E": "Electrical", "P": "Plumbing", "C": "Civil"
  }
}
```

```python
analyzer.load_titleblock_template("templates/company-a.json")
```

### 模板自动匹配

若不指定模板，按优先级尝试：自定义 > 国标 > ISO > ANSI > 默认正则。匹配后输出置信度，低于阈值时提示"标题栏识别不确定，请指定模板"。

## 多比例检测（核心差异化）

原始方案只取第一个匹配的比例。实际工程图常有"主图 1:100，详图 1:20"的多比例情况。本技能检测所有比例并标注区域：

```python
scales = analyzer.detect_scales("A101.pdf")
```

```json
[
  {"scale": "1:100", "region": "full-sheet", "type": "main", "factor": 0.01},
  {"scale": "1:20",  "region": "detail-A",   "type": "detail", "factor": 0.05},
  {"scale": "1:5",   "region": "detail-B",   "type": "detail", "factor": 0.2}
]
```

比例识别模式：
- `1/4" = 1'-0"`（英制）
- `1:100`（公制）
- `NTS` / `NOT TO SCALE`（不按比例）
- 比例尺图形（扫描件，需图像识别）

## 尺寸提取与上下文关联（核心差异化）

原始方案只提取尺寸数值，不知道尺寸标在哪个构件上。本技能关联尺寸与邻近构件：

```python
dimensions = analyzer.extract_dimensions("A101.pdf", associate=True)
```

```json
[
  {
    "value": 360,
    "unit": "in",
    "raw": "30'-0\"",
    "type": "linear",
    "location": [120.5, 340.2],
    "associated_element": "wall-101",
    "associated_text": "WALL TYP.1"
  },
  {
    "value": 3.0,
    "unit": "m",
    "raw": "3000mm",
    "type": "linear",
    "location": [200.1, 150.8],
    "associated_element": "door-001",
    "associated_text": "DOOR D-01"
  }
]
```

尺寸模式识别：
- 英制：`10'-6"`, `10' - 6 1/2"`
- 公制：`3000mm`, `3.0m`, `120cm`
- 工程量：`150 SF`, `32 LF`, `12 CY`, `8 EA`

## 符号库（可扩展）

```python
# 加载符号库
analyzer.load_symbol_library("libraries/architectural.json")
analyzer.load_symbol_library("libraries/electrical.json")

# 识别符号
symbols = analyzer.extract_symbols("A101.pdf")
```

```json
[
  {"type": "door", "tag": "D-01", "width": 900, "location": [200, 150]},
  {"type": "window", "tag": "W-01", "width": 1200, "location": [300, 150]},
  {"type": "receptacle", "tag": "R-01", "circuit": "R1", "location": [250, 200]}
]
```

符号库格式（可自定义扩展）：

```json
// libraries/architectural.json
{
  "category": "architectural",
  "symbols": [
    {
      "type": "door",
      "patterns": ["D-\\d+", "DR-\\d+"],
      "properties": ["width", "height", "type", "swing"],
      "schedule_table": "door-schedule"
    },
    {
      "type": "window",
      "patterns": ["W-\\d+", "WIN-\\d+"],
      "properties": ["width", "height", "type", "glass"],
      "schedule_table": "window-schedule"
    }
  ]
}
```

## OCR 扫描件管线（核心差异化）

扫描件无文字层，原始方案直接失效。本技能提供 OCR 管线：

```python
# 扫描件分析（自动 OCR）
result = analyzer.analyze("scanned_1990.pdf", ocr=True)
```

OCR 管线流程：
1. pdfplumber 提取页面图像
2. 图像预处理（去噪、二值化、倾斜校正）
3. Tesseract OCR 提取文字
4. 用相同正则/模板解析
5. 标注"OCR 置信度"供人工复核

```python
result = analyzer.analyze("scanned.pdf", ocr=True)
for dim in result.dimensions:
    print(f"{dim.raw} (OCR置信度: {dim.confidence}%)")
```

## 工程量自动统计（核心差异化）

原始方案只提取不统计。本技能自动汇总工程量：

```python
takeoff = analyzer.quantity_takeoff("A101.pdf")
```

```markdown
## 工程量统计 - A101 底层平面图

### 门窗表
| 标签 | 类型 | 宽度 | 数量 | 备注 |
|:-----|:-----|:-----|:-----|:-----|
| D-01 | 单扇门 | 900mm | 6 | 防火门 |
| D-02 | 双扇门 | 1800mm | 2 | |
| W-01 | 推拉窗 | 1500mm | 8 | |

### 墙体
| 类型 | 长度 | 数量 |
|:-----|:-----|:-----|
| WALL TYP.1 | 30'-0" | 4 段 |
| WALL TYP.2 | 12'-0" | 6 段 |

### 面积统计
- 总建筑面积: 2,400 SF
- 房间数: 8

### 电气
| 类型 | 数量 | 回路 |
|:-----|:-----|:-----|
| 插座 | 24 | R1-R6 |
| 开关 | 12 | S1-S4 |
| 灯具 | 18 | L1-L3 |
```

## 质量合规检查

```python
issues = analyzer.check_quality("A101.pdf")
```

```markdown
## 质量检查报告

### 严重问题
- 标题栏缺少项目编号
- 缺少比例标注（详图 B）

### 警告
- 未发现一般说明（NOTE）
- 图号 A-101 与图纸索引不一致（索引为 A-101a）

### 合规检查（GB 标准）
- [x] 标题栏基本字段齐全
- [x] 尺寸单位统一（mm）
- [ ] 缺少图签日期
- [x] 图纸边界完整
```

## 图纸集交叉索引

多张图纸的标题栏汇总成索引：

```python
results = [analyzer.analyze(f) for f in ["A101.pdf", "A102.pdf", "S200.pdf"]]
index = analyzer.generate_drawing_index(results)
```

```markdown
# 图纸索引

| 图号 | 标题 | 专业 | 比例 | 版本 | 日期 |
|:-----|:-----|:-----|:-----|:-----|:-----|
| A-101 | 底层平面图 | 建筑 | 1:100 | C | 2026-06-15 |
| A-102 | 二层平面图 | 建筑 | 1:100 | B | 2026-06-15 |
| S-200 | 结构平面图 | 结构 | 1:50 | A | 2026-06-20 |

## 交叉引用检查
- A-101 引用详图 3/A-301 → A-301 存在 ✓
- S-200 引用 A-101 → 存在 ✓
- A-102 引用详图 7/A-401 → A-401 缺失 ✗
```

## 快速开始

### 安装

```bash
pip install pdfplumber ezdxf pytesseract pillow opencv-python
# OCR 需安装 Tesseract: https://github.com/tesseract-ocr/tesseract
# 中文: tesseract-ocr-chi-sim
```

### 基本用法

```python
from cad_insight import CadAnalyzer

analyzer = CadAnalyzer()
analyzer.load_titleblock_template("gb")           # 国标标题栏
analyzer.load_symbol_library("architectural.json") # 建筑符号库

# 分析单张
result = analyzer.analyze("A101_Floor_Plan.pdf")
print(f"图号: {result.title_block.sheet_number}")
print(f"标题: {result.title_block.sheet_title}")
print(f"比例: {result.title_block.scale}")
print(f"尺寸数: {len(result.dimensions)}")
print(f"符号数: {len(result.symbols)}")

# 工程量统计
takeoff = analyzer.quantity_takeoff("A101_Floor_Plan.pdf")
print(takeoff)

# 生成报告
report = analyzer.generate_report(result)
print(report)
```

### 批量分析图纸集

```python
import glob

analyzer = CadAnalyzer()
analyzer.load_titleblock_template("company-a.json")

results = []
for pdf in sorted(glob.glob("drawings/*.pdf")):
    try:
        r = analyzer.analyze(pdf)
        results.append(r)
    except Exception as e:
        print(f"跳过 {pdf}: {e}")

# 生成图纸索引
index = analyzer.generate_drawing_index(results)
# 导出为 CSV 供造价软件使用
analyzer.export_csv(results, "takeoff.csv")
```

## 数据结构

### TitleBlockData

```python
@dataclass
class TitleBlockData:
    project_name: str
    project_number: str
    sheet_number: str
    sheet_title: str
    discipline: str        # Architectural/Structural/Mechanical...
    scale: str
    date: str
    revision: str
    drawn_by: str
    checked_by: str
    approved_by: str
    confidence: float      # 模板匹配置信度 0-1
```

### Dimension

```python
@dataclass
class Dimension:
    value: float
    unit: str
    dimension_type: str    # linear/angular/radial
    raw: str               # 原始文本
    location: Tuple[float, float]
    associated_element: Optional[str]  # 关联构件
    associated_text: Optional[str]     # 关联标注
    confidence: float      # OCR 置信度（扫描件）
```

## 场景化指南

### 场景 A：施工图算量

```python
analyzer = CadAnalyzer()
analyzer.load_titleblock_template("gb")
analyzer.load_symbol_library("architectural.json")
analyzer.load_symbol_library("door-window.json")

takeoff = analyzer.quantity_takeoff("A101.pdf")
# 输出门窗表、墙体长度、面积统计，直接用于造价
```

### 场景 B：老旧图纸数字化

```python
# 扫描件 OCR 数字化
result = analyzer.analyze("scanned_1990.pdf", ocr=True)
# 低置信度项标记待人工复核
for item in result.low_confidence_items():
    print(f"需复核: {item.raw} (置信度 {item.confidence}%)")
```

### 场景 C：设计合规审查

```python
analyzer = CadAnalyzer()
analyzer.load_titleblock_template("gb")
analyzer.load_compliance_rules("gb-2024.json")  # 国标合规规则

issues = analyzer.check_compliance("A101.pdf")
for issue in issues:
    print(f"[{issue.severity}] {issue.rule}: {issue.description}")
```

### 场景 D：DWG 文件分析

```python
# 直接读 AutoCAD 原文件
result = analyzer.analyze("S200_Structural.dwg")
# ezdxf 提取实体、块、属性，比 PDF 更精确
print(f"钢筋标注: {len(result.annotations)} 条")
print(f"构件数: {len(result.symbols)} 个")
```

## FAQ

**Q：DWG 文件解析需要 AutoCAD 吗？**
A：不需要。本技能用 ezdxf 读 DXF/DWG，无需安装 AutoCAD。但加密的 DWG 可能需要先另存为 DXF。

**Q：扫描件 OCR 识别率低怎么办？**
A：① 确保安装中文语言包（chi_sim）；② 预处理图像（提高 DPI、去噪）；③ 低置信度项标记后人工复核；④ 清晰的矢量 PDF 不需要 OCR。

**Q：标题栏识别不准怎么办？**
A：① 用 `load_titleblock_template` 指定你公司的模板；② 自定义模板（参考模板格式）；③ 查看输出的 `confidence`，低于 0.7 时人工复核。

**Q：一张图有多个比例怎么处理？**
A：本技能的 `detect_scales` 返回所有检测到的比例及其区域。算量时按各自比例换算，不要全局用同一个比例。

**Q：能识别电气/暖通符号吗？**
A：能。加载对应符号库（`electrical.json`、`hvac.json`）。符号库可自定义扩展，按 JSON 格式添加。

**Q：工程量统计准确吗？**
A：矢量 PDF/DWG 的统计较准确。扫描件受 OCR 影响可能有误差，建议复核低置信度项。复杂构件（如弧形墙）可能需要人工补充。

**Q：能导出到造价软件吗？**
A：能。`export_csv` 导出标准 CSV，可导入广联达、鲁班等造价软件。也支持 Excel（`export_xlsx`）。

## 故障排查

| 症状 | 可能原因 | 处置 |
|:-----|:---------|:-----|
| 标题栏字段全空 | 模板不匹配 | 指定正确模板或自定义 |
| 尺寸数为 0 | 扫描件未开 OCR | `ocr=True` |
| DWG 读取失败 | 加密/新版本 | 另存为 DXF 或降版本 |
| OCR 乱码 | 语言包缺失 | 安装 chi_sim 语言包 |
| 比例检测错误 | 多比例未分别识别 | 用 `detect_scales` 看全部比例 |
| 符号不识别 | 符号库未加载 | `load_symbol_library` |
| 工程量偏差大 | 比例用错 | 确认每个区域的比例 |

## 性能优化

1. **批量分析**：一次加载多张，共享模板与符号库，减少重复初始化。
2. **缓存模板**：标题栏模板与符号库加载后缓存，避免每次读盘。
3. **区域限定**：DWG 分析时按图层过滤，只处理目标图层。
4. **OCR 降级**：批量分析时先试矢量提取，失败再 OCR，避免无谓 OCR 开销。
5. **并行处理**：多张图纸用多进程并行分析（`multiprocessing`）。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent
- **操作系统**：Linux / macOS / Windows
- **Python**：3.9+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| pdfplumber | Python 包 | PDF 必需 | `pip install pdfplumber` |
| ezdxf | Python 包 | DWG 必需 | `pip install ezdxf` |
| pytesseract | Python 包 | OCR 可选 | `pip install pytesseract` |
| Tesseract OCR | 系统程序 | OCR 必需 | 官方安装 + 中文语言包 |
| Pillow | Python 包 | 必需（图像） | `pip install pillow` |
| opencv-python | Python 包 | 推荐（图像处理） | `pip install opencv-python` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能为本地图纸分析，无需外部 API Key。
- OCR 功能需本地安装 Tesseract，无需 Key。
- 若需云端增强 OCR（如百度 OCR），需配置对应 API Key（可选，非必需）。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + Python 执行）
- **说明**：Agent 通过 Python API 驱动图纸分析，本技能负责格式解析、模板匹配、符号识别与工程量统计，结果以结构化数据/Markdown 报告输出。
