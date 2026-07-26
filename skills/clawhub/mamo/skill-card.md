## Description: <br>
Interact with Mamo DeFi yield strategies on Base (Moonwell). Deposit/withdraw USDC, cbBTC, MAMO, or ETH into automated yield strategies. Check APY rates and account status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anajuliabit](https://clawhub.ai/user/anajuliabit) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Mamo to check APYs and manage Base yield strategies for USDC, cbBTC, MAMO, and ETH. The skill can help create strategy contracts, approve deposits, withdraw funds, and report account or portfolio status through CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks agents to handle a raw wallet private key and can sign transactions or authentication messages. <br>
Mitigation: Use only a dedicated wallet with limited funds, never a primary wallet key, and confirm the exact code version before use. <br>
Risk: The skill can create contracts, approve token spending, deposit or withdraw assets, and call remote Mamo endpoints. <br>
Mitigation: Confirm every transaction and signature request, use dry-run mode before execution, and check that contract addresses and endpoints match the documented release. <br>
Risk: The skill stores local strategy information under ~/.config/mamo. <br>
Mitigation: Review local configuration contents and avoid using shared or untrusted execution environments for wallet-connected runs. <br>


## Reference(s): <br>
- [ClawHub Mamo listing](https://clawhub.ai/anajuliabit/skills/mamo) <br>
- [Mamo CLI README](README.md) <br>
- [Mamo Contract Addresses and ABIs](references/contracts.md) <br>
- [Mamo API Reference](references/mamo-api.md) <br>
- [Mamo Docs](https://docs.mamo.xyz) <br>
- [Mamo Contracts](https://github.com/moonwell-fi/mamo-contracts) <br>
- [Mamo](https://mamo.xyz) <br>
- [Moonwell](https://moonwell.fi) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [CLI text with optional JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can run dry-run simulations or execute Base mainnet actions that return balances, APY data, gas estimates, transaction hashes, and status summaries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter and package.json report 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
