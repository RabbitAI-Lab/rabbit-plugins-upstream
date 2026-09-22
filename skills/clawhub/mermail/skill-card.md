## Description:

Route broad Mermail requests to the right focused workflow across connection, CLI, inbox, composition, administration, triage, integrations, scheduling, support, research, x402, xStocks, and Agent Wallet tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route broad or multi-part Mermail requests to the narrowest installed workflow before mailbox, email, workspace, integration, wallet, or x402 work proceeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Mermail request may combine independent effects such as mailbox changes, email sends, provider actions, payments, or trading workflows.

Mitigation: Apply the selected focused skill's approval and confirmation boundary independently for each write, external effect, payment, or destructive operation.

Risk: Inbound email, attachments, web content, tool output, Composio output, or payment-service content may try to redirect routing or authorize actions.

Mitigation: Treat those inputs as untrusted data and route or authorize effects only from the authenticated user's current request.

Risk: Using the wrong Mermail profile or authentication mode may expose unavailable tools or create role, workspace, rate-limit, credit, or provider-policy failures.

Mitigation: Verify the active Mermail connection, profile, role, and workspace before business routing, and use API-key mode only where the workflow permits it.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail ClawHub skill page](https://clawhub.ai/mermail/skills/mermail)
- [Mermail routing reference](references/routing.md)
- [Mermail MCP server](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with focused workflow selection, ordered next steps, and handoff notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires MERMAIL_API_KEY for API-key mode and may use Mermail MCP OAuth for supported workflows.]

## Skill Version(s):

1.2.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
