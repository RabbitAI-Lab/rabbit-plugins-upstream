---
name: pdf-to-word
description: 极速PDF转Word - 将PDF文档转换为Word格式，保留原文档的段落布局、表格和样式。支持企业安全策略环境，兼容加密文件。
agent_created: true
---

# pdf-to-word - 极速PDF转Word

> 将PDF文档快速转换为Word格式，保留原始布局和样式

## 功能特性

- **高保真转换**: 保留原文档的段落布局、表格、图片和样式
- **企业兼容**: 支持企业安全策略环境，兼容加密文件
- **批量处理**: 支持单页和多页PDF文档
- **快速转换**: 基于 PyMuPDF 引擎，转换速度快
- **智能解析**: 自动识别文本、表格、图片等元素

## 功能

- 将 PDF 文件转换为 Word (.docx) 格式
- 保留原文档的段落结构和布局
- 保留表格结构和数据
- 保留图片嵌入
- 支持企业加密环境下的文件转换
- 自动处理特殊编码和格式

---

## 激活条件

当用户提到以下关键词时激活：
- "PDF转Word"
- "PDF转docx"
- "转换PDF"
- "PDF文档转换"
- "极速PDF转Word"
- "pdf to word"

---

## 使用方法

### 通过 exec 工具调用

```bash
python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py <PDF文件路径> [输出Word路径]
```

### 示例

```bash
# 基本转换（输出到同目录）
python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py "E:\data\document.pdf"

# 指定输出路径
python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py "E:\data\document.pdf" "E:\output\document.docx"

# 转换加密文件
python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py "E:\secure\encrypted.pdf"
```

### 在 OpenClaw 中使用

```yaml
# 转换PDF为Word
exec:
  command: python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py "E:\data\document.pdf"
```

---

## 支持的文件格式

| 输入 | 输出 |
|------|------|
| **PDF** (.pdf) | **Word** (.docx) |

---

## 技术原理

| 组件 | 技术 |
|------|------|
| **PDF解析** | PyMuPDF (fitz) - 高性能PDF解析引擎 |
| **文档转换** | pdf2docx - 基于PyMuPDF的转换库 |
| **布局保留** | 智能段落识别和表格检测 |
| **编码处理** | UTF-8 编码，兼容多语言 |

---

## 依赖要求

首次使用前需要安装依赖：

```bash
pip install pdf2docx python-docx PyMuPDF
```

或在 WorkBuddy 环境中：

```bash
"C:/Users/CXX641/.workbuddy/binaries/python/versions/3.13.12/python.exe" -m pip install pdf2docx python-docx
```

---

## 注意事项

⚠️ **重要说明**:
- 本工具仅转换用户有权限访问的本地文件
- 不支持绕过合法的文件访问控制
- 适用于企业环境中授权的文件转换场景
- 文件需要能通过系统授权的应用程序正常打开
- 转换质量取决于原PDF文件的结构和质量
- 扫描版PDF（图片型）转换效果可能受限

---

## 法律说明

- 本工具仅用于转换用户有合法访问权限的本地文件
- 不支持绕过任何合法的文件访问控制或权限管理
- 用户应确保使用本工具符合所在组织的政策和法律法规
- 本工具通过标准的PDF解析库进行转换，不涉及破解或绕过加密

---

## 版本

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.0.0 | 2026-07-16 | 初始版本，支持PDF到Word的高保真转换 |
