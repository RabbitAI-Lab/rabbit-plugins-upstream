## Description: <br>
Nano (XNO) supports cryptocurrency wallet operations, transaction analysis, explorer lookups, address validation, unit conversion, and block-lattice guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and wallet operators use this skill when an agent needs to work with Nano/XNO wallets, balances, pending funds, payment requests, transaction history, explorer links, and Nano protocol questions. The skill guides MCP tool use first and CLI commands as a fallback for compatible agent environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can automatically broadcast receive/open transactions and may activate on generic wallet, balance, invoice, or open-account requests. <br>
Mitigation: Install it only for Nano/XNO wallet work and require explicit confirmation before receive/open, send, refund, representative change, or spending-limit/config changes. <br>
Risk: Wallet seeds or private keys could be exposed if they are provided to an agent. <br>
Mitigation: Do not share seeds or private keys with the agent; use OWS-managed wallet flows and placeholder commands when private-key signing is unavoidable. <br>
Risk: Ambiguous refund, send, or representative-change requests can move funds or alter wallet governance incorrectly. <br>
Mitigation: Validate destination addresses, show full addresses and amounts, and require operator confirmation before executing value-moving or representative-changing actions. <br>


## Reference(s): <br>
- [Nano Protocol](https://nano.org) <br>
- [MCP Reference](references/mcp.md) <br>
- [Wallets Reference](references/wallets.md) <br>
- [Balance Reference](references/balance.md) <br>
- [Receive Reference](references/receive.md) <br>
- [Send Reference](references/send.md) <br>
- [Transaction History Reference](references/history.md) <br>
- [Address Validation Reference](references/validate.md) <br>
- [Unit Conversion Reference](references/convert.md) <br>
- [QR Reference](references/qr.md) <br>
- [Message Signing Reference](references/sign.md) <br>
- [Message Verification Reference](references/verify.md) <br>
- [Representative Change Reference](references/change-rep.md) <br>
- [RPC Account Balance Reference](references/rpc_account-balance.md) <br>
- [RPC Account Info Reference](references/rpc_account-info.md) <br>
- [RPC Receivable Reference](references/rpc_receivable.md) <br>
- [RPC Capability Probe Reference](references/rpc_probe-caps.md) <br>
- [Submit Block Reference](references/submit-block.md) <br>
- [Block Send Reference](references/block_send.md) <br>
- [Block Receive Reference](references/block_receive.md) <br>
- [Block Change Reference](references/block_change.md) <br>
- [Diagnostics Reference](references/diag.md) <br>
- [Nano Representative Lists](https://blocklattice.io/representatives) <br>
- [NanoTicker Representatives](https://nanoticker.org/representatives) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON tool-call examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access for RPC-backed wallet and explorer operations; address validation and unit conversion can be performed offline.] <br>

## Skill Version(s): <br>
4.5.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
