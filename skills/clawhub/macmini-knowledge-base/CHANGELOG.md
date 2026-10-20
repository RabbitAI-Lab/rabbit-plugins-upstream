## v1.4.8 (2026-10-13) — 4 项健壮性修复

### 修复内容（来自 2026-10-13 凌晨任务）

1. **MuPDF/kreuzberg/OCR 异常不再静默吞掉**
   - `utils.py` 中 4 处 `except Exception: pass` 改为 `import sys; print(..., file=sys.stderr)` 记录错误
   - 涉及：extract_pdf_text (pymupdf 分支)、extract_pdf_via_ocr、extract_via_kreuzberg、_quick_page_check
   - 影响：之前 2 个 MuPDF 错误（高盛汇率、野村政策）现在能看到具体异常

2. **[:3000] 硬截断修复**
   - `run_analysis.py` 中 2 处 `f.read()[:3000]` 改为 `f.read()[:MAX_EXTRACT_LEN]`
   - MAX_EXTRACT_LEN = 500_000（与 SKILL.md 描述一致）
   - 影响：.md/.txt/.csv 等小文件不再被截断

3. **错误重试机制**
   - 新增 `retry_with_backoff(func, *args, max_retries=2, initial_delay=1.0)`
   - 退避策略：1s, 2s（指数）
   - PDF 提取调用已包 retry
   - 影响：临时性网络/IO 错误自动恢复

4. **clean_noise 噪音清理（v2.2.4）**
   - 新增 `clean_noise(text)` 函数，3 阶段处理：
     - 阶段 1: 在段落边界插换行（处理单行连续文本）
     - 阶段 1.5: 行级过滤（disclaimer 关键词）
     - 阶段 2: span-based 兜底（处理嵌入句中的关键词）
     - 阶段 2.5: 公式专项（"liability (in negligence...in whole or in part)" 等）
   - 已知 disclaimer 关键词：in whole or in part / to train or finetune / this foregoing restriction 等
   - 影响：投行研报摘要不再包含版权/机器学习训练限制等法律噪音
   - 实测：野村 PDF（31,980 → 29,144 字符，8.9% 删除，disclaimer 全部清除）
   - 实测：高盛 PDF（27,291 → 26,516 字符，2.8% 删除，disclaimer 全部清除）

### 文件变更
- `scripts/utils.py` (18585 → 21249 字符)
- `scripts/run_analysis.py` (8164 → 8500+ 字符，加 retry_with_backoff + clean_noise 调用)
- `SKILL.md` (description + 行为变化说明)
- `CHANGELOG.md` (本条)

### 兼容性
- 向后兼容：旧 knowledge/.analysis 目录升级后立即生效
- 不需要重新分析：现有 .summary.txt 仍是原文（可手动跑 re_clean_summaries.py 重清理）


# Changelog

## v1.4.7 (2026-08-17) — SKILL.md version 字段同步

- 修复 SKILL.md 顶部 version 字段（1.4.5 → 1.4.7）
- 与 _meta.json version 一致

## v1.4.6 (2026-08-17) — SKILL.md 修补
- 加"结构化权限声明"表格
- 修复 SKILL.md 顶部 version（1.4.2 → 1.4.5）

## v1.4.5 (2026-08-17) — NVIDIA SkillSpector 完整修复
### 元数据修复
### SKILL.md 修复
### setup.sh 改造（交互式）

## v1.4.4 (2026-08-17) — 仅 SKILL.md 补充
## v1.4.3 (2026-08-17) — 代码安全修复
## v1.4.2 (2026-08-17) — 仅元数据更新
