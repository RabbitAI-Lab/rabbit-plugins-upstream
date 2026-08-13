## Description:

Stock Factor gives agents a curated A-share equity factor library with 1,101 factors across 18 families, bundled factor-analysis outputs, QuantAll task JSON files, and a local HTML report generator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and quantitative researchers use this skill to inspect A-share factor definitions, review IC/IR screening metrics, run bundled QuantAll factor-analysis tasks, and generate local factor research reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running bundled QuantAll tasks can overwrite or update spreadsheet and report outputs in the local output directory.

Mitigation: Review each task JSON save path and run updates on a copy when preserving existing analysis outputs matters.

Risk: Factor-analysis results depend on the configured local QuantAll database and its data coverage.

Mitigation: Confirm the local database path, data freshness, and field availability before relying on generated IC/IR metrics.

Risk: Bundled factors and screening metrics are research inputs, not validated trading recommendations.

Mitigation: Perform independent validation, redundancy checks, and strategy backtests before using factors in investment workflows.

## Reference(s):

- [ClawHub stock-factor skill page](https://clawhub.ai/mifochen/skills/stock-factor)
- [Skill documentation](artifact/SKILL.md)
- [Factor collection and transcription notes](artifact/scripts/因子收集与转写经验.md)
- [Qlib Alpha158 factor reference](artifact/scripts/因子初始参考文件/Alpha158_因子参考.md)
- [Qlib Alpha360 factor reference](artifact/scripts/因子初始参考文件/Alpha360_因子参考.md)
- [WorldQuant Alpha101 formulas](artifact/scripts/因子初始参考文件/Alpha101.txt)
- [TA-Lib indicator reference](artifact/scripts/因子初始参考文件/TA-Lib指标参考.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with Python and JSON task snippets, local spreadsheet outputs, and generated HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled QuantAll task files and output workbooks; report generation writes a local self-contained HTML file.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
