## Description: <br>
Web3 Trader helps agents prepare DEX swaps, smart swap orders, and Hyperliquid trades by returning quotes, transaction data, wallet review links, QR-code guidance, and order or account status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deanpeng-dotcom](https://clawhub.ai/user/deanpeng-dotcom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to prepare crypto trade workflows, including DEX swap previews, hosted wallet-signing pages, smart swap orders, and Hyperliquid account, order, and position operations. Users remain responsible for reviewing wallet prompts, trade terms, approvals, and risk controls before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: This is a real crypto-trading skill that can enable automated trades and uses live trading credentials such as agent keys. <br>
Mitigation: Review carefully before installing, start with test or very small balances, treat any agent key as a live trading credential, and avoid using a main wallet private key. <br>
Risk: Wallet addresses, intended trades, preview links, and signatures may be shared with external trading services. <br>
Mitigation: Use only accounts and trade sizes appropriate for that exposure, review wallet prompts before signing, and revoke token approvals or Hyperliquid agent permissions when finished. <br>
Risk: The server security summary reports inconsistent disclosure around custody, automatic wallet prompts, approvals, and exposed trading credentials. <br>
Mitigation: Disable automatic small-trade execution when possible and require explicit confirmation for meaningful balances, leverage, approvals, or order changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deanpeng-dotcom/web3-trader) <br>
- [Antalpha MCP Server](https://mcp-skills.ai.antalpha.com/mcp) <br>
- [Hyperliquid MCP Tools Specification](references/HL_MCP_TOOLS_SPEC.md) <br>
- [Security Guidelines](references/SECURITY.md) <br>
- [Configuration Example](references/config.example.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON tool results, shell commands, configuration snippets, preview URLs, and QR-code file guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local configuration, transaction logs, hosted preview links, and wallet-signing flows; users must review and approve trades in their wallet or authorized trading account.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
