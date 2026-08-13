# EPUB文件结构说明和样式规范

## EPUB基础结构

### 目录结构
```
EPUB文件（ZIP压缩包）
├── mimetype
├── META-INF/
│   └── container.xml
└── OEBPS/
    ├── content.opf
    ├── toc.ncx
    └── chapters/
        ├── chapter_001.xhtml
        ├── chapter_002.xhtml
        ├── style/
        │   └── default.css
        └── images/
            ├── cover.jpg
            └── figure_001.jpg
```

### 关键文件说明

#### mimetype
- 必须是第一个文件且未压缩
- 内容固定为：`application/epub+zip`

#### container.xml
- 定义了OPF文件的路径
- 示例：
```xml
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
```

#### content.opf
- 包含书籍的元数据、清单和spine
- 描述了书籍的所有组成部分

#### toc.ncx
- 导航控制文件（EPUB2）或nav.xhtml（EPUB3）
- 定义了书籍的目录结构

## 元数据规范

### 基础元数据
```xml
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
  <!-- 必需 -->
  <dc:title>书名</dc:title>
  <dc:identifier id="bookid">unique-id-12345</dc:identifier>
  
  <!-- 推荐 -->
  <dc:language>zh-CN</dc:language>
  <dc:creator>作者名</dc:creator>
  
  <!-- 可选 -->
  <dc:publisher>出版社</dc:publisher>
  <dc:date>2024-01-01</dc:date>
  <dc:description>书籍描述</dc:description>
  <dc:subject>主题分类</dc:subject>
  <dc:rights>版权信息</dc:rights>
</metadata>
```

### 元数据最佳实践
1. **标题**: 简洁明确，避免过长
2. **作者**: 使用真实姓名或常用笔名
3. **语言**: 使用标准的语言代码（zh-CN, en-US等）
4. **标识符**: 使用UUID或ISBN
5. **描述**: 100-500字的简介，便于搜索

## 内容组织规范

### 章节文件命名
```
chapter_001.xhtml  # 第一章
chapter_002.xhtml  # 第二章
...
chapter_999.xhtml  # 附录等
```

### 章节文件结构
```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>章节标题</title>
  <link rel="stylesheet" type="text/css" href="style/default.css"/>
</head>
<body>
  <h1>章节标题</h1>
  <div class="content">
    <p>段落内容...</p>
    <p>更多段落...</p>
  </div>
</body>
</html>
```

## CSS样式规范

### 基础样式框架
```css
/* 全局设置 */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: "PingFang SC", "Microsoft YaHei", "SimHei", serif;
  line-height: 1.8;
  margin: 1em;
  padding: 0;
  color: #333;
  background-color: #fff;
}
```

### 标题样式
```css
h1 {
  text-align: center;
  margin: 1em 0;
  font-size: 1.8em;
  color: #333;
  border-bottom: 2px solid #eee;
  padding-bottom: 0.5em;
  font-weight: bold;
}

h2 {
  margin: 1.5em 0 0.8em 0;
  font-size: 1.4em;
  color: #444;
  border-left: 4px solid #007bff;
  padding-left: 0.5em;
}

h3 {
  margin: 1.2em 0 0.6em 0;
  font-size: 1.2em;
  color: #555;
}
```

### 正文样式
```css
p {
  margin: 0.8em 0;
  text-align: justify;
  text-indent: 2em;
  font-size: 1em;
  line-height: 1.8;
  color: #333;
}

/* 首字下沉（可选） */
p:first-of-type::first-letter {
  font-size: 2em;
  font-weight: bold;
  float: left;
  margin-right: 0.1em;
  line-height: 1;
}
```

### 响应式设计
```css
/* 平板设备 */
@media screen and (max-width: 768px) {
  body {
    font-size: 16px;
    margin: 0.5em;
  }
  
  h1 {
    font-size: 1.6em;
  }
  
  h2 {
    font-size: 1.3em;
  }
}

/* 手机设备 */
@media screen and (max-width: 480px) {
  body {
    font-size: 14px;
    margin: 0.3em;
  }
  
  h1 {
    font-size: 1.4em;
  }
  
  p {
    text-indent: 1.5em;
    margin: 0.6em 0;
  }
}
```

## 图片处理规范

### 图片格式选择
- **封面**: JPEG（压缩率高，文件小）
- **插图**: PNG（质量好，支持透明）
- **照片**: JPEG（适合复杂色彩）
- **图表**: PNG或SVG（矢量图最佳）

### 图片尺寸规范
```css
/* 封面图片 */
img.cover {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}

/* 内联插图 */
img.figure {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
  border: 1px solid #ddd;
}

/* 图片标题 */
.figure-caption {
  text-align: center;
  font-style: italic;
  color: #666;
  margin-top: 0.5em;
  font-size: 0.9em;
}
```

