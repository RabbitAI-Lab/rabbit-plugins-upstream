---
name: document-pro
version: 1.1.0
description: "Extract key information from PDF, DOCX, PPT and other documents"
tags: [documentation, frontend, file-based, visual, memory-based]
dependencies:
  python:
    - pdfplumber
    - pypdf
    - python-docx
    - python-pptx
    - openpyxl
    - pandas
---

# Document Pro - 文档处理技能

## 概述

赋予 AI 强大的文档处理能力：
- PDF 读取与提取
- Word 文档解析
- PowerPoint 提取
- Excel 数据提取
- 文档格式转换

## 触发场景

1. 用户发送文档并要求"分析"或"总结"
2. 用户要求"提取文档内容"
3. 用户要求"转换为 PDF"
4. 用户询问文档中的具体信息
5. 用户要求"从报告/论文中提取要点"

## 支持的格式

| 格式 | 读取 | 写入 | 工具 |
|------|------|------|------|
| PDF | ✅ | ✅ | pdfplumber, pypdf, reportlab |
| DOCX | ✅ | ✅ | python-docx |
| PPTX | ✅ | ✅ | python-pptx |
| XLSX | ✅ | ✅ | openpyxl |
| TXT | ✅ | ✅ | 内置 |
| Markdown | ✅ | ✅ | 内置 |

## 工具使用

### PDF 处理

```python
# 提取文本
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)

# 提取表格
with pdfplumber.open("document.pdf") as pdf:
    table = pdf.pages[0].extract_tables()
```

### Word 文档

```python
from docx import Document

doc = Document("document.docx")
for para in doc.paragraphs:
    print(para.text)

# 提取表格
for table in doc.tables:
    for row in table.rows:
        print([cell.text for cell in row.cells])
```

### PowerPoint

```python
from pptx import Presentation

prs = Presentation("presentation.pptx")
for slide in prs.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            print(shape.text)
```

### Excel 数据

```python
import openpyxl

wb = openpyxl.load_workbook("data.xlsx")
ws = wb.active

for row in ws.iter_rows(values_only=True):
    print(row)
```

## 工作流程

```
1. 识别文档类型 → 选择正确的工具
2. 读取内容 → 提取文本、表格、图片
3. 分析信息 → 理解结构、提取要点
4. 总结呈现 → 用中文总结给用户
```

## 进阶功能

### 文档摘要
- 提取文档主要观点
- 生成简短摘要
- 列出关键要点

### 表格处理
- 识别表格结构
- 提取表格数据
- 转换为 CSV/Excel

### 关键词提取
- 找出重要名词/术语
- 识别主题
- 提取关键信息

## 输出格式

向用户呈现文档时：
- 文档类型和页数
- 主要内容摘要
- 关键要点（3-5条）
- 建议的后续操作

## 错误处理

### 常见问题与解决方案

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| PDF 文本为空 | 扫描件/图片型 PDF | 使用 OCR（pytesseract + pdf2image） |
| Word 表格丢失 | 复杂嵌套表格 | 使用 `python-docx` 的 `table.rows` 遍历 |
| PPT 图片无法提取 | 嵌入方式不同 | 检查 `shape.shape_type`，使用 `Image` 对象 |
| Excel 日期格式错误 | 序列号未转换 | 使用 `openpyxl` 的 `dateutil` 解析 |
| 编码乱码 | 文件编码非 UTF-8 | 尝试 `gbk`、`latin1` 等编码 |
| 文件损坏 | 下载不完整或格式错误 | 尝试用 Office 软件修复，或重新获取文件 |

### 依赖检查脚本

```python
def check_document_dependencies():
    """检查文档处理依赖是否可用"""
    missing = []
    
    packages = {
        'pdfplumber': 'PDF 文本提取',
        'pypdf': 'PDF 基础操作',
        'docx': 'Word 文档处理',
        'pptx': 'PowerPoint 处理',
        'openpyxl': 'Excel 处理',
    }
    
    for package, desc in packages.items():
        try:
            __import__(package)
        except ImportError:
            missing.append(f"{package} ({desc})")
    
    if missing:
        print("缺少以下依赖：")
        for m in missing:
            print(f"  - {m}")
        print(f"\n安装命令: pip install {' '.join(p.split()[0] for p in missing)}")
        return False
    
    print("所有文档处理依赖已就绪！")
    return True
```

### 降级策略

```
文档处理优先级：
1. 专用库（pdfplumber/python-docx/python-pptx）→ 最佳效果
2. 通用库（pypdf/内置读取）→ 基础功能
3. 命令行工具（pdftotext/libreoffice）→ 最后手段
4. 提示用户手动转换 → 无法处理时
```

## 与其他技能的关系

- **pdf 技能**：更专注于 PDF 的高级操作（合并、拆分、加密、表单填充）
- **docx 技能**：更专注于 Word 文档的创建和复杂排版
- **pptx 技能**：更专注于 PPT 的生成和设计
- **本技能**：侧重于文档内容的提取、分析和总结，是文档处理的"入口"技能

## 限制

- 扫描件 PDF 需要 OCR
- 复杂格式可能丢失
- 图片/图表无法完全理解

---

## 任务完成后

完成任务后，做任务总结，将操作记录更新到 record.md 中。

---

*Version 1.0.1 — 增加任务完成后更新record.md规则*
