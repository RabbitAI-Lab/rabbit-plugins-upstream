## Description:

Create, inspect, update, or deactivate a human-approved AgentMailer identity with a unique @agentmailer.ai address through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and manage human-approved AgentMailer identities and their associated @agentmailer.ai inboxes. It helps agents list, inspect, update, and deactivate inboxes while respecting AgentMailer authorization and confirmation requirements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an AgentMailer-authorized account to create, update, or deactivate inboxes.

Mitigation: Install it only when those account actions are intended, review metadata before updates, and require explicit confirmation before mailbox deactivation.

## Reference(s):

- [Inbox tool reference](references/inbox-tools.md)
- [AgentMailer human approval and signup guidance](https://api.agentmailer.ai/llms.txt)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [ClawHub skill page](https://clawhub.ai/agentmailer/skills/agentmailer-inbox)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Configuration, Text]

**Output Format:** [Markdown or plain text summaries of AgentMailer MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include inbox handle, inbox ID, address, display name, and metadata returned by AgentMailer.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
