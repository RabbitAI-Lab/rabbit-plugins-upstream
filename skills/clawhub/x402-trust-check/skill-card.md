## Description:

Check the trust rating of any x402 service before paying it, and of any skill before installing it. Free JSON, daily, sybil-resistant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to check advisory trust ratings before paying x402 endpoints or installing skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trust ratings are advisory and do not guarantee service quality or safety.

Mitigation: Use the rating as one input, report the tier and relevant flags, and apply the skill's conservative payment or install policy.

Risk: Optional history and archive lookups can spend through the configured x402 wallet.

Mitigation: Use paid endpoints only when the user intentionally asks for history or an audit trail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [ClawHub publisher profile](https://clawhub.ai/user/aladaf)
- [Agent Economy Report service ratings](https://agenteconomy.report/s/)
- [Agent Economy Report method and corrections policy](https://agenteconomy.report/s/policy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with inline bash commands and concise risk guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public rating JSON by default; optional paid endpoints are used only when intentionally requested.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
