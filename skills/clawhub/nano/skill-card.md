## Description:

Nano (XNO) cryptocurrency wallet operations, transaction analysis, and explorer lookups. Use for send/receive, balances, pending funds, address validation, unit conversion, tx/hash/account lookup, explorer links, and Nano block-lattice questions. Prefer xno-mcp first; use xno-skills CLI as fallback. Configured OWS wallets are the assistant's own wallets; never claim you cannot receive or hold Nano.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users can use this skill to let an agent work with configured Nano/XNO wallets, inspect balances and transaction history, create payment requests, validate addresses, produce explorer links, and guide send, receive, refund, and unit-conversion workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases could activate Nano wallet behavior for unrelated wallet, balance, invoice, refund, or account requests.

Mitigation: Confirm the user is asking about Nano/XNO when intent is ambiguous, and narrow activation before deployment when possible.

Risk: The skill can guide operations on configured Nano/XNO wallets, including sends and refunds.

Mitigation: Confirm every destination, amount, refund address, and send-limit change before allowing a transaction.

Risk: Private keys, seeds, or mnemonics exposed to an agent can leak through logs, memory, or downstream systems.

Mitigation: Never paste secret wallet material into the agent; use local-only commands with placeholders for any raw private-key signing workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/casualsecurityinc/skills/nano)
- [Nano.org](https://nano.org)
- [Block-Lattice Protocol Reference](references/blocklattice.md)
- [Configuration Reference](references/config.md)
- [Payment Create Reference](references/payment.create.md)
- [Payment Receive Reference](references/payment.receive.md)
- [Payment Refund Reference](references/payment.refund.md)
- [Troubleshooting Reference](references/troubleshooting.md)
- [OWS message signing pull request](https://github.com/open-wallet-standard/core/pull/217)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON tool calls and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nano addresses, transaction hashes, explorer links, payment request details, balance summaries, and terminal QR output.]

## Skill Version(s):

4.7.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
