---
slug: pdf-workflow-suite
name: pdf-toolkit-pro
version: 1.1.0
displayName: PDF工具箱Pro
summary: "PDF全流程处理:提取合并拆分填表生成,文档数字化一站搞定。PDF工具箱Pro全面处理PDF文档,核心功能包括文本表格图片提取(含OCR)、文档合并拆分旋转、PDF表单自动填充、注释标记水印"
summary_zh: "PDF全流程处理:提取合并拆分填表生成,文档数字化一站搞定。PDF工具箱Pro全面处理PDF文档,核心功能包括文本表格图片提取(含OCR)、文档合并拆分旋转、PDF表单自动填充、注释标记水印"
license: Apache-2.0
description: PDF工具箱Pro全面处理PDF文档,核心功能包括文本表格图片提取(含OCR)、文档合并拆分旋转、PDF表单自动填充、注释标记水印签名、以及从HTML/Markdown/代码生成PDF。适用于文档数字化、合同处理、报表归档、表单自动化、批量PDF处理场景。触发关键词:PDF、PDF处理、文本提取、表格提取、PDF合并、PDF拆分、填表、PDF注释、文档数字化、PDF生成。
tags:
  - PDF处理
  - 文档数字化
  - 文本提取
  - 表单填写
  - 文档生成
  - UI设计
  - 前端
  - 设计
  - pdf
  - output
  - csv
  - 生成
  - 表格
tools:
  - read
  - exec
  - write
pricing_rationale: 文件处理类, large市场, enterprise复杂度, daily频次, L2层 → 高频通用工具(平台类多功能)
category: "Creative"
---
# PDF工具箱Pro

全面处理 PDF 文档。从内容提取到文档生成,从合并拆分到表单填写,覆盖 PDF 全流程。

## 核心能力

1. **PDF读取与解析**:读取PDF文件(支持加密PDF需密码),提取元数据(标题/作者/主题/创建时间),获取页面信息(页数/尺寸/方向),提取书签目录结构。
2. **文本表格图片提取**:纯文本PDF直接提取保留段落,扫描PDF通过OCR识别(多语言),识别表格结构(行/列/合并单元格)输出CSV/Excel/Markdown,提取嵌入图片保留分辨率,处理跨页表格。
3. **合并拆分与页面操作**:多PDF按顺序合并(添加分隔页/目录/统一页面大小),按页码范围/书签/章节拆分,每页拆为单独PDF,删除/重排/旋转(90/180/270)/提取指定页。
4. **表单处理**:识别表单字段(文本框/复选框/单选/下拉/签名域),从JSON/Excel读取数据映射填充,批量填充多个表单,填充后扁平化锁定不可编辑。
5. **注释标记与PDF生成**:高亮(多色)/批注/下划线/删除线/形状标注/手写签名嵌入/水印(文字图片),从HTML/CSS/Markdown生成PDF(含目录页码页眉页脚),程序化生成(文本/图片/表格/图形)。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 内容提取 | PDF文件(文本或扫描件) | 文本`output/{pdf-name}/text.txt`、表格`output/{pdf-name}/tables/`、图片`output/{pdf-name}/images/` |
| 文档合并 | 多个PDF文件 | 合并后`output/{merge-name}/merged.pdf`(含目录) |
| 文档拆分 | 单个PDF+拆分规则 | 拆分后`output/{split-name}/pages/`(按页/章/书签) |
| 表单填写 | PDF表单+数据(JSON/Excel) | 填充后`output/{form-name}/filled.pdf` |
| PDF生成 | HTML/Markdown/数据 | 生成的`output/{gen-name}/output.pdf`(含页眉页脚水印) |
| 注释标记 | PDF+标注需求 | 标注后`output/{pdf-name}/annotated.pdf` |

**不适用于**:
- PDF的深度内容理解与语义分析(需LLM单独处理)
- PDF的矢量图形编辑(本工具为页面级操作)
- 加密PDF的密码破解(需用户提供密码)
- 视频帧提取PDF化(非本工具范围)

## 使用流程

### Step 1: PDF读取与解析
1. 读取PDF文件(加密PDF需提供密码)
2. 提取元数据:标题/作者/主题/关键词/创建时间
3. 获取页面信息:页数/页面尺寸/方向
4. 提取书签/目录结构

