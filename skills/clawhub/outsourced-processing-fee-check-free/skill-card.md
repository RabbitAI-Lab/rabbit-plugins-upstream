## Description:

委外加工结算核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and manufacturing operations staff use this skill during monthly closing, reconciliation, or inventory checks to recalculate outsourced-processing settlement rows, totals, duplicates, blanks, and negative quantities or amounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence notes inconsistent telemetry and --no-stats wording.

Mitigation: Treat the checker as a local arithmetic and table-validation aid, and confirm telemetry behavior and user-facing wording before operational reliance.

Risk: The skill checks settlement-table arithmetic and table consistency, not contract terms or payment obligations.

Mitigation: Use findings as review prompts and confirm billing decisions against contracts, signed settlement documents, and internal approval processes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/outsourced-processing-fee-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON findings with cited table lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local table-check results include executed checks, omitted checks, findings, summary counts, and insufficient-input guidance.]

## Skill Version(s):

1.0.52 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
