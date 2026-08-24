## Description:

Nano (XNO) cryptocurrency wallet operations, transaction analysis, and explorer lookups. Use for send/receive, balances, pending funds, address validation, unit conversion, tx/hash/account lookup, explorer links, and Nano block-lattice questions. Prefer xno-mcp first; use xno-skills CLI as fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[casualsecurityinc](https://clawhub.ai/user/casualsecurityinc)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external users use this skill to guide Nano (XNO) wallet operations, transaction analysis, address validation, unit conversion, QR generation, and block-lattice lookups through MCP tools or pinned CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers could activate a money-moving Nano wallet skill in unrelated wallet or payment contexts.

Mitigation: Review and narrow trigger scope before installation, and require clarification when the user intent is not clearly Nano/XNO-specific.

Risk: Users may expose private keys or authorize spending limit increases without intending to grant wallet authority.

Mitigation: Do not accept private keys in agent context, and change spending limits only after explicit user instruction.

Risk: Wallet sends or refunds can move funds irreversibly if the destination or amount is wrong.

Mitigation: Validate destination addresses, check wallet balances before sending, and require explicit confirmation for refunds or draining balances.

## Reference(s):

- [Nano skill page](https://clawhub.ai/casualsecurityinc/skills/nano)
- [Nano protocol](https://nano.org)
- [MCP setup reference](artifact/references/mcp.md)
- [Balance command reference](artifact/references/balance.md)
- [Send command reference](artifact/references/send.md)
- [Receive command reference](artifact/references/receive.md)
- [Address validation reference](artifact/references/validate.md)
- [Unit conversion reference](artifact/references/convert.md)
- [Blocklattice representatives](https://blocklattice.io/representatives)
- [NanoTicker representatives](https://nanoticker.org/representatives)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls, JSON]

**Output Format:** [Markdown guidance with inline JSON tool calls and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce wallet operation plans, transaction summaries, explorer links, MCP configuration snippets, and pinned xno-skills CLI commands.]

## Skill Version(s):

4.7.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
