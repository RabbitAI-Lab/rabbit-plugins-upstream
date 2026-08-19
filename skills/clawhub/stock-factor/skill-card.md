## Description:

Stock Factor gives agents a curated A-share stock-factor catalog with QuantAll-ready task JSON files, IC/IR result spreadsheets, and a report generator for factor research workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, quantitative researchers, and agents use this skill to inspect A-share factor definitions, run QuantAll batch factor analyses from local JSON task files, and summarize factor performance from generated spreadsheets and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external QuantAll package and a local stock database.

Mitigation: Install only when using QuantAll with a local stock database, and review the external quantall package before installation.

Risk: Troubleshooting QuantAll by stopping Python processes can interrupt unrelated Python work.

Mitigation: Stop only QuantAll-related Python processes when resolving a busy or stuck QuantAll service.

Risk: Factor IC/IR outputs can be overread as trading recommendations.

Mitigation: Treat outputs as research signals and validate factors through independent review, redundancy checks, and backtesting before use in investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mifochen/skills/stock-factor)
- [Skill instructions](artifact/SKILL.md)
- [Factor collection and transcription notes](artifact/scripts/因子收集与转写经验.md)
- [QuantAll code environment reference](artifact/scripts/因子初始参考文件/how_code.txt)
- [TA-Lib indicator reference](artifact/scripts/因子初始参考文件/TA-Lib指标参考.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON task references, Python code snippets, spreadsheet references, and self-contained HTML report output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local QuantAll MCP service setup, scripts/task JSON files, scripts/output XLSX files, and scripts/因子分析报告.html.]

## Skill Version(s):

1.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
