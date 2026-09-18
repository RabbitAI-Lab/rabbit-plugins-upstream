## Description:

Performs a free deterministic local check of labor cost allocation tables, with each finding citing source material and no payment, registration, API key, or network access required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashiering, and operations staff use this skill during month-end closing, reconciliation, and inventory checks to validate labor cost allocation tables. It recomputes row amounts, reconciles totals, detects duplicates and blanks, and reports missing input instead of inventing conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation points users toward an agent-driven paid install flow that runs unpinned remote code and loads external instructions.

Mitigation: Use the free local checker only after deciding to run its bundled Node script; independently verify the SkillPay instructions, package publisher, package version, and payment details before using the paid-upgrade flow.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/labor-cost-allocation-check-free)
- [Paid-upgrade purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Shell commands]

**Output Format:** [Human-readable text or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js; insufficient input returns missing fields instead of a finding.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
