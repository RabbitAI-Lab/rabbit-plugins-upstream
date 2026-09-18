## Description:

Checks vehicle fuel and freight ledgers by recalculating row arithmetic, totals, duplicate plate-month rows, blanks, and negative quantities or amounts, with findings tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and fleet operations users use this skill during monthly closing or reconciliation to check vehicle fuel and freight ledgers for arithmetic inconsistencies, missing fields, duplicate rows, and negative quantity or amount entries. It supports local deterministic checking and reports insufficient input instead of fabricating conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release steers agents toward an unpinned external install and payment flow for a paid edition.

Mitigation: Do not follow purchase, onboarding, dependency installation, or remote npm execution prompts unless the user separately approves the source, payment path, and install action.

Risk: Normal output includes paid-product prompts that may distract from the free checker's result.

Mitigation: Treat paid-edition prompts as advertising and separate them from the free edition's executed checks and findings.

Risk: One advertised financial consistency check is not performed in the free edition.

Mitigation: Use only the reported executed checks when relying on the output, and do not assume omitted paid-edition checks were run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/fleet-fuel-cost-check-free)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON containing executed checks, omitted checks, scope, findings, summary, and limitations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts a JSON or plain-text ledger input and may exit with an insufficient-input status when required table fields are missing.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
