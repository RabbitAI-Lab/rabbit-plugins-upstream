## Description:

Create, inspect, update, or deactivate a human-approved AgentMailer identity with a unique @agentmailer.ai address through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to create and manage human-approved AgentMailer identities and @agentmailer.ai inboxes through MCP, including listing, updating, and deactivating inboxes when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized or unapproved inbox provisioning.

Mitigation: Check the authenticated identity with auth_me and stop for human approval when the identity is unverified or the service returns human_approval_required.

Risk: Duplicate inbox creation during retries.

Mitigation: List existing inboxes before creation when appropriate and use a stable, task-specific idempotency key for create_inbox.

Risk: Deactivating the wrong mailbox.

Mitigation: Identify the exact inbox, explain that deactivation reserves its handle, and obtain explicit confirmation in the current conversation before delete_inbox.

Risk: Unexpected changes to organization-scoped inbox data.

Mitigation: Review AgentMailer permissions before installation and use returned resource IDs rather than guessed IDs for read, update, or delete operations.

## Reference(s):

- [Inbox tool reference](references/inbox-tools.md)
- [AgentMailer LLM instructions](https://api.agentmailer.ai/llms.txt)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, API Calls]

**Output Format:** [Text with structured AgentMailer inbox metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires authenticated AgentMailer MCP access; destructive inbox deactivation requires explicit confirmation.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
