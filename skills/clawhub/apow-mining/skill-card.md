## Description:

Set up APoW Easy Mode with one Base ETH deposit, a recoverable encrypted wallet, and remote GPU mining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentoshi](https://clawhub.ai/user/agentoshi)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to set up a recoverable, dedicated wallet and run APoW Easy Mode mining on Base with remote GPU services, subject to explicit approval and spending limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mining spends deposited funds on transactions and paid services, and gas or exchange rates may exceed quoted estimates.

Mitigation: Require explicit approval and a dedicated low-balance wallet; honor approved budgets and enforced action limits, and stop if a cost exceeds them.

Risk: Losing the wallet password or keystore can make deposited funds inaccessible; sharing secrets exposes the wallet.

Mitigation: Verify recovery before funding, keep separate durable backups, and never request or disclose wallet secrets in chat.

Risk: An unclear payment or transaction result can lead to duplicate charges or an inaccurate claim of mining success.

Mitigation: Stop and reconcile uncertain outcomes before resuming; report a confirmed mine only with its Base transaction hash.

## Reference(s):

- [ClawHub APoW Mining release](https://clawhub.ai/agentoshi/skills/apow-mining)
- [APoW assistant profiles](https://apow.io/docs/technical/assistants)
- [APoW managed mining status](https://apow.io/docs/technical/managed-mining)
- [MoltCaptcha](https://github.com/MoltCaptcha/MoltCaptcha)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Transaction status reports]

**Output Format:** [Markdown with inline bash commands and status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports confirmed mines with a Base transaction hash; does not promise yield or profitability.]

## Skill Version(s):

0.12.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
