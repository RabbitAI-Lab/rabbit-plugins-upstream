## Description:

AgentEarth helps agents discover and execute AgentEarth API-backed external tools when live or external-tool results are useful and the host permits external API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shanminghui](https://clawhub.ai/user/shanminghui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route tasks requiring live or external data through AgentEarth's Recommend and Execute APIs while preserving host policy and credential safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task queries and Execute parameters may include sensitive information that is sent to an external tool marketplace.

Mitigation: Confirm trust in AgentEarth before use and avoid sending sensitive tokens, private code, account data, or other confidential values unless that is intended for the selected tool.

Risk: API keys could be exposed through logs or sent to an unsafe endpoint if URL validation is skipped.

Mitigation: Configure AGENT_EARTH_API_KEY through the host secret mechanism, redact credentials from user-visible output, and send the key only to validated HTTPS AgentEarth endpoints.

Risk: Incorrect tool selection or malformed parameters could cause failed or misleading external tool execution.

Mitigation: Call Recommend before Execute, select tools by task relevance and schema clarity, validate required fields and types, remove unknown keys when required, and ask the user for missing real values.

## Reference(s):

- [AgentEarth API Specification](references/api-specification.md)
- [AgentEarth Homepage](https://agentearth.ai)
- [ClawHub AgentEarth Skill Page](https://clawhub.ai/shanminghui/skills/agentearth)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP examples, shell commands, PowerShell commands, and JSON request and response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires AGENT_EARTH_API_KEY and returns selected external tool results through the AgentEarth API flow.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
