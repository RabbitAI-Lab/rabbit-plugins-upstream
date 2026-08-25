## Description:

Check the trust rating of any x402 service before paying it. Free JSON, daily, sybil-resistant; refuse dead or unknown recipients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladaf](https://clawhub.ai/user/aladaf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill before paying x402 endpoints to check service trust ratings, liveness, adoption, and payment risk. It also helps evaluate wallet-only recipients and report concise, citation-based trust summaries to users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow consults an external rating service before x402 payments.

Mitigation: Use it where this external lookup is acceptable, and review queried hosts before sending requests.

Risk: Optional history and archive checks may trigger paid x402 requests.

Mitigation: Use the free JSON checks for routine decisions, and allow paid endpoints only when the user explicitly requests deeper history or an audit trail and accepts the stated cost.

Risk: Trust ratings are decision support, not a guarantee of service quality.

Mitigation: Treat tier, uptime, flags, organic paying agents, and settled volume as risk signals, and ask the user or refuse payment for unknown or high-risk recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aladaf/skills/x402-trust-check)
- [Agent Economy Report ratings](https://agenteconomy.report/s/)
- [Agent Economy Report method and corrections policy](https://agenteconomy.report/s/policy)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Text]

**Output Format:** [Markdown with inline bash commands and concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited rating URLs and optional paid endpoint choices when the user explicitly requests deeper history or an audit trail.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
