## Description:

AgentEarth helps agents discover and execute AgentEarth API-backed tools for tasks that need live or external results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanminghui](https://clawhub.ai/user/shanminghui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route tasks that need live or external results through AgentEarth while following schema, endpoint, and credential-safety checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task queries and selected tool parameters are sent to agentearth.ai.

Mitigation: Use the skill only when live or external-tool results are intended, and avoid sending unnecessary sensitive information.

Risk: The AgentEarth API key could be exposed if it is included in messages, logs, or unvalidated requests.

Mitigation: Keep AGENT_EARTH_API_KEY in host-managed secret storage, redact it from output, and send it only to validated AgentEarth HTTPS endpoints.

Risk: Executing tools with invented or schema-mismatched parameters can produce failed or misleading external-tool results.

Mitigation: Call Recommend before Execute, build params only from the selected tool input schema, validate required fields and types, and ask the user for missing real values.

## Reference(s):

- [AgentEarth API Specification](references/api-specification.md)
- [AgentEarth Homepage](https://agentearth.ai)
- [ClawHub Skill Page](https://clawhub.ai/shanminghui/skills/ag-earth)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTTP, JSON, bash, and PowerShell examples; runtime results are summarized as text or JSON-derived text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_EARTH_API_KEY and sends task queries and selected tool parameters to AgentEarth endpoints.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
