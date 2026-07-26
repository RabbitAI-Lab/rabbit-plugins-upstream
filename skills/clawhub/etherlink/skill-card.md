## Description: <br>
Etherlink Skill helps agents interact with Etherlink, an EVM-compatible Layer 2 on Tezos, through an MCP server for balance checks, transactions, smart contracts, and token operations on mainnet or Shadownet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[efekucuk](https://clawhub.ai/user/efekucuk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and web3 operators use this skill to configure Etherlink network access, query balances and chain data, and prepare contract or token operations through an Etherlink MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An external MCP server configured with a private key can sign real Etherlink transactions. <br>
Mitigation: Prefer read-only mode, use Shadownet first, avoid primary wallet keys, and use a dedicated low-balance wallet for write operations. <br>
Risk: Transaction requests may target the wrong network, recipient, amount, contract, or gas settings. <br>
Mitigation: Manually verify the network, recipient, amount, contract, and gas before allowing any transaction to be signed. <br>
Risk: Private keys can be exposed through unsafe local configuration or source control practices. <br>
Mitigation: Provide private keys only through environment variables, never commit them, and omit the key entirely for read-only usage. <br>
Risk: Public Etherlink RPC endpoints are rate-limited and may be unsuitable for high-throughput production use. <br>
Mitigation: Use a dedicated RPC provider or run an Etherlink node when higher request volume or stronger availability is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/efekucuk/skills/etherlink) <br>
- [Etherlink website](https://etherlink.com) <br>
- [Etherlink documentation](https://docs.etherlink.com/) <br>
- [Etherlink bridging documentation](https://docs.etherlink.com/building-on-etherlink/bridging) <br>
- [Etherlink mainnet explorer](https://explorer.etherlink.com) <br>
- [Etherlink Shadownet explorer](https://shadownet.explorer.etherlink.com) <br>
- [Etherlink Shadownet faucet](https://shadownet.faucet.etherlink.com) <br>
- [Etherlink network reference](references/networks.md) <br>
- [Etherlink MCP server setup](references/mcp-setup.md) <br>
- [Etherlink differences from standard Ethereum](references/differences.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands, code] <br>
**Output Format:** [Markdown with JSON configuration snippets, shell commands, and natural-language operation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Etherlink network identifiers, RPC endpoint guidance, MCP server configuration, transaction prompts, and troubleshooting notes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
