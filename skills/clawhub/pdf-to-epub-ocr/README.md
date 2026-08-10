# PDF转EPUB OCR技能

将扫描版PDF电子书通过OCR识别转换为结构化精排的EPUB格式电子书。

## 功能特点

- ✅ **智能OCR识别**: 使用Tesseract OCR引擎，支持中英文混合识别
- ✅ **封面提取**: 自动提取PDF第一页作为EPUB封面
- ✅ **文本清洗**: 去除页眉页脚、页码、水印等干扰内容
- ✅ **章节识别**: 自动识别章节标题，生成结构化目录
- ✅ **元数据管理**: 提取和写入书名、作者等元数据信息
- ✅ **移动优化**: 生成适合移动设备阅读的EPUB文件

## 系统依赖

### 必需的系统组件

1. **Tesseract OCR引擎**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
   
   # macOS
   brew install tesseract tesseract-lang
   
   # Windows
   # 下载安装: https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. **Poppler** (PDF处理库)
   ```bash
   # Ubuntu/Debian
   sudo apt-get install poppler-utils
   
   # macOS
   brew install poppler
   
   # Windows
   # 下载安装: https://github.com/oschwartz10612/poppler-windows/releases/
   ```

## Python依赖

安装Python依赖包：
```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python scripts/pdf_to_epub_converter.py your_book.pdf
```

### 高级用法

```bash
# 指定输出目录
python scripts/pdf_to_epub_converter.py your_book.pdf --output-dir ./output

# 指定书名和作者
python scripts/pdf_to_epub_converter.py your_book.pdf \
    --title "我的书籍" \
    --author "作者名"
```

### 在Agent中使用

当用户提到以下内容时，此技能会自动触发：
- "PDF转EPUB"、"PDF转电子书"
- "OCR提取PDF"、"扫描版PDF转换"
- "PDF结构化处理"
- 上传PDF文件要求转换为电子书格式

## 输出说明

### 输出文件
- **位置**: `output/`目录
- **文件名**: `{原文件名}_converted.epub`
- **格式**: EPUB 2.0.1（兼容性最好）

### 转换报告
每个转换任务会生成详细报告，包括：
- 总页数和识别成功页数
- OCR平均置信度
- 识别的章节数量
- 输出文件大小
- 处理时间统计

## 工作流程

1. **文件分析**: 验证PDF格式，提取元数据
2. **封面提取**: 转换第一页为封面图片
3. **OCR识别**: 逐页进行文字识别
4. **文本清洗**: 去除噪音内容
5. **章节识别**: 自动识别章节结构
6. **EPUB生成**: 创建结构化电子书文件
7. **质量验证**: 检查文件完整性

## 质量保证

### OCR质量
- 推荐DPI: 300-400
- 语言支持: 中英文混合
- 置信度监控: 自动统计识别准确率

### EPUB质量
- 结构验证: 自动检查EPUB结构完整性
- 兼容性测试: 支持主流阅读设备
- 响应式设计: 适配不同屏幕尺寸

## 故障排除

### 常见问题

**问题**: Tesseract not found
```bash
# 解决方案: 安装Tesseract OCR引擎
sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
```

**问题**: 识别准确率低
```bash
# 解决方案: 
# 1. 提高PDF扫描质量
# 2. 调整DPI设置（推荐300-400）
# 3. 使用预处理脚本增强图像
```

**问题**: 章节识别错误
```bash
# 解决方案: 
# 1. 检查章节标题格式
# 2. 在代码中添加自定义正则表达式
# 3. 手动调整章节划分
```

## 性能参数

### 典型处理时间（基于300 DPI）
- 简单文本PDF (100页): 2-3分钟
- 复杂排版PDF (100页): 5-8分钟
- 高质量扫描PDF (100页): 3-5分钟

### 硬件建议
- **CPU**: 多核处理器（4核以上）
- **内存**: 最低4GB，推荐8GB
- **存储**: SSD硬盘（显著提升I/O性能）

## 配置选项

### OCR配置
可在`scripts/ocr_processor.py`中调整：
- `dpi`: 图片转换分辨率（默认300）
- `language`: OCR语言（默认`chi_sim+eng`）
- `psm_mode`: 页面分割模式（默认6）

### 清洗配置
可在`scripts/text_cleaner.py`中调整：
- 章节标题识别模式
- 噪音文本过滤规则
- 文本清洗策略

### EPUB配置
可在`scripts/epub_generator.py`中调整：
- CSS样式文件
- 章节HTML模板
- 元数据设置

## 参考文档

- `references/ocr_best_practices.md`: OCR识别最佳实践
- `references/chapter_patterns.md`: 章节标题识别模式库
- `references/epub_structure_guide.md`: EPUB结构说明和样式规范

## 技术支持

如遇到问题，请检查：
1. 系统依赖是否正确安装
2. Python依赖包是否完整
3. PDF文件是否有效
4. 系统资源是否充足

## 许可证

本技能仅供学习和个人使用。使用时请遵守相关版权法律法规。

## 更新日志

### v1.0.0 (2024-08-07)
- ✨ 初始版本发布
- ✅ 支持基础PDF到EPUB转换
- ✅ OCR识别和文本清洗
- ✅ 章节自动识别
- ✅ 元数据管理