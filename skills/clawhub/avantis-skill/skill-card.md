## Description: <br>
Execute leverage trading on Avantis (Base) for crypto, forex, commodities, and indices using the Avantis Python SDK with direct wallet integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[droppingbeans](https://clawhub.ai/user/droppingbeans) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to inspect Avantis positions and open or close leveraged long/short positions on Base through the Avantis Python SDK. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet private keys and approvals can expose funds if used with a primary wallet or plaintext key material. <br>
Mitigation: Use only a dedicated low-value trading wallet, treat any bundled hardcoded private keys as compromised, and avoid plaintext private-key files. <br>
Risk: The skill can broadcast live leveraged trading transactions that may lose collateral quickly. <br>
Mitigation: Manually review the wallet, collateral, leverage, slippage, approval amount, take-profit, stop-loss, and close details before any transaction is broadcast. <br>
Risk: Under-scoped trade checks can allow unintended position size, leverage, or close behavior. <br>
Mitigation: Confirm balances, allowances, open positions, pair indices, and exit plan before opening or closing a trade. <br>


## Reference(s): <br>
- [Avantis Quick Start](references/quick-start.md) <br>
- [Avantis Platform](https://avantisfi.com) <br>
- [Avantis SDK Docs](https://sdk.avantisfi.com) <br>
- [Avantis Trading Guide](https://docs.avantisfi.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/droppingbeans/skills/avantis-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown guidance with bash command examples and terminal text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke Python scripts that read wallet credentials and broadcast Base mainnet trading transactions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter metadata version is 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
