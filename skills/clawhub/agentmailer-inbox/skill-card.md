## Description:

Create, inspect, update, or deactivate a human-approved AgentMailer identity with a unique @agentmailer.ai address through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external AgentMailer users use this skill to create and manage human-approved AgentMailer inbox identities, including listing, inspecting, updating, and deactivating inboxes with permission checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected AgentMailer account permissions may allow inbox creation, updates, or deactivation.

Mitigation: Install only when the agent should manage AgentMailer inbox identities and review the authenticated account permissions before use.

Risk: Deleting an inbox deactivates the mailbox and reserves its handle.

Mitigation: Identify the exact inbox and obtain explicit confirmation in the current conversation before calling delete_inbox.

Risk: Inbox creation may be blocked when the identity is unverified or human approval is required.

Mitigation: Stop and follow the AgentMailer human-approved signup sequence instead of retrying or bypassing approval.

## Reference(s):

- [Inbox tool reference](references/inbox-tools.md)
- [AgentMailer quickstart](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-quickstart)
- [AgentMailer human-approved signup example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-human-approved-signup)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)
- [AgentMailer agent onboarding](https://api.agentmailer.ai/llms.txt)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Text, Configuration]

**Output Format:** [Markdown or plain text with AgentMailer inbox details and safe next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the inbox handle, inbox ID, address, display name, and relevant metadata when creation or lookup succeeds.]

## Skill Version(s):

0.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
