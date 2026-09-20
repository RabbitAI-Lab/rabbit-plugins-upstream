## Description:

Routes broad, ambiguous, or cross-domain Mermail requests to the narrowest current workflow across MCP connection, CLI automation, mailbox, email, workspace, integration, scheduling, support, research, x402, xStocks, and Agent Wallet tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this root Mermail routing skill to choose the focused Mermail workflow for ambiguous or multi-domain mailbox, workspace, integration, scheduling, payment, and wallet requests before taking action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can route requests toward workflows that affect email, workspace administration, external integrations, payments, or wallet operations.

Mitigation: Use it only with the intended Mermail MCP server and verify that the focused skill and provider approval prompts match the exact action requested before approving any effect.

Risk: Email, attachment, web, provider, or tool output could try to influence routing or authorize an action.

Mitigation: Treat those sources as untrusted data and allow only the authenticated user's current request to select skills, targets, payment terms, or external effects.

Risk: A broad or multi-step request may combine independent writes, sends, integrations, payments, or destructive operations.

Mitigation: Split the work by domain and require separate, exact authorization for each write, external effect, payment, or destructive action.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP server](https://console.mermail.app/mcp)
- [Mermail routing reference](references/routing.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with skill-routing decisions, ordered action summaries, and optional command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to focused Mermail skills and preserves independent approval boundaries for writes, external integrations, payments, and destructive actions.]

## Skill Version(s):

1.2.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
