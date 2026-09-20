## Description:

采购返利核对表逐项核对（应得返利与差额复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, finance, and operations users use this skill to check supplier purchase rebate tables for rebate arithmetic, received-vs-owed differences, totals, duplicate suppliers, and blank fields. It is intended for Chinese-language rebate tables and reports missing input instead of producing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill only performs the local arithmetic and table checks listed for the free version, and does not run withheld checks such as rate-tier matching, tax treatment, contract interpretation, or financial advice.

Mitigation: Review the output's checks_not_run section and validate rebate tiers, tax basis, and contract terms outside the skill before acting on results.

Risk: Chinese-language purchase rebate tables may be misinterpreted when required headers or source rows are missing or exported incorrectly.

Mitigation: Provide the full table with recognizable headers and source rows; treat insufficient_input results as no conclusion.

Risk: The runner documents an optional anonymous usage statistic after local execution, even though security evidence found no hidden network use or credential access.

Mitigation: Review the runner behavior before deployment and use the documented no-stats path or local policy controls if anonymous telemetry is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/purchase-rebate-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON diagnostic report with line-referenced findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and no conclusion.]

## Skill Version(s):

1.0.30 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
