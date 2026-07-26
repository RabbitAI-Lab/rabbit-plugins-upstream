## Description: <br>
Etherlink blockchain interaction - EVM-compatible L2 on Tezos. Supports mainnet and shadownet testnet via MCP server. Use for balance checks, transactions, smart contracts, and token operations on Etherlink. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[efekucuk](https://clawhub.ai/user/efekucuk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and web3 operators use this skill to configure Etherlink mainnet or shadownet access, check balances, inspect blocks and transactions, call smart contracts, and prepare token or XTZ operations through an MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write operations may require a wallet private key that can sign real Etherlink transactions. <br>
Mitigation: Use read-only mode when possible, use a dedicated low-value wallet for write operations, and never use a primary wallet or key with funds you cannot afford to lose. <br>
Risk: The MCP server code and package invoked by the skill can affect transaction behavior. <br>
Mitigation: Pin and review the package before use, and test operations on shadownet before using mainnet. <br>
Risk: Etherlink differs from standard Ethereum behavior, including legacy gas pricing and unsupported filter or subscription endpoints. <br>
Mitigation: Use legacy gas pricing, follow the documented supported RPC methods, and account for public RPC rate limits. <br>


## Reference(s): <br>
- [Etherlink Skill on ClawHub](https://clawhub.ai/efekucuk/skills/etherlink-skill) <br>
- [Etherlink Docs](https://docs.etherlink.com/) <br>
- [Etherlink Bridge Docs](https://docs.etherlink.com/building-on-etherlink/bridging) <br>
- [Etherlink Mainnet Explorer](https://explorer.etherlink.com) <br>
- [Etherlink Shadownet Explorer](https://shadownet.explorer.etherlink.com) <br>
- [Etherlink Shadownet Faucet](https://shadownet.faucet.etherlink.com) <br>
- [Network Reference](references/networks.md) <br>
- [Etherlink Differences](references/differences.md) <br>
- [MCP Setup](references/mcp-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON, bash, and blockchain operation examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP configuration snippets, network identifiers, RPC endpoint guidance, and transaction or contract-call instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
