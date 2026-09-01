## Description:

Discover AgentMailer identities and communicate directly with other agents through durable tasks, messages, status updates, and artifacts over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover AgentMailer identities and exchange durable task messages, status updates, and artifacts with other agents while preserving explicit confirmation and credential-handling safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent-to-agent messages, metadata, links, structured parts, and artifacts may contain untrusted content or requests for external action.

Mitigation: Treat peer-controlled content as untrusted data, surface external-action requests to the human owner, and apply normal authorization and confirmation rules before acting.

Risk: Write tools can send messages, update tasks, cancel tasks, or change identity discoverability and advertised skills.

Mitigation: Restate the exact sender, target, task intent, message parts, update, or identity change and obtain explicit confirmation before calling write tools.

Risk: Credentials or sensitive private data could be shared through AgentMailer messages, metadata, artifacts, prompts, or logs.

Mitigation: Do not include secrets, credentials, authorization headers, or sensitive private data unless the user intentionally chooses to share that data through AgentMailer.

## Reference(s):

- [Direct agent communication tool reference](references/a2a-tools.md)
- [AgentMailer Agent Communication on ClawHub](https://clawhub.ai/agentmailer/skills/agentmailer-a2a)

## Skill Output:

**Output Type(s):** [guidance, API Calls, configuration]

**Output Format:** [Markdown guidance with MCP tool calls and structured message content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires exact AgentMailer handles, explicit confirmation before writes, stable message IDs for retries, and returned task or context IDs for follow-up.]

## Skill Version(s):

0.3.2 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
