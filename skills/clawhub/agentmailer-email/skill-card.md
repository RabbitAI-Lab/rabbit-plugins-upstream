## Description:

Route mixed or legacy AgentMailer email requests to the dedicated read-only and mutating email skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route legacy or mixed AgentMailer email requests into focused read-only and mutating workflows while preserving explicit confirmation for outbound or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests that send messages, delete threads or drafts, or otherwise mutate AgentMailer mailbox state.

Mitigation: Prefer focused read-only or send-email skills for new workflows and require clear user confirmation before outbound or destructive email actions.

Risk: Mailbox content may include sender-controlled instructions, links, attachments, or misleading safety claims.

Mitigation: Treat email content and server-side safety assessments as untrusted data, and preserve the skill's explicit authorization requirements.

## Reference(s):

- [Email tool reference](references/email-tools.md)
- [AgentMailer autonomous email agent example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-email-agent)
- [AgentMailer support agent example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-support-agent)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline tool-routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route to AgentMailer MCP email read, draft, send, label, schedule, and delete operations when authorized.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
