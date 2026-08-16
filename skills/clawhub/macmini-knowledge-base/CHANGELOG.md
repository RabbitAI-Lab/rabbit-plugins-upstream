# Changelog

## 1.4.1 (2026-08-12)

### Fixed
- **run_analysis.py**: `OSError: [Errno 63] File name too long` 修复
  - 新增 `sanitize_filename()` 函数（截断 + 8位 MD5 hash 防冲突，限额 200 bytes）
  - 主循环加 OSError 63 异常捕获 + 重试（max_length=180）
  - 触发场景：畸形 PDF 文件名（如 `_; filename_=utf-8''...` 双名拼接）超出 NAME_MAX=255 bytes

### Added
- **run_analysis.py**: `sanitize_filename()` 函数
- **run_analysis.py**: `SUMMARY_NAME_MAX = 200` 常量
- **run_analysis.py**: 异常捕获 Errno 63 重试逻辑
- **SKILL.md**: "summary 文件名 sanitize" 章节
- **SKILL.md**: "temp_docs 畸形文件清理" 章节
- **SKILL.md**: 避坑指南增加 sanitize 条目

### Cleanup
- 重命名 1 个畸形 PDF 文件（248 → 122 bytes）
- temp_docs: `20260730-Nomura-..._; filename_=utf-8''Nomura-...pdf` → `20260730-Nomura-...pdf`

## 1.4.0 (2026-08-12)

### Changed
- **utils.py**: `--skip-text` → `--force-ocr`（OCR 路径真正工作）
- **utils.py**: OCR 超时 60s → 600s
- **utils.py**: 文本提取上限 `[:8000]` → `MAX_EXTRACT_LEN = 500_000`

### Added
- **utils.py**: `is_cmap_broken()` CMap 残缺度自检
- **utils.py**: `PDFExtractError` / `ExtractError` 异常类
- **utils.py**: `ocr_office_via_ocr()` 通用 OCR 函数
- **scripts/**: 新增 `re_ocr_corrupted.py`
- **SKILL.md**: 新增"CMap 残缺度自检"章节

### Impact
- CMap 残缺: 40 → 0
- 文档完整度: 8K 字 → 500K 字上限

## 1.3.0 (2026-05-28)
- kreuzberg 统一提取层
- antiword 极速专线
- pandoc 依赖

## 1.2.1 (2026-05-22)
- utils.py 共享模块重构
- LibreOffice 熔断机制

## 1.2.0 (2026-05-21)
- 分批处理优化

## 1.1.0 (2026-05-13)
- 三步 PDF 处理

## 1.0.0 (2026-05-10)
- 初始版本
