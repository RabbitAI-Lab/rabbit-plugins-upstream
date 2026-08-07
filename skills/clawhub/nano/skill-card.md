## Description:

Nano (XNO) cryptocurrency wallet operations, transaction analysis, and explorer lookups. Use for send/receive, balances, pending funds, address validation, unit conversion, tx/hash/account lookup, explorer links, and Nano block-lattice questions. Prefer xno-mcp first; use xno-skills CLI as fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to manage Nano/XNO wallet workflows, inspect balances and transaction history, validate addresses, generate payment QR codes, and look up Nano account or block information. It is intended for Nano protocol tasks only, with MCP tools preferred and CLI commands used as a fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers can activate the skill for generic wallet, balance, invoice, pending-funds, or account-opening requests outside the intended Nano/XNO context.

Mitigation: Confirm the task is specifically about the Nano protocol before using the skill; ask for clarification when the word Nano could refer to another product or concept.

Risk: Balance checks can automatically claim pending funds by broadcasting receive or open blocks.

Mitigation: Install and enable the skill only where automatic receipt of pending Nano funds is acceptable, and review wallet actions before running balance workflows in sensitive accounts.

Risk: Send, refund, and representative-change operations can affect wallet funds or delegation.

Mitigation: Confirm full destination addresses, refund recipients, amounts, representative changes, and spending-limit changes with the operator before execution.

Risk: Raw private-key signing could expose secret material if a key is pasted into an agent context.

Mitigation: Do not provide private keys or mnemonics to the agent; use the documented placeholder command locally for low-level signing and use OWS-backed flows for wallet operations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/casualsecurityinc/skills/nano)
- [Nano Protocol](https://nano.org)
- [xno-skills MCP Reference](artifact/references/mcp.md)
- [Wallet Balance Reference](artifact/references/balance.md)
- [Send Reference](artifact/references/send.md)
- [Receive Reference](artifact/references/receive.md)
- [Address Validation Reference](artifact/references/validate.md)
- [Blocklattice Representatives](https://blocklattice.io/representatives)
- [Nanoticker Representatives](https://nanoticker.org/representatives)
- [OWS Message Signing Support PR](https://github.com/open-wallet-standard/core/pull/217)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and bash command examples; tool results may be returned as structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access for wallet, RPC, and explorer operations; address validation and diagnostics can operate without network access.]

## Skill Version(s):

4.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
