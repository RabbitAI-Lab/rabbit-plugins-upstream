## Description:

销售提成与业绩核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff use this skill during monthly close, reconciliation, or sales commission review to check Chinese sales commission tables for row-level arithmetic errors, total-row mismatches, duplicate period/person rows, blank placeholders, and negative amounts. It reports missing inputs instead of giving a clean result when required table fields are absent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a clean result as a full audit of commission policy or tier eligibility.

Mitigation: Treat the output as a limited local arithmetic check and review the listed checks_not_run before relying on the result.

Risk: The checker is scoped to Chinese sales commission tables with expected columns and may not support other commission formats.

Mitigation: Provide a table with the required sales commission fields and review missing-input guidance when the skill declines to issue a conclusion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/sales-commission-tier-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable text or JSON findings with cited source lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, missing-input guidance, findings, summary counts, and audit-scope disclaimers.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
