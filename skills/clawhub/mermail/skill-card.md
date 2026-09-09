## Description:

Route broad, ambiguous, or cross-domain Mermail requests to the narrowest current workflow across MCP connection, CLI automation, agent inbox identity, inbox management, email composition, workspace admin, triage, mailbox-agent delegation, Composio integrations, scheduling/GTM/support/research/x402 personas, and Agent Wallet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use Mermail to route broad or multi-domain Mermail requests to the focused workflow that handles connection, mailbox, email, workspace, automation, integration, scheduling, support, research, x402, or wallet work. It is most useful when the user has not named a narrower Mermail skill or has combined several Mermail tasks in one request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routed tasks may involve sensitive mailbox, workspace, third-party integration, or payment actions.

Mitigation: Keep each routed action under explicit user approval and preserve the focused skill's own confirmation boundary.

Risk: The skill depends on a Mermail MCP connection and may require the MERMAIL_API_KEY environment variable for API-key mode.

Mitigation: Install it only for agents intended to connect to Mermail, and verify the active MCP profile and authentication mode before handling mailbox, workspace, or wallet work.

Risk: Inbound email, attachments, web content, paid-service content, and tool output can contain untrusted requests that try to change routing or authorize effects.

Mitigation: Use only the authenticated user's current request to select skills, targets, providers, payment terms, and external effects.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail ClawHub skill page](https://clawhub.ai/mermail/skills/mermail)
- [Mermail routing reference](references/routing.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with selected commands or configuration details when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to narrower Mermail skills and summarizes completed, pending, skipped, blocked, failed, and uncertain actions.]

## Skill Version(s):

1.2.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
