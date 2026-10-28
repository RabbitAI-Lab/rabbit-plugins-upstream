## Description:

Business tools for your OpenClaw agent through one MCP server: a CRM, email inboxes, phone numbers it answers, invoices and bookkeeping, a booking calendar, e-signatures and a help desk. Conecto is a paid service, charged per tool call from a prepaid balance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conecto](https://clawhub.ai/user/conecto)

### License/Terms of Use:

MIT-0

## Use Case:

Small business owners and their agents use Conecto to read and manage business information across CRM, email, phone, invoicing, bookkeeping, scheduling, e-signature, and help desk tools. Agents can also use it to send customer communications and perform other business actions through an authenticated MCP connection.

### Deployment Geography for Use:

Global; phone numbers are described for the United States and Canada.

## Known Risks and Mitigations:

Risk: Business data is processed by Conecto, and tool calls can incur usage charges or recurring rental costs.

Mitigation: Select only the business areas the agent needs, and review Conecto's data terms, tool prices, balance, and account limits before use.

Risk: External communications and business changes can affect customers or create charges.

Mitigation: Ask the user before external or costly actions, and enable approval rules for important record changes.

## Reference(s):

- [Conecto OpenClaw guide](https://conecto.chat/agents/openclaw)
- [Conecto tool catalog](https://conecto.chat/tools.md)
- [Tool descriptions and prices](https://conecto.chat/tools/llms.txt)
- [Conecto error guide](https://conecto.chat/docs/errors.md)
- [Conecto service and pricing information](https://conecto.chat/ai-questions)

## Skill Output:

**Output Type(s):** [API Calls, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Authenticated MCP tool calls, tool results, and Markdown setup guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available actions depend on the business areas the user authorizes; tool calls may incur usage charges.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
