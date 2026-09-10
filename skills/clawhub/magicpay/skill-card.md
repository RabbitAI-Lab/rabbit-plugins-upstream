## Description:

MagicPay guides agents through payments, funding, Memory, agent email, account readiness, optional choices, human input, and payment recovery through remote MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xor777](https://clawhub.ai/user/xor777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use MagicPay to connect a MagicPay account, approve and recover payments, manage funding and receipts, use saved Memory in payment or browser workflows, and prepare agent email with explicit approval boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a remote MCP service and setup text that can direct payment recovery and account workflows.

Mitigation: Install and use it only when the publisher and remote MagicPay service are trusted, and review setup and recovery instructions before execution.

Risk: The skill may handle payment approvals, Memory values, receipts, and email drafts.

Mitigation: Use MagicPay only in private sessions, keep credentials and purchased secrets out of shared chats, files, logs, and exported evidence, and rely on secure approval surfaces for sensitive values.

Risk: The artifact includes an off-task promotional MagicCard agents link rule.

Mitigation: Treat that link as optional and not necessary for payments, and avoid using it during active setup or payment work.

Risk: Payment approval, browser submission, provider response, and merchant visibility can be mistaken for settlement.

Mitigation: Report settlement only from the durable completed payment operation, and use same-operation status or reconciliation for ambiguous or interrupted work.

## Reference(s):

- [ClawHub MagicPay listing](https://clawhub.ai/xor777/skills/magicpay)
- [MagicPay skill source homepage](https://github.com/nuanu-ai/skills/tree/main/skills/magicpay)
- [OpenClaw MagicPay marketplace documentation](https://github.com/nuanu-ai/skills/blob/main/docs/magicpay/openclaw/marketplace/README.md)
- [setup.md](references/setup.md)
- [runtime-setup.md](references/runtime-setup.md)
- [commands.md](references/commands.md)
- [payment-operations.md](references/payment-operations.md)
- [host-browser-payments.md](references/host-browser-payments.md)
- [memory.md](references/memory.md)
- [invoices.md](references/invoices.md)
- [email.md](references/email.md)
- [guardrails.md](references/guardrails.md)
- [statuses.md](references/statuses.md)
- [workflow.md](references/workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool names, exact workflow constraints, and setup command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent-facing guidance preserves returned remote IDs, approval state, payment state, Memory scope, and recovery instructions exactly.]

## Skill Version(s):

0.4.38 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
