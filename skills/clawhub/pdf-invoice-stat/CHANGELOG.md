# Changelog

## 2.3.0 (2026-08-13)

### Added
- **PP-StructureV3 集成**（针对纯图片发票 + 复杂版面场景）
  - 新增 `pp_structure.py` 适配器（~315 行）
  - PP-StructureV3 = Layout Analysis + Table Recognition + OCR + 公式识别
  - 模型自动下载到 `~/.paddlex/official_models/`（额外 ~290MB）
  - 表格识别：HTML 格式输出，行/列结构精准
  - 字段抽取：发票号、日期、购方/销方、税号、金额、税率、税额、价税合计
- **通用 HTML 表格解析器** `parse_html_table`
- **PP-Structure 智能 fallback 路径**：pdfplumber + PaddleOCR 都失败时启动

### Changed
- **依赖新增**：`paddlex[ocr]>=3.7`

## 2.2.0 (2026-08-13)
- 集成 PaddleOCR 3.7
- 火车票字段抽取升级

## 2.1.0 (2026-08-13)
- 火车票自动识别

## 2.0.0 (2026-08-11)
- 修复通行费税额缺失 bug
- 布局感知
- 康熙字典 `**` 修复
- 水印页兜底
- 多税率留空
