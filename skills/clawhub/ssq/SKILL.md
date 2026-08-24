---
name: drawing-parser
description: "建筑图纸解析引擎。支持 DWG/DXF/PDF/图片格式的图纸解析，提取文字、段落、材料表、尺寸标注等结构化数据。用户提及'解析图纸''读图''CAD解析''PDF解析'时触发。"
metadata:
  version: "1.0.0"
  author: "yfg305"
  license: "MIT"
  tags: ["建筑", "图纸解析", "CAD", "PDF", "OCR"]
---

# Drawing Parser — 建筑图纸解析引擎

自动识别图纸格式（DWG/DXF/PDF/图片），调度对应解析管线，输出结构化数据供方案编制和审核使用。

## 支持的格式

| 格式 | 子引擎 | 技术方案 | 精度 |
|:----|:------|:---------|:----:|
| `.dwg` | CAD管线 | ODA转换→DXF→ezdxf | 高 |
| `.dxf` | CAD管线 | ezdxf 直接读取 | 高 |
| `.pdf` | PDF管线 | PyMuPDF + 多模式OCR | 高 |
| `.png/.jpg` | PDF管线 | 同上，三种OCR可选 | 高 |

## OCR 模式对比（PDF/图片）

| 模式 | 技术栈 | 精度 | 速度 | 依赖 |
|:----|:--------|:---:|:----|:----|
| `v6`（推荐） | PP-OCRv6 rapidocr | 最高 | 较快 | pip install rapidocr |
| `dl` | deepdoc ONNX | 高 | 较慢 | onnxruntime, opencv |
| `rapid` | RapidOCR-json.exe | 高 | 较快 | 仅需exe |
| `fast` | PaddleOCR-json.exe | 够用 | 快 | 仅需exe |

## 快速开始

### Python API

```python
import sys
sys.path.insert(0, 'path/to/scripts')

# CAD 图纸解析
from cad_parser import parse_cad_drawing
result = parse_cad_drawing('图纸.dwg', output_dir='./output')

# PDF 图纸解析
from pdf_parser import parse_pdf_drawing
result = parse_pdf_drawing('图纸.pdf', ocr_mode='v6', output_dir='./output')
```

### 命令行

```bash
# CAD 解析
python scripts/cad_parser.py 图纸.dwg ./output --mode v4

# PDF 解析（自动降级 v6→dl→rapid→fast）
python scripts/pdf_parser.py 图纸.pdf ./output --mode v6
```

## 输出结构

所有解析结果写入 `{项目}/_drawing_parser/project_data.json`：

```json
{
  "project_name": "示例项目",
  "source_file": "图纸.dwg",
  "parse_time": "2026-08-18T18:00:00Z",
  "texts": [
    {
      "content": "钢筋混凝土",
      "bbox": [x1, y1, x2, y2],
      "layer": "TEXT",
      "confidence": 0.95
    }
  ],
  "paragraphs": [
    {
      "type": "title",
      "content": "结构设计说明",
      "position": 1
    }
  ],
  "tables": [
    {
      "header": ["材料", "规格", "数量"],
      "rows": [["钢筋", "HRB400", "120"]]
    }
  ],
  "dimensions": [
    {
      "value": 3600,
      "unit": "mm",
      "position": [x, y]
    }
  ]
}
```

## 依赖安装

### 基础依赖（所有模式）

```bash
pip install pymupdf ezdxf openpyxl numpy matplotlib
```

### CAD 管线（v4主力）

```bash
# ODA File Converter（免费，需手动下载安装）
# 下载地址：https://www.opendesign.com/guestfiles/oda_file_converter

# 或 AutoCAD（v3备用管线）
# 需要安装 AutoCAD 2026+
```

### PDF 管线

```bash
# v6 模式（推荐）
pip install rapidocr

# dl 模式
pip install onnxruntime opencv-python-headless
# 模型文件：models/deepdoc/（已内置）

# rapid / fast 模式
# exe 文件已内置在 scripts/ocr_service/
```

## 故障排查

| 问题 | 解决方案 |
|:----|:--------|
| ODA 路径异常 | 更新 config.json 中的 ODA_PATH |
| ezdxf 版本冲突 | `pip install ezdxf==1.4.4` |
| LISP 脚本失效 | 检查 dwg_extract_v2.lsp 路径配置 |
| v4 管线失败 | 切 v3（accoreconsole+LISP） |
| OCR 模型缺失 | 从 hf-mirror.com 下载 PP-OCRv6 模型 |
| 内存不足 | 降低 max_pages 参数 |

## 版本历史

- v1.0.0（2026-08-18）：初始开源版本
  - 支持 DWG/DXF/PDF/图片四种格式
  - 四模式OCR自动降级
  - 结构化JSON输出

## 许可证

MIT License - 可自由使用、修改、分发

## 贡献

欢迎提 Issue 和 PR。请确保：
1. 代码符合 PEP 8 规范
2. 新增功能附带测试用例
3. 更新 CHANGELOG.md