### 图片优化建议
1. **分辨率**: 72-150 DPI（适合屏幕阅读）
2. **文件大小**: 单张图片控制在200KB以内
3. **格式**: 优先使用WebP格式（兼容性允许时）

## 目录结构规范

### 章节层级设置
```python
# 一级章节（主要标题）
level_1_chapters = [
    "第一章",
    "第二章",
    "第三章"
]

# 二级章节（子标题）
level_2_chapters = [
    "1.1 背景",
    "1.2 目标",
    "2.1 方法",
    "2.2 结果"
]

# 三级章节（小标题）
level_3_chapters = [
    "1.1.1 研究背景",
    "1.1.2 技术背景"
]
```

### 目录生成规则
1. **最大深度**: 不超过3级
2. **每级条目**: 每级至少2个条目
3. **标题长度**: 控制在30字以内
4. **链接格式**: 使用相对路径

## 特殊元素处理

### 表格样式
```css
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1em 0;
  font-size: 0.9em;
}

th, td {
  border: 1px solid #ddd;
  padding: 0.5em;
  text-align: left;
}

th {
  background-color: #f5f5f5;
  font-weight: bold;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}
```

### 代码块样式
```css
pre {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 1em;
  overflow-x: auto;
  font-family: "Courier New", monospace;
  font-size: 0.9em;
  line-height: 1.4;
}

code {
  background-color: #f5f5f5;
  padding: 0.2em 0.4em;
  border-radius: 3px;
  font-family: "Courier New", monospace;
  font-size: 0.9em;
}

pre code {
  background-color: transparent;
  padding: 0;
}
```

### 引用块样式
```css
blockquote {
  margin: 1em 0;
  padding: 0.5em 1em;
  border-left: 4px solid #007bff;
  background-color: #f9f9f9;
  color: #555;
  font-style: italic;
}

blockquote cite {
  display: block;
  text-align: right;
  font-size: 0.9em;
  color: #777;
  margin-top: 0.5em;
}
```

## 兼容性规范

### EPUB版本选择
- **EPUB 2.0.1**: 兼容性最好，推荐使用
- **EPUB 3.0**: 功能丰富，支持多媒体
- **EPUB 3.2**: 最新标准，但兼容性有限

### 设备兼容性测试
```
✅ 必须支持：
- iBooks (Apple)
- Google Play Books
- Kindle Fire
- Adobe Digital Editions

⚠️ 建议支持：
- Kobo
- Nook
- Sony Reader

❌ 不需要支持：
- 旧Kindle设备（不支持EPUB）
```

## 性能优化

### 文件大小控制
```python
# 推荐的文件大小限制
MAX_EPUB_SIZE = 50 * 1024 * 1024  # 50MB
MAX_IMAGE_SIZE = 200 * 1024         # 200KB per image
MAX_CHAPTER_SIZE = 500 * 1024       # 500KB per chapter
```

### 加载优化
1. **分章节加载**: 避免单文件过大
2. **图片懒加载**: 减少初始加载时间
3. **CSS压缩**: 去除空格和注释
4. **资源合并**: 合并小文件

## 质量检查清单

### 文件结构检查
- [ ] mimetype文件存在且正确
- [ ] container.xml路径正确
- [ ] content.opf包含所有必需元素
- [ ] toc.ncx目录结构完整
- [ ] 所有章节文件链接正确

### 内容质量检查
- [ ] 章节顺序正确
- [ ] 标题层级合理
- [ ] 图片显示正常
- [ ] 样式应用一致
- [ ] 无无效链接

### 兼容性检查
- [ ] 在多个阅读器中测试
- [ ] 不同屏幕尺寸下显示正常
- [ ] 字体回退机制工作
- [ ] 特殊字符正确显示

### 元数据检查
- [ ] 标题准确
- [ ] 作者信息完整
- [ ] 语言代码正确
- [ ] 标识符唯一
- [ ] 描述信息适当

## 错误处理

### 常见问题解决
1. **封面不显示**: 检查文件路径和MIME类型
2. **目录不工作**: 验证toc.ncx中的ID引用
3. **样式不应用**: 检查CSS路径和语法
4. **中文乱码**: 确保文件编码为UTF-8
5. **图片过大**: 压缩图片或降低分辨率

### 调试技巧
```python
# 使用ebooklib验证EPUB
from ebooklib import epub

try:
    book = epub.read_epub('book.epub')
    print("EPUB文件有效")
except Exception as e:
    print(f"EPUB文件无效: {e}")

# 检查特定元素
for item in book.get_items():
    print(f"{item.get_name()}: {item.get_type()}")
```