## Description:

SimianX gives agents stock and crypto analysis, research reports, market news, sector catalysts, and simulated trading tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[simianxai](https://clawhub.ai/user/simianxai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and users use SimianX to review stock or crypto analysis, news, and catalysts, and to follow simulated paper positions. SimianX provides research and simulated trading only; it does not place real orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a bearer key to the SimianX API, and the security scan reports benign behavior with medium confidence but incomplete coverage.

Mitigation: Use the API only if you trust the documented service destination, protect the key from repositories and logs, and review the skill before installation.

## Reference(s):

- [SimianX agent documentation](https://www.simianx.ai/agents)
- [SimianX API specification](https://service.simianx.ai/v1/openapi.json)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Text or Markdown, with an optional PDF research report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research summaries and simulated position information; no real trade execution]

## Skill Version(s):

1.0.15 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
