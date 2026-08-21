# Drawing Parser — 建筑图纸解析引擎

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/yfg305/drawing-parser)](https://github.com/yfg305/drawing-parser/stargazers)

> 建筑图纸智能解析工具，支持 DWG/DXF/PDF/图片格式，自动提取文字、段落、材料表、尺寸标注等结构化数据。

## ✨ 特性

- **多格式支持**：DWG、DXF、PDF、PNG、JPG
- **智能OCR**：四种OCR模式自动降级（PP-OCRv6 → deepdoc → RapidOCR → PaddleOCR）
- **结构化输出**：JSON格式，包含文字、段落、表格、尺寸标注
- **可视化分析**：支持图层截图、区域放大、距离测量
- **Hana集成**：可直接作为 HanaAgent 技能使用

## 📦 安装

### 1. 克隆仓库

```bash
git clone https://github.com/yfg305/drawing-parser.git
cd drawing-parser
```

### 2. 安装依赖

```bash
# 基础依赖
pip install -r requirements.txt

# 按需安装OCR模式
pip install rapidocr        # v6模式（推荐）
# 或
pip install onnxruntime opencv-python-headless  # dl模式
```

### 3. CAD 依赖（可选）

```bash
# 方法一：ODA File Converter（推荐）
# 下载地址：https://www.opendesign.com/guestfiles/oda_file_converter

# 方法二：AutoCAD（v3备用）
# 需要安装 AutoCAD 2026+
```

## 🚀 快速开始

### Python API

```python
from scripts.cad_parser import parse_cad_drawing
from scripts.pdf_parser import parse_pdf_drawing

# 解析 CAD 图纸
result = parse_cad_drawing('floor_plan.dwg', output_dir='./output')
print(f"提取文字: {len(result['texts'])} 条")
print(f"提取表格: {len(result['tables'])} 个")

# 解析 PDF 图纸
result = parse_pdf_drawing('elevation.pdf', ocr_mode='v6', output_dir='./output')
```

### 命令行

```bash
# 解析 CAD 图纸
python scripts/cad_parser.py floor_plan.dwg ./output --mode v4

# 解析 PDF 图纸（自动降级）
python scripts/pdf_parser.py elevation.pdf ./output --mode v6
```

## 📊 输出示例

```json
{
  "project_name": "示例项目",
  "source_file": "floor_plan.dwg",
  "parse_time": "2026-08-18T18:00:00Z",
  "texts": [
    {
      "content": "C30混凝土",
      "bbox": [100, 200, 300, 250],
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
      "rows": [
        ["钢筋", "HRB400", "120"],
        ["混凝土", "C30", "45m³"]
      ]
    }
  ],
  "dimensions": [
    {
      "value": 3600,
      "unit": "mm",
      "position": [500, 600]
    }
  ]
}
```

## 🔧 配置

编辑 `config.json`：

```json
{
  "ODA_PATH": "C:\\Program Files\\ODA\\ODAFileConverter.exe",
  "ACCONSOLE_PATH": "C:\\Program Files\\Autodesk\\AutoCAD 2026\\accoreconsole.exe",
  "OCR_MODE": "v6",
  "MAX_PAGES": 10,
  "OUTPUT_DIR": "./output"
}
```

## 📚 文档

- [SKILL.md](SKILL.md) - 技能描述和触发条件
- [scripts/](scripts/) - 核心解析脚本
- [examples/](examples/) - 使用示例
- [models/](models/) - OCR 模型文件

## 🤝 贡献

欢迎提 Issue 和 PR！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [ezdxf](https://github.com/mozman/ezdxf) - DXF 文件处理
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF 处理
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR 引擎
- [RapidOCR](https://github.com/RapidAI/RapidOCR) - 快速OCR
- [OpenDesign Alliance](https://www.opendesign.com/) - ODA File Converter

---

Made with ❤️ by [yfg305](https://github.com/yfg305)
