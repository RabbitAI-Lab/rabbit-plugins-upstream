## Description:

Inspect Mermail Agent Wallet and PayBox balances, guide browser funding handoffs, and create or submit human-approved USDC transfer proposals through Mermail MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users with OAuth-connected Mermail workspaces use this skill to inspect Agent Wallet balances, hand off funding to the Mermail console, and create or submit reviewed USDC transfer proposals on Base or Solana.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth wallet scopes allow the agent to inspect wallet data and help prepare transfer submission workflows.

Mitigation: Grant wallet scopes only when needed, verify the MCP session is OAuth-based, and review wallet:read and wallet:transact consent before use.

Risk: USDC transfers on mainnet may be irreversible after approval and submission.

Mitigation: Confirm the exact chain, amount, and destination before proposal creation and again before submission; require explicit acknowledgement for irreversible transfer submission.

Risk: Funding, checkout, and approval URLs are browser-only and may be redacted from model-visible tool output.

Mitigation: Use the Mermail console funding handoff link and do not attempt to recover redacted MoonPay or approval URLs in chat.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agent Wallet Skill Page](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Agent Wallet tool map](references/tools.md)
- [Agent Wallet security boundary](references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool-call sequencing, console links, and optional shell command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OAuth wallet scopes for wallet actions; transfer submission guidance includes human confirmation and mainnet irreversibility acknowledgement.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
