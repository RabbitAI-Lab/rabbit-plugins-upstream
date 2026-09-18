## Description:

A Chinese-language manufacturing monthly self-check skill that runs local table checks for production yield and scrap, material usage and quota loss, and inventory weighted-average cost.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and operations staff use this skill during monthly closing, reconciliation, and inventory review to check manufacturing tables for arithmetic and cross-table consistency. It reports source-grounded findings and withholds conclusions when required input is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reviewed free skill includes an optional path that points the agent toward an external paid SkillPay purchase and installation workflow with code outside this review.

Mitigation: Use the free local checks unless the paid workflow is reviewed separately; require explicit user approval before any package install, payment, or newly loaded skill instruction.

Risk: The skill performs accounting-oriented arithmetic and reconciliation checks but does not replace bookkeeping, attestation, filing, ERP or MES import, or professional judgment.

Mitigation: Treat findings as review aids, keep source records available for human verification, and do not use missing-input runs as evidence that no issue exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/manufacturing-monthly-selfcheck-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, shell commands, guidance]

**Output Format:** [Chinese human-readable text or JSON findings with check names, source lines, severity, summaries, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; input larger than 4 MB is rejected by the bundled runner.]

## Skill Version(s):

1.0.5 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
