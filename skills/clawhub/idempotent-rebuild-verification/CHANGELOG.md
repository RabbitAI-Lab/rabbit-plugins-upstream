# Changelog

## v2.0.0 — 2026-09-06

**形态变更**：从纯散文提示词（v1.0.6：5 个 md、约 11KB）升级为确定性 CLI 工具包
（`scripts/rebuild_verify.py` 纯标准库 + `scripts/selftest.py` 12 组离线自检）。
散文保留为规则/根因参考（references/），可执行语义全部代码化。

新增（全部 v1 缺失）：
- `verify`：7 类漂移分类（ok / trailing_newline_drift / crlf_drift / html_error_page /
  truncated_paste / content_change / unknown）+ 尺寸钉扎（size_ok / size_mismatch），
  每条带 next_action；v1 内联片段只覆盖"单个尾部换行"，现在覆盖 1..N 个尾部换行、
  CRLF、HTML 错误页、截断、同尺寸改动。
- `manifest`：批量校验，每行 `path sha256 [size]`，rc 0/2/3，缺失文件进 missing 列表。
- `pins`：runbook 钉扎提取（行号、所属标题、引用文件、围栏内外）。
- `extract-steps`：CommonMark §4.5 正确的块切分（内嵌围栏不再静默截断载荷），
  heredoc 终止核查，suspect 标记，`--write-steps` 字节精确落盘 + steps.json。
- `wipe-audit`：快照擦除后 5 类扫描 + 4 态判定 + 步骤路由建议（clean /
  normal_post_wipe / pre_wipe_or_full / scripts_missing_too）。
- `gen-fixtures`：确定性测试夹具（无时间戳/随机，sha256 可复现）。
- 退出码纪律：0/2/3；stdout 数据 JSON、stderr 错误 JSON。

加固（pass-1 三模型审计后）：
- 围栏缩进按 CommonMark 列展开判定（Tab 展开到下一 4 列；1 个前导 Tab = 4 列 = 非法，
  不再被误认为闭合围栏）。
- `html_error_page` 关键词分支要求 `< >` 标签上下文（纯文本含 "error" 不再误判；
  doctype/html 头分支不变）。
- 快照排除清单可用环境变量 `RV_SNAPSHOT_EXCLUDED`（空白/逗号/分号/冒号分隔）覆盖，
  按所在环境文档校准无需改代码。
- heredoc 标签文法补齐连字符（`MY-LABEL` 等合法 shell 标签）。
- 自检 87→94：step3 完整字节精确、Tab 缩进围栏、CRLF+尺寸钉扎优先级、纯文本/真 HTML
  404 正反例、env 覆盖双向。

修复 v1 缺陷：
- 版本漂移（frontmatter 1.0.0 vs 发布 1.0.6）→ 统一 2.0.0。
- README 声称具备 sha256sum 批量能力但无可执行物 → `manifest` 落实。
- 内联 triage 片段只处理单个 `\n` → 完整分类器。
- 散文规则"按行范围切步骤"无执行物且朴素切分会被内嵌围栏截断 → `extract-steps`。

## v1.0.6 — 2026-04-22

（历史版本：散文版。见 ClawHub 版本历史。）
