## Description:

Checks promotion subsidy reconciliation tables for payable subsidy arithmetic, settlement differences, total-row consistency, duplicate activity/SKU rows, and missing placeholders, with each finding tied to source line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External business-operations users in retail or ecommerce use this skill after promotions to check subsidy reconciliation tables for arithmetic inconsistencies, duplicate rows, missing fields, and settlement differences. The skill is a local Node-based checker and does not validate promotion-policy terms or withheld premium checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an AI-directed paid upgrade flow that may install unreviewed software and initiate a purchase workflow.

Mitigation: Use only the bundled free local checker unless you separately verify the package, understand the SkillPay purchase flow, and explicitly choose to install additional content.

Risk: The free checker's results are limited and do not validate activity caps despite the cap rule being mentioned.

Mitigation: Treat outputs as a subset of reconciliation checks and separately validate cap compliance and other withheld checks before relying on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/promo-subsidy-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown or plain text guidance with optional JSON command output from the local checker]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing-material guidance instead of a conclusion.]

## Skill Version(s):

1.0.10 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
