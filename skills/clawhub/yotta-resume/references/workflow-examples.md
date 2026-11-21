# 端到端工作流示例

## 1. 安装后自检

```bash
python scripts/yotta_resume.py doctor --format json
```

核心契约或随包文件失败时停止并修复；PyMuPDF 或浏览器缺失只影响对应格式。

## 2. 分析

```bash
python scripts/yotta_resume.py audit --resume resume.md --jd jd.txt --format json
```

读取 `source_manifest`、`parse_warnings`、`industry_detection`、`issues`、
`questions`、`unknowns` 和 `jd_match`。先确认行业、输入质量和事实边界，再改简历。

## 3. 追问与确认

按问题的优先级向用户确认：

1. 个人责任：主导、共同负责、协助还是参与。
2. 规模：系统数、告警量、时间窗、覆盖团队。
3. 方法：工具、流程、验证和回滚。
4. 结果：可证明的基线、变化和证据。

未确认的事实不写入简历。

## 4. 修改 Markdown

```markdown
### 示例科技 | 安全运营工程师 | 2023.01 - 2026.01
- 负责 6 个业务系统的 SIEM 规则维护，按周复盘 100 条脱敏样本，未公开真实告警数据。
```

## 5. 事务化导出

```bash
python scripts/yotta_resume.py export --input revised.md --docx revised.docx --html revised.html --pdf revised.pdf
```

全部格式成功后才会写入目标路径。任一格式失败时保留原有文件，不留下本次半成品。

## 6. 交付检查

- 核对 `doctor`、目标和实际文件名。
- DOCX / PDF 必须可打开，PDF 应包含文字层。
- 报告联系方式已打码，成品按用户确认保留。
- 不承诺 ATS、面试或 Offer 结果。
