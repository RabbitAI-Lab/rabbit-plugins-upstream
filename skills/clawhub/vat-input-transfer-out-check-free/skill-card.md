## Description:

Checks Chinese input VAT transfer-out calculation tables for row arithmetic, totals, duplicate rows, blanks, and negative values, with each finding tied to source table text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill during monthly close, reconciliation, or inventory review to check input VAT transfer-out tables before relying on the table totals. It reports only the checks included in the free release and does not provide tax advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence notes inconsistent wording about anonymous usage statistics.

Mitigation: Users should install only if comfortable with the stated telemetry behavior and should seek publisher clarification before relying on the no-network claim.

Risk: The skill checks table arithmetic and related consistency but should not be treated as tax advice.

Mitigation: Use the output as a table-checking aid and have qualified tax or finance staff review tax treatment decisions.

Risk: The free release does not include every check listed for the full edition.

Mitigation: Review the listed withheld checks before relying on a clean result for broader VAT review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-input-transfer-out-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON report with cited findings, missing-input guidance, executed checks, and withheld checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The free release withholds some advanced checks and avoids a conclusion when input material is insufficient.]

## Skill Version(s):

1.0.50 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
