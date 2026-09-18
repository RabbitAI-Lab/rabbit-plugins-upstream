## Description:

A local checker for driver freight settlement sheets that recalculates freight and payable amounts, reconciles detail rows to totals, detects duplicate or incomplete waybills, and cites each finding with source line and waybill identifiers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External logistics, fleet, finance, dispatch, and settlement staff use this skill to check carrier and driver freight settlement sheets before payment. It supports local reconciliation of copied tabular settlement data and reports calculable discrepancies without claiming to validate external contracts or source business records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release embeds paid-upgrade prompts and unpinned remote install or payment instructions that go beyond the local checker framing.

Mitigation: Use the free local checker without following purchase prompts unless the SkillPay or Alipay flow is independently trusted; require explicit human review before running unpinned install commands or initiating payment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/driver-freight-settlement-check-free)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Human-readable findings or JSON reconciliation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line and waybill identifiers; insufficient input returns missing-field guidance rather than a conclusion.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
