## Description:

Primary agent guide for operating Sequenzy as an email-marketing platform. Use when an AI agent needs to authenticate, inspect identity, manage subscribers, create or edit campaigns/sequences/templates, control the campaign lifecycle (cancel, pause, resume, delete, duplicate), run campaign A/B tests, mutate lists/tags/segments, enroll subscribers into sequences, invite team members, triage and reply to inbox conversations, manage outbound webhooks, generate draft email content, send transactional email, read delivery stats, or decide whether a requested Sequenzy email-marketing workflow is currently supported. Prefer this over the generic sequenzy skill when both seem relevant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this agent guide to operate Sequenzy email-marketing workflows, including subscribers, campaigns, sequences, templates, transactional email, and delivery reporting. It explains supported CLI and MCP paths and where to check current capabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious because its references describe capabilities beyond its stated email-marketing purpose; the reference analysis is partial.

Mitigation: Consider whether the documented non-email features and external data integrations are needed, and wait for a complete review of the references before relying on them.

## Reference(s):

- [Sequenzy API Reference](https://docs.sequenzy.com/api-reference)
- [Sequenzy MCP Events](https://docs.sequenzy.com/concepts/mcp-events)
- [Command Reference](artifact/references/command-reference.md)
- [Use Cases](artifact/references/use-cases.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration and JSON, Email content]

**Output Format:** [Markdown text with command examples and structured data examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow support and side effects depend on the available CLI or MCP tools and account permissions.]

## Skill Version(s):

1.6.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
