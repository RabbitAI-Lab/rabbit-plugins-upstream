## Description:

Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check x402 service or skill reputation before paying for an endpoint or installing a skill. It helps them interpret trust tiers, uptime, adoption signals, flags, and optional audit records from Agent Economy Report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queried hosts or skill slugs are disclosed to a third-party reputation service.

Mitigation: Use the free rating endpoints only when that disclosure is acceptable, and avoid submitting sensitive internal hostnames.

Risk: Ratings are advisory and may not prove service quality or financial safety.

Mitigation: Use rating tier, uptime, adoption, and flags as decision support, and require explicit user approval for higher-risk or higher-value payments.

Risk: Optional history, archive, and audit endpoints require x402 payment.

Mitigation: Ask the user before making any optional paid request and state the listed price before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [Agent Economy Report service ratings](https://agenteconomy.report/s/)
- [Agent Economy Report method and corrections policy](https://agenteconomy.report/s/policy)
- [Audited skill index](https://agenteconomy.report/k/audited)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, Text]

**Output Format:** [Markdown or concise text with optional inline shell commands and JSON field interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for free checks and agentcash for optional paid x402 requests.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
