## Description:

Locally checks payment fee worksheets by recalculating row-level fees, settlement amounts, totals, duplicate channels, and blank fields, with findings tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and operations users use this skill to review payment-channel fee worksheets during reconciliation. It highlights arithmetic mismatches, total-row inconsistencies, duplicate channels, and missing required fields without treating insufficient material as a clean result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free checker documentation and default output steer agents toward an external paid install and purchase flow that is not necessary for the free local check.

Mitigation: Use the free local checker only for worksheet review; do not run @latest installers, install paid variants, or authorize purchase steps unless the user independently verifies the SkillPay flow and explicitly approves each step.

Risk: The free version omits several checks and withholds conclusions when required worksheet material is missing.

Mitigation: Review the executed and omitted check lists, provide complete worksheet headers and rows, and do not interpret insufficient-input responses as a clean reconciliation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payment-fee-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON result containing worksheet findings, source line numbers, executed checks, omitted checks, and missing-input guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields instead of a no-issues conclusion.]

## Skill Version(s):

1.0.12 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
