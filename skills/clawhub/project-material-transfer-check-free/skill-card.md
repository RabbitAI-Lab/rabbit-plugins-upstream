## Description:

A Chinese-language local checker for engineering material transfer and issue tables that recalculates line arithmetic, total rows, duplicate rows, blanks, and negative quantity or amount values with source-row evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and project cost staff use this skill during monthly closing, reconciliation, and inventory review to check copied or exported material-transfer tables before continuing downstream accounting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The help text mentions anonymous statistics even though the inspected code does not implement network reporting.

Mitigation: Review and clean the help text before release so privacy expectations match the local-only implementation.

Risk: The free checker covers selected table arithmetic and consistency checks, but it does not verify physical inventory, business approval, unit conversion, tax, freight, or withheld paid-tier checks.

Mitigation: Use results as a reconciliation aid and keep project controls, contract review, and physical inventory checks in the operating process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/project-material-transfer-check-free)
- [Artifact skill definition](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, cited rows, omitted checks, summary counts, and scope notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on provided table text; reports insufficient input instead of fabricating a conclusion.]

## Skill Version(s):

1.0.50 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
