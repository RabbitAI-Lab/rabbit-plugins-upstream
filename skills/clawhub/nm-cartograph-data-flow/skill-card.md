## Description:

Generates a Mermaid sequence diagram showing how data moves between components.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to trace request flows, understand data transformation pipelines, document API call chains, and explain what happens when a scoped code path is called.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read private or sensitive code while building the data-flow diagram.

Mitigation: Scope requests to the files, components, or flows that are appropriate to inspect, especially in private repositories.

Risk: Rendered Mermaid diagram content may be shared with the configured Mermaid Chart MCP service.

Mitigation: Avoid rendering diagrams that include secrets, proprietary details, or sensitive system architecture unless that service is approved for the content.

Risk: Generated diagrams may omit or simplify important behavior in complex code paths.

Mitigation: Review the Mermaid output against the source code before using it as authoritative documentation.

## Reference(s):

- [Cartograph plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/cartograph)

## Skill Output:

**Output Type(s):** [analysis, markdown, code, guidance]

**Output Format:** [Markdown with Mermaid sequence diagram code and a brief prose summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated diagrams should stay within the skill's requested scope; rendering uses the configured Mermaid Chart MCP service when available.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
