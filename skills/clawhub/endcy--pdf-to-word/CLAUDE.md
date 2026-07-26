# pdf-to-word - 极速PDF转Word

将PDF文档转换为Word格式，保留原文档的段落布局、表格和样式。支持企业安全策略环境，兼容加密文件。

## 功能特性

- **高保真转换**: 保留原文档的段落布局、表格、图片和样式
- **企业兼容**: 支持企业安全策略环境，兼容加密文件
- **批量处理**: 支持单页和多页PDF文档
- **快速转换**: 基于 PyMuPDF 引擎，转换速度快
- **智能解析**: 自动识别文本、表格、图片等元素

## 使用方法

### 基本用法

```bash
python convert_pdf.py <PDF文件路径> [输出Word路径]
```

### 示例

```bash
# 基本转换（输出到同目录）
python convert_pdf.py "E:\data\document.pdf"

# 指定输出路径
python convert_pdf.py "E:\data\document.pdf" "E:\output\document.docx"
```

## 依赖要求

```bash
pip install pdf2docx python-docx PyMuPDF
```

## 注意事项

- 本工具仅转换用户有权限访问的本地文件
- 转换质量取决于原PDF文件的结构和质量
- 扫描版PDF（图片型）转换效果可能受限
- 适用于企业环境中授权的文件转换场景

## 技术规格

- **转换引擎**: PyMuPDF + pdf2docx
- **支持格式**: PDF → DOCX
- **保留元素**: 段落、表格、图片、样式
- **编码**: UTF-8
