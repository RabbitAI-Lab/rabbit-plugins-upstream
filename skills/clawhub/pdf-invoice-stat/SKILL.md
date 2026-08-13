# PDF 发票统计 Skill v2.3.0

基于 pdfplumber + PaddleOCR + PP-StructureV3 的本地提取方案，支持增值税电子发票（普通发票）、火车票、通行费等场景，输出格式化 Excel。

## 🆕 v2.0.0 更新（重大改进）

相比 v1.0.1 增量升级了 7 个本地版本（v2~v8）的改进：

- ✅ **修复通行费税额缺失 bug**：v1 把 `合 计` 正则贪婪匹配到 `价税合计` 跨行内容，导致通行费（金额和 `合 计` 分两行）税额=0
- ✅ **布局感知**：基于 pdfplumber 坐标分析，按 top 分组 + 邻近组合并
- ✅ **康熙字典 `**` → 生/海/消**：处理 PDF 渲染时的 `*生产生活服务*` 双星编码
- ✅ **水印页兜底**：发票号 / 日期 / 税号 在水印遮挡时自动 fallback
- ✅ **多税率留空**：同一张发票含多个税率时，税率列留空
- ✅ **命令行参数**：`python3 invoice_extractor.py <PDF> [输出.xlsx]`，不硬编码路径
- ✅ **支持更多场景**：通行费、火车票、增值税电子普票、餐饮、过路费等

## 功能特性

| 特性 | 说明 |
|------|------|
| 票据类型 | 增值税电子发票（普通发票）+ 铁路电子客票（火车票）+ 通行费 |
| 提取字段 | 发票号码、日期、购买方、销售方、税号、项目名称、金额、税率、税额、价税合计 |
| 输出格式 | Excel（15 列，冻结首行，会计格式）|
| 本地运行 | 纯 Python + pdfplumber，无外部 API |
| 多税率处理 | 多税率发票税率留空 |
| 免税/不征税 | 税额=0，税率列显示对应文字 |
| 水印页兜底 | 支持水印遮挡场景的发票号/日期/税号兜底提取 |
| 火车票 | 自动识别，金额=0，税率留空，项目名称=火车票 |
| 通行费 | 自动处理「合 计」跨行 bug |

## 使用方式

### 方式一：通过 ClawHub 安装（推荐）

```bash
clawhub install pdf-invoice-stat
```

### 方式二：直接使用脚本

```bash
python3 invoice_extractor.py <PDF路径> [输出Excel路径]
```

- `<PDF路径>`：必填，合并 PDF 文件路径
- `[输出Excel路径]`：选填，默认在同目录下生成 `<原文件名>_发票统计.xlsx`

### 运行示例

```bash
# 示例1：指定输出路径
python3 invoice_extractor.py /path/to/invoices.pdf /path/to/output.xlsx

# 示例2：使用默认输出路径（PDF 同目录）
python3 invoice_extractor.py /path/to/invoices.pdf
```

## 字段填写规则

### 税率/征收率

| 情形 | 填写内容 |
|------|---------|
| 单税率（如 3%、6%、13%）| 对应百分比 |
| 仅含"不征税"文字 | 不征税 |
| 仅含"免税"文字 | 免税 |
| 含多个不同税率 | 留空 |

### 税额

| 情形 | 填写内容 |
|------|---------|
| 免税/不征税 | 0 |
| 含税额 | 实际税额 |

### 火车票

- 金额 = 0
- 税率 = 留空
- 税额 = 0
- 销售方/销售方税号 = 留空
- 项目名称 = "火车票"
- **备注 = "票面价 ¥XX.XX"**（便于核对，火车票免增值税不进 Excel 金额合计）

**识别特征：** 含 `电子客票` / `中国铁路` / `国铁` / `12306` 字样时自动判定为火车票，按上述规则填字段。

## 依赖安装

