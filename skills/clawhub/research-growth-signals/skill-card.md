## Description:

Research traceable public social and SEO signals through SignalDig's single MCP connection and two business tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and growth teams use this skill to route natural-language requests for public social discussion, SEO demand, SERP, trend, competitor, backlink, ranking, and traffic evidence through SignalDig's bounded research tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries, domains, public profile URLs, and SEO or social targets are submitted to SignalDig through its MCP service.

Mitigation: Use the skill only for public growth research inputs that the user is comfortable sharing with SignalDig.

Risk: Compatible Social or SEO research requests may be routed to SignalDig automatically once the MCP connection is installed.

Mitigation: Review tool calls before execution when available, and disable implicit invocation or disconnect the MCP service where automatic routing is not desired.

Risk: Partial or limited source coverage could be mistaken for exhaustive market evidence.

Mitigation: Preserve SignalDig coverage and limitations in user-facing answers and avoid describing partial evidence as comprehensive.

## Reference(s):

- [SignalDig homepage](https://signaldig.com/)
- [Connect SignalDig](https://signaldig.com/agent-setup)
- [SignalDig Unified Research MCP Contract](artifact/references/mcp-contract.md)
- [SignalDig Connection Setup](artifact/references/setup-guide.md)
- [ClawHub skill page](https://clawhub.ai/jerrykik/skills/research-growth-signals)
- [Publisher profile](https://clawhub.ai/user/jerrykik)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, API calls]

**Output Format:** [Markdown guidance with structured SignalDig MCP tool calls and cited public evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses terminal SignalDig analysis responses, preserves coverage and limitations, and reports analysis_id for traceability.]

## Skill Version(s):

2.1.0 (source: server evidence, release metadata, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
