# Skill: docx-writer — 标准学术文档生成

## 概述

通过 **bayoo-docx**（原生支持脚注的 python-docx 分支）+ **lxml** 生成符合学术规范的 Word 文档。脚注由库引擎原生创建，避免手工构造 OOXML 导致的格式问题。

## 前置条件

```powershell
pip install bayoo-docx lxml
```

## 文件管理

| 类型 | 路径 | 生命周期 |
|------|------|----------|
| SKILL 本体 | `skills/docx-writer/SKILL.md` | 长期 |
| 标准模板 | `skills/docx-writer/template.docx` | **不修改** |
| 持久脚本 | `skills/docx-writer/scripts/` | 长期 |
| 临时脚本 | `skills/docx-writer/tmp/scripts/` | 写入 log.md，2周清除 |
| 输出 | `skills/docx-writer/output/` | 用户确认后移到目标位置 |

## 引擎选择决策

| 需求 | 推荐 | 理由 |
|------|------|------|
| 创建含脚注的 docx | **bayoo-docx** | `paragraph.add_footnote()` 原生创建，编号/间距正确 |
| 格式化（字体/字号/缩进） | bayoo-docx + lxml | 字体用 `run.font` API，边框/样式用 lxml 微调 |
| 加载模板样式 | bayoo-docx | `Document(模板路径)` 继承模板的样式和页设置 |
| 脚注字体/字号设定 | 创建后遍历 `fn.findall('.//w:r')` | 显式设置 `w:sz=18` 和 `w:rFonts` |

**不要用的**：
- win32com（需要安装 Word，本环境没有）
- python-docx 原始版（无 `add_footnote`）
- 手工构造 `footnotes.xml`（编号/分隔线不可控）

---

## 生成流程

### 步骤 1：准备模板

SKILL 自带模板 `skills/docx-writer/template.docx`（已验证的初稿文件，含 Word 原生脚注）。该模板提供正确的 `footnote text`（样式ID=12）和 `footnote reference`（样式ID=20）样式。

脚本中引用方式：`TEMPLATE = os.path.join(SKILL_DIR, 'template.docx')`

### 步骤 2：编写内容

使用 `B('文本{F1}更多文本')` 语法，其中 `{F1}` 表示脚注。

**脚注编号规则**：
- 句号在前，脚注在后：`句子内容。{F1}` ✅
- 不可：`句子内容{F1}。` ❌

### 步骤 3：注册脚注文本

```python
FN_TEXT_MAP = {
    'F1': '作者. 标题. 期刊, 年份, 卷(期): 页码.',
}
```

### 步骤 4：排版函数

| 函数 | 用途 | 字体/字号 |
|------|------|-----------|
| `P(text, ...)` | 通用段落 | 宋体/TNR 10.5pt |
| `B(text)` | 正文 | 宋体/TNR 10.5pt |
| `Bs(text)` | 小字正文（摘要） | 宋体/TNR 9pt |
| `H1(text)` | 一级标题 | 黑体/Arial 12pt |
| `H2(text)` | 二级标题 | 黑体/Arial 12pt |
| `H3(text)` | 三级标题 | 黑体/Arial 10.5pt |
| `Tc(text)` | 表题/图题 | 宋体/TNR 9pt |
| `add_img(path, cap)` | 插入图片+图题 | 居中 |
| `add_tbl(h, rows)` | 三线表格 | 小五号 |

### 步骤 5：保存

```python
doc.save('输出路径.docx')
```

---

## 模板脚本

**不要自己写脚本。** 使用已有的已验证脚本：

| 文件 | 说明 | 路径 |
|------|------|------|
| `build_docx.py` | 空白模板，填空即用 | `skills/docx-writer/scripts/build_docx.py` |
| `build_final.py` | 已验证的完整终稿生成脚本 | `skills/docx-writer/scripts/build_final.py` |

使用方法：

1. 复制 `build_docx.py` 到目标目录
2. 修改顶部的配置（模板路径、输出路径、图片目录）
3. 修改 `FN_TEXT_MAP` 为实际脚注内容
4. 用 `B('文本{F1}')` 等函数编写正文内容
5. 运行

**不要修改排版函数**（`set_font`, `P`, `B`, `H1`, `H2`, `H3`, `Tc`, `add_img`, `add_tbl`），这些已经过验证。

---

## 排版规范（终稿样例标准）

### 页面设置
- 纸张：A4
- 页边距：上下 2.54cm，左右 3.18cm

### 字体字号行距总表

