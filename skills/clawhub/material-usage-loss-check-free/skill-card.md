## Description:

A local deterministic checker for material usage and loss tables that recalculates row arithmetic, verifies totals, detects duplicate or incomplete rows, and cites source rows for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, project, and materials staff use this skill during monthly closing, reconciliation, or inventory review to check material usage and loss tables. It helps recalculate quota usage, loss quantities, totals, duplicate rows, blanks, placeholders, and negative quantities or prices from user-provided table text or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes optional paid-upgrade instructions that ask the user to invoke an external payment installation flow beyond the local free checker.

Mitigation: Use only the bundled local checker unless you independently trust the publisher, payment package, and SkillPay purchase workflow; do not paste the prepared purchase prompt or run the external install command by default.

Risk: The free checker intentionally omits several checks that are described as available only in a separate paid product.

Mitigation: Treat results as limited to the listed free checks and do not rely on the skill for omitted checks such as reference loss-rate warnings, amount recalculation, unit consistency, or negative-loss detection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/material-usage-loss-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON reports with cited source rows and command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided material table input; reports insufficient input instead of drawing conclusions when required fields are missing.]

## Skill Version(s):

1.0.4 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