```bash
# 必需依赖
pip3 install pdfplumber openpyxl

# v2.2.0 新增：纯图片发票 OCR（可选，但建议装）
pip3 install paddlepaddle>=3.0 paddleocr>=3.0
# 首次运行会自动下载模型到 ~/.paddlex/official_models/ (~180MB)

# v2.3.0 新增：纯图片发票 + 复杂版面（可选，按需装）
pip3 install "paddlex[ocr]"
# 首次运行会自动下载模型到 ~/.paddlex/official_models/ (~290MB)
# PP-StructureV3 含 Layout + Table Recognition
```

> **不装 PaddleOCR 也能用：** skill 默认用 pdfplumber 处理电子发票，只有遇到纯图片 PDF（扫描件、拍照）才需要 PaddleOCR fallback。

## 故障排查

| 问题 | 可能原因 | 解决方案 |
|------|---------|---------|
| 日期为空 | 水印页日期格式特殊 | 检查 PDF 水印样式，更新 `normalize_date` 兜底正则 |
| 税号为空 | 水印遮挡标签 | 检查 zone 扫描逻辑是否有新变体 |
| 项目名称为空 | `**` 误输入 | 检查 `parse_star_word` 双星处理逻辑 |
| 金额为 0 但非火车票 | 合汁行提取失败 | 检查金额正则匹配逻辑（v2.0.0 已修复通行费跨行 bug）|
| 通行费税额=0 | v1 版本的跨行 bug | 升级到 v2.0.0 |

## 更新日志

### v2.3.0 (2026-08-13)

- ✅ **集成 PP-StructureV3**（针对纯图片发票 + 复杂版面场景）
  - 新增 `pp_structure.py` 适配器（~315 行）
  - PP-StructureV3 = Layout Analysis + Table Recognition + OCR + 公式识别
  - 模型自动下载到 `~/.paddlex/official_models/`（额外 ~290MB）
  - 表格识别：HTML 格式输出，行/列结构精准
  - 字段抽取：发票号、日期、购方/销方、税号、金额、税率、税额、价税合计
- ⚠️ **依赖新增**：`paddlex[ocr]>=3.7`
- **优化**：`parse_html_table` 通用 HTML 表格解析器

### v2.2.0 (2026-08-13)

- ✅ **集成 PaddleOCR 3.7**（针对纯图片发票场景）
  - 新增 `paddle_ocr.py` 适配器（单例引擎）
  - 中文精准度 95%+（PP-OCRv6_medium 模型）
  - 火车票 OCR 置信度 0.988（实测）
  - 智能 fallback：pdfplumber 提取为空时自动用 PaddleOCR
- ✅ **火车票字段抽取升级**（用 OCR 结果的字段抽取）
  - 起点/终点/车次/席别/车厢座位/身份证/姓名 等
- ⚠️ **依赖新增**：paddlepaddle>=3.0 + paddleocr>=3.0（首次需下载 ~180MB 模型）

### v2.1.0 (2026-08-13)

- ✅ **新增：火车票自动识别**（按 SKILL.md 规则填字段）
  - 识别特征：含 `电子客票` / `中国铁路` / `国铁` / `12306` 字样
  - 字段填写：金额=0, 税率留空, 税额=0, 销售方/税号留空, 项目名称="火车票"
  - 备注自动填 "票面价 ¥XX.XX" 便于核对
  - 实现位置：`invoice_extractor.py` 第 184-200 行 (`get_page_info` 火车票分支)

### v2.0.0 (2026-08-11)
- ✅ **修复：通行费「合 计」跨行 bug**（负向断言 + 不跨行 group）
- ✅ 增量升级 v2~v8 本地版本的全部改进
- ✅ 新增命令行参数支持
- ✅ 新增康熙字典 `**` → 生/海/消 修复
- ✅ 新增水印页发票号/日期/税号兜底
- ✅ 新增多税率留空
- ✅ 布局感知（基于 pdfplumber 坐标分析）
- ✅ SKILL.md slug 修正：原本写错的 `pdf-vat-invoice-extractor` → 正确的 `pdf-invoice-stat`
- ✅ _meta.json author 修正：原本写错的"小伊" → 真正的作者 seairteng

### v1.0.1
- 支持增值税发票 + 火车票混合 PDF

## 版权

MIT-0 License. 作者 seairteng.
