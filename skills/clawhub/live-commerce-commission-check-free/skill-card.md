## Description:

直播佣金与坑位费结算核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and settlement operations users use this skill during monthly close, reconciliation, or pre-payment review to check live-commerce commission and slot-fee settlement tables. It recomputes row-level arithmetic, column totals, duplicate rows, blank placeholders, and negative amounts, and cites the source rows for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a clean result as a full settlement, contract, platform, bank, or duplicate-settlement audit.

Mitigation: Present results as checks of the listed arithmetic and table consistency only, and route contract terms, platform exports, bank records, and duplicate-settlement questions to the appropriate source records or reviewers.

Risk: The free release withholds some full-version checks, so users may miss issues outside the executed check list.

Mitigation: Show the executed and withheld check lists with each result and avoid claiming that omitted checks were performed.

Risk: Insufficient or malformed table input can lead to misleading confidence if the skill guesses missing values.

Mitigation: Require the expected table headers and return missing-input guidance instead of producing a pass or fail conclusion when required fields are absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/live-commerce-commission-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill instructions](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON findings with cited source rows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld full-version checks, missing-input guidance, local execution status, and finding summaries.]

## Skill Version(s):

1.0.46 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
