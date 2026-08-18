## Description:

Cash out Base USDC to fiat through Peer with custody-separated MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[adwilkinson](https://clawhub.ai/user/adwilkinson)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use Peer Cash to prepare and manage custody-separated Base USDC cash-outs to fiat through Peer, including payout estimates, ordered unsigned transaction plans, order tracking, withdrawals, top-ups, and recovery steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare transactions that affect real USDC funds.

Mitigation: Review the destination, value, calldata purpose, ordered steps, and expected effect before approving wallet signing or submission.

Risk: The MCP server or npm package could be misconfigured or differ from the intended Peer Cash implementation.

Mitigation: Confirm the installed package, MCP server configuration, and optional environment variables before using the skill for cash-outs.

Risk: Unknown transaction outcomes can lead to duplicate or incorrect recovery actions.

Mitigation: Inspect wallet activity, transaction hashes, receipts, and existing orders before retrying or resubmitting.

## Reference(s):

- [Peer Cash MCP repository](https://github.com/zkp2p/peer-cash-mcp)
- [ClawHub skill page](https://clawhub.ai/adwilkinson/skills/peer-cash)
- [Publisher profile](https://clawhub.ai/user/adwilkinson)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and transaction-review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces human-reviewable plans and operating guidance; signing and submission remain with the user, host, or connected wallet.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
