## Description:

Helps agents analyze stocks and crypto with live market research, scored news, sector catalysts, and scheduled paper-position monitoring through SimianX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request stock or crypto analyses, monitor market news and sector catalysts, and follow scheduled analyses or paper positions. Its analyses are informational, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable remote skill instructions could change agent behavior unexpectedly.

Mitigation: Review and approve updated instructions before the agent follows them; do not enable automatic remote updates.

Risk: An agent could receive overly broad, durable account access through an API key.

Mitigation: Prefer browser approval of requested scopes, or limit ordinary analysis keys to data:read and analysis:run with an appropriate points budget.

Risk: Autopilots, paper-position changes, and metered analysis may have financial or account consequences.

Mitigation: Require user confirmation before autopilot or paper-position changes and high-cost calls; review analysis independently rather than treating it as investment advice.

## Reference(s):

- [SimianX agent documentation](https://www.simianx.ai/agents)
- [SimianX API specification](https://service.simianx.ai/v1/openapi.json)
- [SimianX AI skill release](https://clawhub.ai/simianxai/skills/simianx)
- [Authentication reference](references/auth.md)
- [Autopilots reference](references/autopilots.md)
- [Live analysis reference](references/live.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with market-analysis summaries and optional API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize news, research verdicts, catalyst calendars, and paper-position events.]

## Skill Version(s):

1.0.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