| 元素 | 中文 | 英文/数字 | 字号 | 对齐 | 缩进 | 行距 |
|------|------|----------|------|------|------|------|
| **文章标题** | 黑体 | Arial | 四号(14pt) | **居中** | 无 | 1.5倍 |
| **作者行** | 楷体 | Times New Roman | 五号(10.5pt) | **居中** | 无 | 1.5倍 |
| **摘要/关键词** | 宋体 | Times New Roman | **小五**(9pt) | 左对齐 | 首行缩进2字符 | 1.5倍 |
| **一级标题** | 黑体 | Arial | **小四**(12pt) | **居中** | **无** | 1.5倍 |
| **二级标题** | 黑体 | Arial | 小四(12pt) | 左对齐 | 首行缩进2字符 | 1.5倍 |
| **三级标题** | 黑体 | Arial | 五号(10.5pt) | 左对齐 | 首行缩进2字符 | 1.5倍 |
| **正文** | **宋体** | **Times New Roman** | **五号(10.5pt)** | 左对齐 | 首行缩进2字符 | **1.5倍** |
| **表题/图题** | 宋体 | Times New Roman | **小五(9pt)** | **居中** | **无** | 1.5倍 |
| **表内文字** | 宋体 | Times New Roman | 小五(9pt) | 居中 | — | 1.5倍 |
| **表注** | 宋体 | Times New Roman | 小五(9pt) | 左对齐 | 首行缩进2字符 | 1.5倍 |
| **脚注正文** | **宋体** | **Times New Roman** | **小五(9pt)** | 左对齐 | 无缩进 | **单倍行距** |
| **脚注编号（正文中）** | — | — | — | — | — | **上标** |

### 标题编号体系
- 一级标题：一、 二、 三、 四、
- 二级标题：（一）（二）（三）（四）
- 三级标题：1. 2. 3. 4.
- 四级标题：（1）（2）（3）（4）

### 脚注规范
1. **字体字号**：宋体/Times New Roman，**小五号(9pt)**，单倍行距
2. **上标**：正文中的脚注编号必须为上标（右上角）
3. **句号位置**：`句子内容。{F1}` — 句号在脚注标记**之前**，符点在前，注释号在后
4. **编号方式**：每页单独编号（Word 自动编号）
5. **分隔线**：仅在有脚注的页面显示，无需手动控制

### 表格规范
- 风格：**三线表**（仅上框线、下框线、表头下分割线，无内部竖线/横线）
- 表头：加粗
- 表内：居中对齐，小五号(9pt)
- 表题：在表格**上方**，居中，小五号(9pt)

### 图片规范
- 居中，无首行缩进
- 图题在图片**下方**，格式同表题

### 引用规范
- 全部使用**脚注**（注释体例），不设文末参考文献
- 顺序编号，格式遵循《清华大学学报（哲学社会科学版）》注释规范

### 常用代码对照

```python
def B(t):   return P(t)                              # 正文
def Bs(t):  return P(t, sz=Pt(9))                    # 小字
def H1(t):  return P(t, cn='黑体', en='Arial',       # 一级标题
                     sz=Pt(12), align='center', fi=None)
def H2(t):  return P(t, cn='黑体', en='Arial',       # 二级标题
                     sz=Pt(12))
def H3(t):  return P(t, cn='黑体', en='Arial',       # 三级标题
                     sz=Pt(10.5))
def Tc(t):  return P(t, sz=Pt(9), align='center',    # 表题/图题
                     fi=None)
```

### 脚本调用约定
- `B('文本{F1}')` — 正文带脚注，句号在脚注前
- `H1('一、标题')` — 一级标题
- `add_tbl(['列名'], [['数据']])` — 三线表
- `add_img('路径.png', '图1  标题')` — 图片+图题

## 编码规范

- **禁止使用全角空格**（`\u3000`）。正文缩进通过 `fi=Cm(0.74)` 控制，表格/标题用 `align` 参数控制。全角空格在不同字体和排版环境下表现不一致，会导致错位。
- 脚注编号与正文之间由 Word 自动处理，不要在脚本文本前加空格。

## 已知问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 脚注显示等线字体 | bayoo-docx 不自动设置中文字体 | 创建后遍历 `fn.findall('.//w:r')` 显式设 `rFonts`：`eastAsia=宋体, ascii=Times New Roman, hAnsi=Times New Roman` |
| 脚注五号字（应为小五） | 脚本文本 run 未设 `w:sz` | 显式设 `sz=18` 和 `szCs=18`（18 half-points = 9pt = 小五号） |
| 正文引用不上标 | bayoo-docx 的 `rStyle` 匹配不到模板的样式 ID | 后处理加 `vertAlign=superscript` |
| 句号位置 | 规范要求 `。{F1}` 而非 `{F1}。` | 写作时注意句号在脚注标记前 |
| 表格全框线 | `Table Grid` 样式默认全框 | 用 lxml 移除所有边框后加三线：header top、header bottom、last row bottom |
