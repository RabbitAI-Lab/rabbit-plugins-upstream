## Description:

Mermail Agent Wallet helps agents inspect PayBox balances, guide funding and onramp handoff, and create or submit USDC transfer proposals on Base or Solana with human confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Mermail Agent Wallet or PayBox status, hand off funding to the official console, and prepare or submit reviewed USDC transfer proposals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet workflows can affect real USDC transfers if the user approves an incorrect mailbox, chain, amount, or destination.

Mitigation: Verify the mailbox, chain, amount, and destination before any transfer; use proposal preview and explicit confirmation before submission.

Risk: Funding, MoonPay, Apple Pay, and passkey approval flows may be mishandled if attempted through chat-visible links.

Mitigation: Use only the official Mermail or PayBox console flow for funding and approval; do not expose or invent checkout URLs in chat.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Skill Page](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Security Boundary](references/security.md)
- [Agent Wallet Tool Map](references/tools.md)
- [Mermail MCP Server](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool-call sequencing and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include reviewed transaction proposal details, funding handoff links to the official console, and OAuth scope guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
