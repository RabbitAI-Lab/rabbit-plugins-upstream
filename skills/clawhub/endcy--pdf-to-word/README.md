# pdf-to-word - 极速PDF转Word

将PDF文档快速转换为Word格式，保留原始布局和样式。支持企业安全策略环境，兼容加密文件。

## 功能

- 将 PDF 文件转换为 Word (.docx) 格式
- 保留原文档的段落结构和布局
- 保留表格结构和数据
- 保留图片嵌入
- 支持企业加密环境下的文件转换
- 自动处理特殊编码和格式

## 跨平台安装指南

### 平台兼容性

| 平台 | 兼容性 | 安装方式 |
|------|--------|----------|
| **WorkBuddy** | ✅ 完全兼容 | 复制到 `~/.workbuddy/skills/pdf-to-word/` |
| **OpenClaw** | ✅ 完全兼容 | 复制到 `D:\ai\workspace\skills\pdf-to-word/` |
| **Claude Code** | ✅ 完全兼容 | 复制到项目根目录或 `~/.claude/skills/pdf-to-word/` |

### WorkBuddy 安装

1. 将整个 `pdf-to-word` 目录复制到 WorkBuddy 技能目录：
   ```bash
   # Windows
   xcopy /E /I pdf-to-word "%USERPROFILE%\.workbuddy\skills\pdf-to-word"
   
   # macOS/Linux
   cp -r pdf-to-word ~/.workbuddy/skills/
   ```

2. 重启 WorkBuddy 或在对话中调用：`/pdf-to-word`

### OpenClaw 安装

1. 将整个 `pdf-to-word` 目录复制到 OpenClaw 技能目录：
   ```bash
   xcopy /E /I pdf-to-word "D:\ai\workspace\skills\pdf-to-word"
   ```

2. 通过 `exec` 工具调用：
   ```bash
   python D:\ai\workspace\skills\pdf-to-word\convert_pdf.py <PDF文件路径>
   ```

### Claude Code 安装

1. 方式一：项目级安装（推荐）
   ```bash
   # 将 pdf-to-word 目录复制到项目根目录
   xcopy /E /I pdf-to-word "项目根目录\pdf-to-word"
   ```

2. 方式二：全局安装
   ```bash
   # Windows
   xcopy /E /I pdf-to-word "%USERPROFILE%\.claude\skills\pdf-to-word"
   
   # macOS/Linux
   cp -r pdf-to-word ~/.claude/skills/
   ```

3. 在 Claude Code 中直接使用：`/pdf-to-word`

### 通用依赖安装

无论使用哪个平台，首次运行前都需要安装 Python 依赖：

```bash
pip install pdf2docx python-docx PyMuPDF
```

## 使用方法

### 命令行调用

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

## 输出

- **成功**: 生成Word文档，输出文件路径到 stdout
- **失败**: 输出错误信息到 stderr，退出码为 1

## 技术原理

- **PDF解析**: 使用 PyMuPDF (fitz) 高性能解析PDF文档结构
- **文档转换**: 使用 pdf2docx 库进行智能转换
- **布局保留**: 自动识别段落、表格、图片等元素并保留原始布局
- **编码处理**: UTF-8 编码，支持多语言内容

## 依赖

- Python 3.x
- pdf2docx >= 0.5.0
- python-docx >= 0.8.10
- PyMuPDF (fitz)

## 在 AI 智能体中使用

```python
import subprocess

def convert_pdf_to_word(pdf_path, output_path=None):
    """
    将PDF转换为Word文档
    
    Args:
        pdf_path: PDF文件路径
        output_path: 输出Word文件路径（可选，默认输出到同目录）
    
    Returns:
        输出文件路径
    """
    cmd = ['python', r'D:\ai\workspace\skills\pdf-to-word\convert_pdf.py', pdf_path]
    if output_path:
        cmd.append(output_path)
    
    result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        raise Exception(result.stderr)
    return result.stdout.strip()

# 使用示例
output = convert_pdf_to_word(r'E:\data\document.pdf')
print(f"转换完成: {output}")
```

## 注意事项

1. 文件路径使用绝对路径或正确的相对路径
2. 路径中的反斜杠需要转义或使用原始字符串
3. 本工具仅转换用户有权限访问的本地文件
4. 适用于企业环境中授权的文件转换场景
5. 文件需要能通过系统授权的应用程序正常打开
6. 转换质量取决于原PDF文件的结构和质量
7. 扫描版PDF（图片型）转换效果可能受限

## 支持的文件格式

| 输入 | 输出 |
|------|------|
| **PDF** (.pdf) | **Word** (.docx) |

## 法律说明

- 本工具仅用于转换用户有合法访问权限的本地文件
- 不支持绕过任何合法的文件访问控制或权限管理
- 用户应确保使用本工具符合所在组织的政策和法律法规
- 本工具通过标准的PDF解析库进行转换，不涉及破解或绕过加密
- 如果文件无法通过授权应用程序正常打开，本工具也可能无法转换
