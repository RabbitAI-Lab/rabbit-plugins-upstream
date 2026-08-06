## Description: <br>
Use 84 FarmDash MCP tools for supervised DeFi research, swaps, simulations, perps, ACP commerce, portfolio intelligence, and MEV-aware execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and DeFi agents use this skill to research DeFi opportunities, compare and simulate swaps or perpetuals, and operate supervised wallet-affecting workflows through local signing or bounded delegation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can prepare wallet-affecting DeFi trades, perpetual orders, and delegated automation. <br>
Mitigation: Require a fresh quote, verify token addresses, chains, fees, slippage, destination wallets, budgets, allowlists, and revocation settings, and obtain explicit confirmation before any signing or execution. <br>
Risk: Private keys, seed phrases, or wallet exports could compromise user funds if shared with an agent or service. <br>
Mitigation: Never provide private keys, seed phrases, or mnemonics; use local EIP-191/EIP-712 signing or explicitly bounded delegation only. <br>
Risk: Airdrop, sybil-risk, and automation guidance could be misused to evade protocol rules or third-party terms. <br>
Mitigation: Use simulations and audits for defensive planning, do not generate evasion patterns, and halt when protocol rules, jurisdiction, or evidence quality is unclear. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect) <br>
- [FarmDash Agents Homepage](https://www.farmdash.one/agents) <br>
- [FarmDash MCP Configuration](https://www.farmdash.one/.well-known/mcp.json) <br>
- [FarmDash OpenAPI Specification](https://www.farmdash.one/agents/openapi.yaml) <br>
- [FarmDash Fee Structure](https://www.farmdash.one/fees) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with inline commands, API call procedures, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include DeFi risk disclosures, quote and simulation review steps, wallet-signing guardrails, and MCP/API setup guidance.] <br>

## Skill Version(s): <br>
1.2.20 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
