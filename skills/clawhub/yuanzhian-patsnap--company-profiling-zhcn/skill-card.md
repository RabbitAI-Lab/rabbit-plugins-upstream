## Description:

Provides Chinese-language pharmaceutical company profiling using PatSnap life-science data to analyze company overview, financing history, pipelines, deals, collaborations, and selected patent positioning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life-science analysts, strategy teams, and business-development users use this skill to profile pharmaceutical companies and produce evidence-grounded Chinese reports on corporate background, R&D pipelines, financing, deals, collaborations, and relevant patent activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a PatSnap API key and adds a remote MCP service to the agent.

Mitigation: Users should configure only the required PatSnap MCP service, protect API keys, verify MCP connectivity before use, and limit use to life-science company analysis.

Risk: Company profiles and investment or partnership recommendations may be incomplete or stale if available MCP data is insufficient.

Mitigation: The skill instructs the agent to fetch detailed records before analysis, avoid unsupported claims, use web search only after MCP retrieval is insufficient or recency is required, and include source and date information in reports.

## Reference(s):

- [PatSnap Open Platform](https://open.patsnap.com)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/company-profiling-zhcn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and setup guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese-language report structure with required summary, numbered sections, conclusion, source notes, date fields, and disclaimer.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
