## Description:

Stock Factor gives agents a QuantAll-ready A-share stock factor library with Excel summaries, task JSON files for recalculating IC/IR metrics, and an HTML report generator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect A-share stock factor definitions, compare IC/IR screening metrics, and run QuantAll task files to refresh factor analysis outputs. It is suited to quantitative research workflows that already have local market data and the QuantAll engine configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local market data through QuantAll and can write local analysis outputs.

Mitigation: Point QuantAll only at DuckDB data you are comfortable analyzing and review generated output paths before running task files.

Risk: The skill depends on a separately installed QuantAll package and MCP connector.

Mitigation: Review the QuantAll package and connector configuration separately before using this skill for local research workflows.

Risk: Broad process-kill commands can terminate an unintended QuantAll process.

Mitigation: Use process termination only after identifying the stuck QuantAll process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mifochen/skills/stock-factor)
- [Publisher profile](https://clawhub.ai/user/mifochen)
- [Skill instructions](artifact/SKILL.md)
- [TA-Lib indicator reference](artifact/scripts/\u56e0\u5b50\u521d\u59cb\u53c2\u8003\u6587\u4ef6/TA-Lib\u6307\u6807\u53c2\u8003.md)
- [Alpha101 formulas](artifact/scripts/\u56e0\u5b50\u521d\u59cb\u53c2\u8003\u6587\u4ef6/Alpha101.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, JSON task files, Excel factor tables, and generated HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local analysis artifacts and requires a separately installed QuantAll engine for recalculation.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
