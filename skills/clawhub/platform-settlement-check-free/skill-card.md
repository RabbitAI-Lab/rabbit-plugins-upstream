## Description:

平台结算单逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill to check e-commerce platform settlement sheets during month-end reconciliation. It reviews line-item arithmetic, totals, duplicate order IDs, and blank or placeholder fields, and it withholds conclusions when required source material is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telemetry wording is inconsistent, which may make users uncertain about whether settlement-sheet data leaves the local machine.

Mitigation: Review the release text before use and run the skill only in an environment appropriate for sensitive settlement data.

Risk: The skill expects Chinese-language settlement-sheet headers and returns Chinese-language output.

Mitigation: Run the bundled sample first and verify that real inputs use recognizable settlement-sheet columns before relying on the results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/platform-settlement-check-free)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console output or JSON result reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and advice instead of a conclusion.]

## Skill Version(s):

1.0.27 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
