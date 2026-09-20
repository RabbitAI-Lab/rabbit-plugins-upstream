## Description:

Checks Chinese training-hour consumption and prepaid-tuition reconciliation tables by recomputing row arithmetic, totals, duplicates, blanks, and negative values, with findings tied to source rows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashier staff at training providers use this skill during monthly closing, reconciliation, or inventory checks to audit training-hour consumption and prepaid-tuition tables before relying on them for revenue rollover and remaining-hour calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free version withholds several reconciliation checks, so a clean result is not a full audit of the table.

Mitigation: Review the listed withheld checks and perform them separately or use a complete reconciliation process when those controls matter.

Risk: The skill checks table arithmetic and consistency but does not decide accounting, contract, tax, refund, or legal treatment.

Mitigation: Use it as a deterministic table-audit aid and have qualified finance, accounting, or legal reviewers decide policy questions.

Risk: Users provide reconciliation tables that may contain student, payment, or business-sensitive data.

Mitigation: Run the checker locally, provide only the minimum exported table needed for the check, and follow the organization's data-handling controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/training-hour-consumption-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console output or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes executed checks, withheld checks, row-level findings, missing-input messages, and local-execution flags.]

## Skill Version(s):

1.0.42 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
