## Description:

Routes broad or cross-domain Mermail requests to the narrowest focused workflow across connection, CLI automation, inbox, email composition, workspace administration, integrations, scheduling, support, x402, and Agent Wallet tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route ambiguous or multi-step Mermail requests to the correct focused workflow before performing mailbox, compose, workspace, integration, scheduling, support, wallet, or payment work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Mermail routing can involve email, workspace administration, integrations, and payments.

Mitigation: Review connected account permissions and keep write actions, sends, provider actions, and payments separately confirmed by the focused downstream skills.

Risk: Mailbox content, tool output, provider output, or payment challenge text could try to influence routing or authorization.

Mitigation: Treat those inputs as untrusted data and rely only on the authenticated user's current request to select a skill, target, recipient, provider, account, payment term, or effect.

Risk: PayBox and wallet actions require the correct profile, role, and authorization boundary.

Mitigation: Use full-profile OAuth where required, respect owner-only boundaries, and do not retry uncertain writes or payments through another client or skill.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail MCP server](https://console.mermail.app/mcp)
- [Mermail routing reference](references/routing.md)

## Skill Output:

**Output Type(s):** [guidance, configuration]

**Output Format:** [Markdown guidance with skill names and ordered workflow steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to focused Mermail skills and preserves separate confirmation boundaries for writes, sends, provider actions, and payments.]

## Skill Version(s):

1.2.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