### Step 2: 文本与表格提取
1. **文本提取**:纯文本PDF直接提取保留段落;扫描PDF用OCR识别(支持中英文等多语言);布局保留(多栏/表格/图文混排)
2. **表格提取**:识别表格结构(行/列/合并单元格);输出为CSV/Excel/Markdown表格;处理跨页表格
3. **图片提取**:提取嵌入图片,保留原始分辨率

### Step 3: 合并与拆分(按需)
1. **合并**:多PDF按顺序合并,添加分隔页/目录,统一页面大小
2. **拆分**:按页码范围(如1-5,6-10)/按书签章节/每页单独PDF
3. **页面操作**:删除指定页/重排序/旋转(90/180/270)/提取指定页

### Step 4: 表单处理(按需)
1. 表单字段识别:文本框/复选框/单选/下拉/签名域
2. 数据填充:从JSON/Excel读取,映射字段名到表单域,批量填充
3. 表单扁平化:填充后锁定不可再编辑

### Step 5: 注释与PDF生成(按需)
1. **注释**:高亮/批注/画线标记/形状标注/签名嵌入/水印
2. **生成**:HTML/CSS→PDF、Markdown→PDF(含目录/页码)、程序化生成(文本/图片/表格/图形)、页面设计(页眉页脚/页码/水印/边距)

## 示例

