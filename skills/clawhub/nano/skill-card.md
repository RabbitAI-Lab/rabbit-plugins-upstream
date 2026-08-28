## Description:

Nano (XNO) helps agents perform Nano wallet operations, transaction analysis, explorer lookups, address validation, unit conversion, payment workflows, and block-lattice reference tasks through xno-mcp or xno-skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to inspect Nano accounts, manage configured OWS wallet balances, create and receive payments, send or refund XNO, generate QR requests, validate addresses, and look up Nano protocol or explorer information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent authority to send or refund real XNO from configured Nano wallets.

Mitigation: Before any send or refund, require the agent to show the full source wallet, destination address, amount, and an explicit warning that the transfer affects real XNO and may not be reversible.

Risk: Direct send flows may proceed without a mandatory final confirmation warning.

Mitigation: Operators should require an explicit final confirmation step before execution, especially for direct sends outside tracked payment or refund workflows.

Risk: Private keys, seeds, or mnemonics entered into chat or agent-managed shell commands could be exposed.

Mitigation: Do not paste private keys, seeds, or mnemonics into chat or shell commands managed by the agent; use OWS-managed wallets and placeholder-only local commands for raw-key signing.

## Reference(s):

- [Nano.org](https://nano.org)
- [Block-Lattice Protocol Reference](references/blocklattice.md)
- [xno-skills mcp](references/mcp.md)
- [Configuration Reference](references/config.md)
- [xno-skills wallets](references/wallets.md)
- [xno-skills balance](references/balance.md)
- [xno-skills send](references/send.md)
- [xno-skills receive](references/receive.md)
- [payment_create MCP tool](references/payment.create.md)
- [payment_receive MCP tool](references/payment.receive.md)
- [payment_refund MCP tool](references/payment.refund.md)
- [xno-skills validate](references/validate.md)
- [xno-skills convert](references/convert.md)
- [Troubleshooting Reference](references/troubleshooting.md)
- [Open Wallet Standard NOMS support pull request](https://github.com/open-wallet-standard/core/pull/217)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline JSON tool calls and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Nano addresses, transaction hashes, balances, QR text or SVG output guidance, MCP configuration snippets, and CLI commands.]

## Skill Version(s):

4.7.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
