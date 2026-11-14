## Description:

Provides one-off and live AI analysis, research, scored news, market events, sector catalysts, and simulated autopilot monitoring for US stocks and crypto.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT

## Use Case:

External users use the skill to request stock and crypto research, live monitoring, scored news, and sector catalysts through SimianX. Developers can also consult its API guidance when building integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires network access and may use server-side monitoring features; the scanner's benign verdict has medium confidence and covers 92.3% of components.

Mitigation: Review network access and monitoring behavior before use, keeping in mind that the scan evidence is incomplete.

Risk: Stock and crypto analysis can inform consequential financial decisions.

Mitigation: Treat results as analysis rather than investment advice; keep SimianX positions simulated and require user confirmation before any external order.

## Reference(s):

- [SimianX Agent Documentation](https://www.simianx.ai/agents)
- [SimianX OpenAPI Specification](https://service.simianx.ai/v1/openapi.json)
- [SimianX AI ClawHub Listing](https://clawhub.ai/simianxai/skills/simianx)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, API Calls, PDF reports]

**Output Format:** [Markdown summaries and structured API responses; PDF reports for deep research.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis varies by symbol, asset class, timeframe, and workflow; SimianX positions are simulated.]

## Skill Version(s):

1.0.12 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