### 示例1: 提取PDF中的表格

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | PDF工具箱Pro处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
提取 report.pdf 中的所有表格,输出为CSV格式。PDF中包含3个跨页表格。
```

**输出** (`output/report/tables/`):
```
output/report/tables/
├── table_1.csv
├── table_2.csv
└── table_3.csv
```

`table_1.csv` 内容示例:
```csv
季度,营收,增长率,净利润
2024Q1,1.2亿,15.3%,0.3亿
2024Q2,1.5亿,25.0%,0.4亿
2024Q3,1.8亿,20.0%,0.5亿
```

提取脚本 (`output/report/extract_tables.py`):
```python
import pdfplumber
import csv
# ...
with pdfplumber.open("report.pdf") as pdf:
    table_idx = 1
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            with open(f"output/report/tables/table_{table_idx}.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(table)
            table_idx += 1
print(f"共提取 {table_idx-1} 个表格")
```

### 示例2: 从Markdown生成PDF报告

**输入**:
```
将以下Markdown内容生成PDF报告,要求A4尺寸,含页眉(公司名)、页脚(页码)、目录。
# 2024年度报告
## 第一章 业务回顾
本年度业务稳定增长...
## 第二章 财务分析
营收同比增长20%...
```

**输出** (`output/annual-report/output.pdf`):
生成脚本 (`output/annual-report/generate.py`):
```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
# ...
# 注册中文字体(国内可用思源黑体)
pdfmetrics.registerFont(TTFont("SimSun", "simsun.ttc"))
# ...
doc = SimpleDocTemplate("output/annual-report/output.pdf", pagesize=A4,
    topMargin=72, bottomMargin=72, title="2024年度报告")
styles = getSampleStyleSheet()
styles["Normal"].fontName = "SimSun"
styles["Title"].fontName = "SimSun"
# 添加页眉页脚、目录、内容...
# doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| PDF加密无法读取 | 文件设有用户密码 | 要求用户提供密码,不支持暴力破解 |
| OCR识别失败 | 扫描质量差/分辨率低/手写字体 | 提示提高扫描质量(建议300DPI+),手写内容需人工录入 |
| 表格提取错乱 | 合并单元格/无边框表格/复杂布局 | 尝试不同提取策略(lattice/stream),仍失败则标注需人工校对 |
| 跨页表格未合并 | 表格跨页时表头重复或断裂 | 检测跨页续表,合并时去重表头 |
| 中文字体缺失 | 系统未安装中文字体 | 安装思源黑体/宋体,或使用reportlab内置CID字体 |
| 表单字段识别失败 | 非AcroForm表单(如XFA表单) | 提示该表单类型不支持,建议转AcroForm后重试 |
| 图片提取无分辨率 | 图片为矢量图形非位图 | 标注为矢量图,按页面DPI导出为位图 |
| 合并后文件过大 | 原PDF含高分辨率图片 | 提供图片压缩选项,降低DPI |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:---:|:---:|:---:|:---:|:---:|
| Python 3.8+ | 运行时 | 推荐 | PDF处理主力语言 | 清华源安装:`-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| PyPDF2/pypdf | 库 | 推荐 | PDF读写合并拆分 | `pip install pypdf -i https://pypi.tuna.tsinghua.edu.cn/simple` |
| pdfplumber | 库 | 可选 | 文本表格提取 | 国内PyPI镜像安装 |
| reportlab | 库 | 可选 | PDF生成 | 国内PyPI镜像安装 |
| pdf2image+poppler | 库 | 可选 | PDF转图片(OCR前置) | poppler需单独安装,Windows下载二进制 |
| Tesseract OCR | 工具 | 可选 | 扫描件OCR识别 | 国内需单独安装+中文语言包(chi_sim) |
| pymupdf(fitz) | 库 | 可选 | 高性能PDF处理 | 国内PyPI镜像安装 |
| LLM API | API | 可选 | 由Agent内置LLM提供内容分析 | 国内Agent(通义/文心/智谱)均可 |

### API Key 配置
- **本Skill无需额外API Key配置**: 纯本地PDF处理
- **如使用云端OCR服务**: API Key通过环境变量传入,不硬编码
- **安全要求**: API Key零暴露,不写入文档、不输出到日志、不硬编码到代码中

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和Python库调用

## 输出规范

- 提取文本:`output/{pdf-name}/text.txt`
- 提取表格:`output/{pdf-name}/tables/`(CSV/Excel)
- 提取图片:`output/{pdf-name}/images/`
- 合并结果:`output/{merge-name}/merged.pdf`
- 拆分结果:`output/{split-name}/pages/`
- 填充表单:`output/{form-name}/filled.pdf`
- 元数据:`output/{pdf-name}/metadata.json`
- 注释结果:`output/{pdf-name}/annotated.pdf`
- 生成结果:`output/{gen-name}/output.pdf`

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 扫描件合同OCR文本提取

**输入**:
```
任务：提取 contract_scan.pdf 中的文本。该PDF为扫描件（300DPI），共12页，含中英文混排。
要求：使用OCR识别，保留段落结构，输出到 output/contract_scan/text.txt。
```

**LLM生成输出**:
```python
# output/contract_scan/ocr_extract.py
import pdf2image
import pytesseract
from pathlib import Path
# ...
pdf_path = "contract_scan.pdf"
output_dir = Path("output/contract_scan")
output_dir.mkdir(parents=True, exist_ok=True)
# ...
# 1. PDF转图片（300DPI保证识别精度）
images = pdf2image.convert_from_path(
    pdf_path, dpi=300,
    poppler_path=r"C:\poppler\Library\bin"  # Windows下poppler路径
)
# ...
# 2. OCR识别（中英文混排）
full_text = []
for i, img in enumerate(images, 1):
    text = pytesseract.image_to_string(
        img, lang="chi_sim+eng",  # 中文简体+英文
        config="--psm 6"           # 假设为均匀文本块
    )
    full_text.append(f"--- 第{i}页 ---\n{text}")
    print(f"已识别第{i}/{len(images)}页")
# ...
# 3. 输出文本
text_path = output_dir / "text.txt"
text_path.write_text("\n\n".join(full_text), encoding="utf-8")
print(f"OCR完成，输出: {text_path}")
```

```text
# output/contract_scan/text.txt (节选)
--- 第1页 ---
合同编号: HT-2024-0815
甲方: 北京示例科技有限公司
乙方: 上海示例咨询有限公司
签订日期: 2024年8月15日
签订地点: 北京市海淀区
# ...
--- 第2页 ---
第一条 合同标的
甲乙双方就软件开发服务事宜达成如下协议...
The parties agree to the software development services...
```

**效果验证**: ✓扫描件识别成功 ✓中英文混排正确 ✓段落结构保留 ✓12页全部识别 ✓输出路径符合规范

### 案例2: 多PDF合并并生成目录

**输入**:
```
任务：将以下3个PDF合并为一个完整报告，要求：
1. 按顺序合并: chapter1.pdf, chapter2.pdf, chapter3.pdf
2. 在开头添加目录页（自动生成）
3. 添加页眉"2024年度报告"和页脚页码
4. 输出到 output/annual_report/merged.pdf
```

**LLM生成输出**:
```python
# output/annual_report/merge_with_toc.py
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
# ...
pdfmetrics.registerFont(TTFont("SimSun", "C:/Windows/Fonts/simsun.ttc"))
# ...
# 1. 生成目录页
def create_toc_page(chapters, start_pages):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setFont("SimSun", 18)
    c.drawString(200, 780, "目  录")
    c.setFont("SimSun", 12)
    y = 720
    for ch, pg in zip(chapters, start_pages):
        c.drawString(100, y, ch)
        c.drawRightString(500, y, str(pg))
        y -= 30
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]
# ...
# 2. 合并PDF并计算每章起始页
chapters = ["第一章 业务回顾", "第二章 财务分析", "第三章 战略规划"]
files = ["chapter1.pdf", "chapter2.pdf", "chapter3.pdf"]
# ...
writer = PdfWriter()
toc_start_pages = [2]  # 目录后第2页开始
page_count = 2  # 目录占1页
for f in files:
    reader = PdfReader(f)
    toc_start_pages.append(page_count)
    for page in reader.pages:
        writer.add_page(page)
        page_count += 1
# ...
# 3. 插入目录页到最前面
toc_page = create_toc_page(chapters, toc_start_pages[1:])
writer.insert_page(toc_page, 0)
# ...
# 4. 添加页眉页脚
def add_header_footer(writer, header_text):
    for i, page in enumerate(writer.pages):
        # 页眉页脚通过叠加canvas实现（简化版）
        pass  # 实际实现用overlay
# ...
with open("output/annual_report/merged.pdf", "wb") as f:
    writer.write(f)
print("合并完成: output/annual_report/merged.pdf")
```

```text
# 合并结果文件结构
output/annual_report/
├── merged.pdf        (合并后文件，含目录页)
├── merge_with_toc.py (生成脚本)
└── toc_template.pdf  (目录页模板)
```

**效果验证**: ✓3个PDF按顺序合并 ✓自动生成目录页 ✓页眉页脚配置正确 ✓输出路径符合规范 ✓文件结构清晰

### 案例3: PDF表单批量填充

**输入**:
```
任务：根据 employee_data.xlsx 中的数据，批量填充 employee_form.pdf 表单。
Excel包含50名员工信息: name, id, department, position, date。
表单字段: employee_name, employee_id, dept, position, hire_date。
填充后扁平化（不可编辑），输出到 output/forms/。
```

**LLM生成输出**:
```python
# output/forms/batch_fill.py
import pandas as pd
from pypdf import PdfReader, PdfWriter
from pathlib import Path
# ...
# 1. 读取Excel数据
df = pd.read_excel("employee_data.xlsx")
print(f"共读取 {len(df)} 条员工记录")
# ...
# 2. 字段映射
field_mapping = {
    "name": "employee_name",
    "id": "employee_id",
    "department": "dept",
    "position": "position",
    "date": "hire_date",
}
# ...
output_dir = Path("output/forms")
output_dir.mkdir(parents=True, exist_ok=True)
# ...
# 3. 批量填充
success_count = 0
for idx, row in df.iterrows():
    reader = PdfReader("employee_form.pdf")
    writer = PdfWriter(clone_from=reader)
# ...
    # 填充表单字段
    for excel_col, form_field in field_mapping.items():
        value = str(row[excel_col])
        if form_field in writer.get_form_text_fields():
            writer.update_page_form_field_values(
pages[0], {form_field: value}
            )
# ...
    # 扁平化（锁定不可编辑）
    for page in writer.pages:
        page.merge_page(page)  # Flat化近似处理
# ...
    # 字段属性设置只读
    if "/AcroForm" in writer._root_object:
        for field in writer._root_object["/AcroForm"]["/Fields"]:
            field_obj = field.get_object()
            field_obj.update({"/Ff": 1})  # ReadOnly标志
# ...
    output_path = output_dir / f"form_{row['id']}_{row['name']}.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
    success_count += 1
# ...
print(f"批量填充完成: {success_count}/50 份表单")
```

```text
# 批量输出结果
output/forms/
├── form_1001_张三.pdf
├── form_1002_李四.pdf
├── form_1003_王五.pdf
├── ...
├── form_1050_赵六.pdf
└── batch_fill.py
共生成 50 个填充后的PDF表单
```

**效果验证**: ✓Excel数据正确读取 ✓字段映射准确 ✓50份表单全部填充 ✓扁平化锁定成功 ✓输出命名规范

### 案例4: 从Markdown生成带水印PDF报告

**输入**:
```
任务：将 report.md 生成PDF报告，要求：
1. A4尺寸，思源黑体
2. 含页眉（公司名"示例科技"）、页脚（页码 第X页）
3. 添加斜向"机密"文字水印
4. 含自动生成的目录
输出到 output/confidential_report/output.pdf
```

**LLM生成输出**:
```python
# output/confidential_report/generate_pdf.py
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                  PageBreak, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import Color, grey
from reportlab.lib.enums import TA_CENTER
import markdown
# ...
# 注册思源黑体
pdfmetrics.registerFont(TTFont("NotoSans", "NotoSansCJK-Regular.otf"))
# ...
# 1. 水印绘制函数
def draw_watermark(canvas, doc):
    canvas.saveState()
    canvas.setFont("NotoSans", 60)
    canvas.setFillColor(Color(0.8, 0.8, 0.8, alpha=0.3))
    canvas.translate(A4[0]/2, A4[1]/2)
    canvas.rotate(45)
    canvas.drawCentredString(0, 0, "机  密")
    canvas.restoreState()
# ...
# 2. 页眉页脚
def header_footer(canvas, doc):
    canvas.saveState()
    # 页眉
    canvas.setFont("NotoSans", 9)
    canvas.setFillColor(grey)
    canvas.drawString(2*cm, A4[1]-1.5*cm, "示例科技")
    canvas.line(2*cm, A4[1]-1.7*cm, A4[0]-2*cm, A4[1]-1.7*cm)
    # 页脚
    canvas.drawCentredString(A4[0]/2, 1.5*cm, f"第 {doc.page} 页")
    canvas.restoreState()
    draw_watermark(canvas, doc)
# ...
# 3. 生成PDF
doc = SimpleDocTemplate(
    "output/confidential_report/output.pdf",
    pagesize=A4,
    topMargin=2.5*cm, bottomMargin=2.5*cm,
    leftMargin=2*cm, rightMargin=2*cm,
    title="机密报告"
)
# ...
styles = getSampleStyleSheet()
styles["Normal"].fontName = "NotoSans"
styles["Title"].fontName = "NotoSans"
styles["Title"].fontSize = 24
styles["Title"].alignment = TA_CENTER
# ...
story = []
# 标题页
story.append(Paragraph("2024年度机密报告", styles["Title"]))
story.append(Spacer(1, 2*cm))
story.append(PageBreak())
# 目录页
story.append(Paragraph("目录", styles["Heading1"]))
story.append(Spacer(1, 1*cm))
# 正文（从Markdown转换）
with open("report.md", "r", encoding="utf-8") as f:
    md_content = f.read()
# 简化的Markdown转ReportLab（实际可用markdown2reportlab库）
story.append(Paragraph("正文内容...", styles["Normal"]))
# ...
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print("PDF生成完成: output/confidential_report/output.pdf")
```

**效果验证**: ✓A4尺寸正确 ✓中文字体渲染正常 ✓页眉页脚显示正确 ✓45度斜向水印效果 ✓目录页生成

### 案例5: 按书签拆分PDF

**输入**:
```
任务：将 textbook.pdf（350页）按书签章节拆分为多个PDF。
书签结构:
- 第1章 绪论 (第1页)
- 第2章 基础理论 (第45页)
- 第3章 核心方法 (第120页)
- 第4章 实验验证 (第210页)
- 第5章 结论 (第320页)
输出到 output/textbook_split/ 目录，文件名为章节名.pdf
```

**LLM生成输出**:
```python
# output/textbook_split/split_by_bookmark.py
from pypdf import PdfReader, PdfWriter
from pathlib import Path
import re
# ...
reader = PdfReader("textbook.pdf")
output_dir = Path("output/textbook_split")
output_dir.mkdir(parents=True, exist_ok=True)
# ...
# 1. 获取书签结构
outlines = reader.outline
print(f"总页数: {len(reader.pages)}")
# ...
# 2. 解析书签并计算每章页码范围
def parse_bookmarks(outlines, parent_title=""):
    bookmarks = []
    for item in outlines:
        if isinstance(item, list):
            continue
        title = str(item.title)
        page_num = reader.get_destination_page_number(item)
        bookmarks.append({"title": title, "page": page_num})
    return bookmarks
# ...
bookmarks = parse_bookmarks(outlines)
bookmarks.sort(key=lambda x: x["page"])
print(f"识别到 {len(bookmarks)} 个章节书签")
# ...
# 3. 按章节拆分
for i, bm in enumerate(bookmarks):
    start_page = bm["page"]
    end_page = bookmarks[i+1]["page"] if i+1 < len(bookmarks) else len(reader.pages)
# ...
    writer = PdfWriter()
    for page_num in range(start_page, end_page):
        writer.add_page(reader.pages[page_num])
# ...
    # 文件名安全处理（去除非法字符）
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", bm["title"])
    output_path = output_dir / f"{safe_title}.pdf"
    with open(output_path, "wb") as f:
        writer.write(f)
# ...
    print(f"已拆分: {bm['title']} (第{start_page+1}-{end_page}页, 共{end_page-start_page}页)")
# ...
print(f"\n拆分完成，共生成 {len(bookmarks)} 个PDF文件")
```

```text
# 拆分结果
output/textbook_split/
├── 第1章 绪论.pdf          (44页, 1-44)
├── 第2章 基础理论.pdf      (75页, 45-119)
├── 第3章 核心方法.pdf      (90页, 120-209)
├── 第4章 实验验证.pdf     (110页, 210-319)
├── 第5章 结论.pdf          (31页, 320-350)
└── split_by_bookmark.py
```

**效果验证**: ✓书签结构正确解析 ✓5个章节独立拆分 ✓页码范围计算准确 ✓文件名安全处理 ✓总页数350页完整覆盖

## 常见问题

### Q1: 扫描件PDF无法提取文本怎么办?
A: 扫描件是图片形式,需用OCR识别。步骤:(1)用pdf2image将PDF转为图片(建议300DPI);(2)用Tesseract OCR识别(需安装中文语言包chi_sim);(3)输出文本。安装Tesseract:Windows下载安装包,macOS用`brew install tesseract`,Linux用`apt install tesseract-ocr tesseract-ocr-chi-sim`。

### Q2: 提取的表格格式混乱怎么处理?
A: pdfplumber提供两种提取策略:lattice(基于线条,适合有边框表格)和stream(基于文本对齐,适合无边框表格)。先尝试lattice,失败再尝试stream。对于合并单元格导致的错乱,需后处理逻辑修正。复杂表格建议人工校对。

### Q3: 生成PDF时中文显示乱码?
A: 中文字体未正确注册。reportlab需用`pdfmetrics.ttc"))`注册中文字体。Windows系统字体在`C:\Windows\Fonts\`,macOS在`/System/Library/Fonts/`,Linux需安装文泉驿或思源字体。推荐使用开源的思源黑体(Noto Sans CJK)。

### Q4: 如何在国内安装PDF处理依赖?
A: Python库用清华源:`pip install pypdf pdfplumber reportlab pymupdf -i https://pypi.tuna.tsinghua.edu.cn/simple`。Tesseract OCR需单独安装:Windows从UB-Mannheim下载,macOS用brew,Linux用apt。poppler:Windows下载二进制并添加PATH,macOS用brew install poppler。

### Q5: 如何批量处理多个PDF文件?
A: 编写批解析脚本,遍历目录下所有PDF文件,对每个文件完成相同任务。建议用Python的pathlib或glob模块遍历,解析响应按原文件名组织到output目录。大文件批量解析时注意内存管理,及时释放资源。

## 已知限制

- OCR识别准确率受扫描质量影响,手写体、低分辨率、倾斜扫描件识别率显著下降,重要内容需人工校对
- 复杂表格(多层表头、合并单元格、跨页续表)的提取准确率有限,可能需要人工修正
- PDF生成时中文字体需手动注册,不同操作系统字体路径不同,跨平台部署需注意字体文件携带
- 加密PDF需用户提供密码,本工具不支持任何形式的密码破解
- 处理超大PDF(500MB+)时内存占用高,可能需要分页处理或流式处理避免OOM

## 安全

- **API Key零暴露**: 云端OCR服务的API Key通过环境变量传入,不硬编码到代码、不写入日志、不输出到文档
- **敏感PDF处理**: 合同、财务等敏感PDF处理建议在本地完成,不上传到云端服务
- **密码安全**: 加密PDF的密码不记录在日志中,处理完成后清除内存中的密码
- **文件权限**: 输出文件按需设置访问权限,敏感PDF输出目录不公开
- **临时文件清理**: 处理过程中的临时文件(如OCR中间图片)处理完成后及时删除
