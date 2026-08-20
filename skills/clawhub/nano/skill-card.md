## Description:

Nano (XNO) supports cryptocurrency wallet operations, transaction analysis, explorer lookups, sends and receives, balances, pending funds, address validation, unit conversion, transaction/hash/account lookup, and Nano block-lattice questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent work with Nano wallets, payments, account data, transaction history, explorer links, unit conversion, and block-lattice concepts through MCP tools or pinned CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate Nano sends or refunds from available wallets.

Mitigation: Review wallet names, destination addresses, and XNO amounts before approving any send or refund action.

Risk: The skill can use and change network RPC endpoints and save configuration.

Mitigation: Approve RPC endpoint changes only when needed and prefer known endpoints or operator-controlled infrastructure.

Risk: Raising maxSendXno increases the maximum amount an agent-assisted action can send.

Mitigation: Change maxSendXno only after an explicit operator decision and set the smallest limit needed for the task.

Risk: Wallet operations involve sensitive assets and may expose risk if secrets are exported or entered into chat.

Mitigation: Do not export mnemonics or private keys; keep signing through OWS-backed wallet flows or use local placeholders for any manual signing command.

## Reference(s):

- [Nano.org](https://nano.org)
- [Nano Skill on ClawHub](https://clawhub.ai/casualsecurityinc/skills/nano)
- [xno-skills MCP](references/mcp.md)
- [xno-skills Wallets](references/wallets.md)
- [xno-skills Send](references/send.md)
- [xno-skills Receive](references/receive.md)
- [xno-skills Balance](references/balance.md)
- [xno-skills Address Validation](references/validate.md)
- [xno-skills Unit Conversion](references/convert.md)
- [xno-skills RPC Account Info](references/rpc_account-info.md)
- [xno-skills RPC Receivable](references/rpc_receivable.md)
- [xno-skills QR](references/qr.md)
- [xno-skills Message Verification](references/verify.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline JSON tool calls and shell commands; command results may be JSON or text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses network RPC endpoints for Nano operations and may save configuration changes when explicitly requested.]

## Skill Version(s):

4.7.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
