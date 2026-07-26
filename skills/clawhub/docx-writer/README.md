# docx-writer

标准学术文档生成技能，基于 **bayoo-docx**（原生支持脚注的 python-docx 分支）。脚注由库引擎原生创建，避免手工构造 OOXML 导致的编号错乱、字体缺失、上标失效等问题。

## 文件结构

```
docx-writer/
├── SKILL.md              # 完整排版规范 + 使用说明
├── template.docx         # 通用模板（含 footnote text 样式 ID=12）
├── scripts/
│   └── build_docx.py     # 填空即用的生成脚本
├── README.md
└── log.md
```

## 前置条件

```powershell
pip install bayoo-docx lxml
```

## 快速开始

1. 复制 `scripts/build_docx.py` 到工作目录
2. 修改配置：

```python
OUTPUT = r'输出路径.docx'
FIG_DIR = r'图片目录'

FN_TEXT_MAP = {
    'F1': '作者. 标题. 期刊, 年份, 卷(期): 页码.',
}
```

3. 在 `build_content()` 中编写正文：

```python
def build_content():
    H1('一、标题')
    B('正文内容。{F1}')
    Tc('表1  示例表格')
    add_tbl(['列A', '列B'], [['数据1', '数据2']])
```

4. 运行：

```powershell
python build_docx.py
```

## 排版函数

| 函数 | 用途 | 默认字体/字号 |
|------|------|-------------|
| `B(text)` | 正文 | 宋体/TNR 五号(10.5pt) |
| `Bs(text)` | 小字（摘要等） | 宋体/TNR 小五(9pt) |
| `H1(text)` | 一级标题 | 黑体/Arial 小四(12pt)，居中 |
| `H2(text)` | 二级标题 | 黑体/Arial 小四(12pt) |
| `H3(text)` | 三级标题 | 黑体/Arial 五号(10.5pt) |
| `Tc(text)` | 表题/图题 | 宋体/TNR 小五(9pt)，居中 |
| `add_img(path, cap)` | 插入图片 + 图题 | 居中 |
| `add_tbl(headers, rows)` | 三线表 | 小五(9pt)，仅上下框线 |

## 脚注语法

- **句号在前**：`句子内容。{F1}` ✅
- **不可**：`句子内容{F1}。` ❌
- 字体/字号/上标由脚本自动处理，不需要手动设置。

## 排版规范

| 元素 | 规格 |
|------|------|
| 纸张 | A4，上下 2.54cm，左右 3.18cm |
| 正文 | 宋体/Times New Roman，五号 10.5pt，1.5倍行距，首行缩进2字符 |
| 标题一级 | 黑体/Arial，小四 12pt，居中 |
| 标题二/三级 | 黑体/Arial，小四/五号，首行缩进2字符 |
| 脚注 | 宋体/TNR，小五 9pt，单倍行距，上标编号 |
| 三线表 | 仅上框线 + 下框线 + 表头下分割线 |
| 表题 | 表格上方，居中，小五 9pt |
| 图题 | 图片下方，居中，小五 9pt |

## License

MIT
