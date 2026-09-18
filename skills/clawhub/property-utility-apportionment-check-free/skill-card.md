## Description:

物业公共能耗分摊核对（免费版） helps agents check property public-utility apportionment tables by recalculating allocation amounts, reconciling totals, and flagging duplicate rows, blank or placeholder fields, and negative values with source-backed findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Property finance and cashier teams use this skill during monthly closing, reconciliation, or inventory checks to run a local deterministic review of property public-utility apportionment tables before billing or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill steers users and agents toward an external paid install and purchase flow using mutable remote instructions.

Mitigation: Use only the free local checker unless a paid upgrade is intended; independently verify the SkillPay flow, package name, and version, and require the user to confirm any wallet authorization or payment.

Risk: The free checker omits listed checks such as ratio-sum validation, over-allocation checks, public-price comparison, vacancy apportionment checks, and duplicate-period checks.

Mitigation: Treat results as support for the six included table checks only, and perform separate review for the omitted checks before relying on the table for billing or publication.

Risk: The checker does not judge whether source totals, apportionment methods, vacancy treatment, transferred-utility pricing, taxes, subsidies, or late fees are legally or factually correct.

Mitigation: Review contracts, public notices, source utility bills, accounting records, and applicable local rules separately from this table arithmetic check.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/property-utility-apportionment-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Artifact skill definition](artifact/SKILL.md)
- [Sample input template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON from the local Node runner; agent-facing guidance may be Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on supplied table text or JSON; insufficient input returns missing requirements instead of a clean finding.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
