## Description:

Claw Future is a Chinese futures trading assistant for CTP-based market monitoring, order placement, conditional orders, scheduled tasks, and daily close reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yoborlon-alpha](https://clawhub.ai/user/yoborlon-alpha)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading agents use this skill to operate a CTP-connected Chinese futures account: checking funds, positions, orders, trades, quotes, subscriptions, order confirmations, cancellations, conditional orders, scheduled orders, and close-of-day reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control futures trading accounts, including placing and cancelling orders.

Mitigation: Require explicit user confirmation for high-impact actions, test in simulation first, and verify account, contract, direction, volume, and price before execution.

Risk: Server evidence reports hard-coded external infrastructure in deployment guidance.

Mitigation: Replace hard-coded host and address values with user-approved placeholders before installation or use.

Risk: Server evidence reports an unauthenticated local control channel.

Mitigation: Require authentication for daemon IPC or restrict the control channel to a trusted local environment before use.

Risk: Configured account credentials and generated logs may contain sensitive financial data.

Mitigation: Protect configuration and runtime files, avoid sharing them, and narrow audit and log retention to the minimum operational need.

Risk: Dependencies may be unconstrained or need patched versions.

Mitigation: Pin dependencies to reviewed, patched versions before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yoborlon-alpha/skills/claw-future)
- [Project Homepage](https://gitee.com/hongoutech/future-claw)
- [Agent Training Guide](references/agent-training.md)
- [Common Futures Instruments](references/instruments.md)
- [Deployment Guide](deploy/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables, concise natural-language guidance, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include order-confirmation prompts, account or market status summaries, and risk reminders before high-impact trading actions.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
