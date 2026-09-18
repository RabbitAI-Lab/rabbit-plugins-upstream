## Description:

预付卡消费核销表逐项核对，覆盖逐行复算、合计勾稽、重复与空缺检测，并为结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashiering teams use this skill during month-end close, reconciliation, or inventory checks to verify prepaid-card consumption write-off tables. It checks arithmetic, totals, duplicate card-period rows, blanks, placeholders, and selected negative amount cases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill's upgrade path can lead an agent toward a paid purchase flow and mutable remote-code installation.

Mitigation: Keep upgrade and purchase actions outside autonomous execution; require human review of the external package, seller, terms, and payment step before any install or purchase.

Risk: The default human-readable output includes upgrade advertising that an automation agent could treat as an action prompt.

Mitigation: Use the JSON output mode for automation and ignore upgrade text unless a human explicitly approves that separate workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/prepaid-card-consumption-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON]

**Output Format:** [Human-readable text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs local reconciliation findings with cited source rows; automation should prefer --json.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
