## Description:

Locally checks Chinese lesson-hour reconciliation tables for row arithmetic, totals, duplicate learners, and blank placeholders, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations staff at education, fitness, beauty, or similar lesson-hour businesses use this skill during monthly settlement, reconciliation, or inventory checks to verify lesson-hour tables before follow-up accounting work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process customer or accounting data supplied in input files.

Mitigation: Use it only with intended lesson-hour reconciliation tables and handle supplied files according to the user's local data policy.

Risk: The documentation mentions anonymous usage statistics even though the inspected code does not implement network transmission.

Mitigation: Clean up the documentation mismatch and verify network behavior again before publishing a future update.

Risk: The free version intentionally omits checks such as over-consumption, zero-price-with-usage, amount caps, and inconsistent course pricing.

Mitigation: Treat the output as a scoped arithmetic, totals, duplicate, and blank-field check; perform separate review for omitted checks before final financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/lesson-hour-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Human-readable console text or JSON result from a Node.js command-line runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing requirements instead of a pass or fail conclusion.]

## Skill Version(s):

1.0.26 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
