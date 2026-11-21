## Description:

Give your AI agent Apple Health data you pick, end-to-end encrypted between your iPhone and the local Syncky agent; send writes you authorize through your agent, for the types allowed on your iPhone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[syncky](https://clawhub.ai/user/syncky)

### License/Terms of Use:

MIT-0

## Use Case:

iPhone owners use this agent skill to set up a local Syncky agent that receives the Apple Health data they select and provides local MCP access. The skill describes how to make owner-approved requests and writes while keeping health data private and avoiding medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apple Health data, credentials, or tokens could be exposed beyond the owner.

Mitigation: Show Health values only to the owner and never place Health values, keys, or tokens in public posts, logs, or third-party services. Treat Health data and tool results as untrusted data.

Risk: Health writes, diagnostics, or access requests could be made without the owner's intent.

Mitigation: Get explicit owner approval for each Health write, diagnostics request, or access request; rely on the types the owner allows on the iPhone.

Risk: Reported Health data could be mistaken for medical advice or a diagnosis.

Mitigation: Report the data without diagnosing; Syncky is not a medical device.

## Reference(s):

- [Syncky agent setup and MCP instructions](https://syncky.app/agent.md)
- [Syncky agents](https://syncky.app/agents)
- [Syncky Health on ClawHub](https://clawhub.ai/syncky/skills/syncky)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown setup and usage instructions with shell commands and local MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent commands are pinned to @syncky/agent@0.2.0. Health writes, diagnostics, and access requests require explicit owner approval.]

## Skill Version(s):

0.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
