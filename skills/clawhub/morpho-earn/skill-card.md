## Description: <br>
Earn yield on USDC by supplying to the Moonwell Flagship USDC vault on Morpho (Base). Use when depositing USDC, withdrawing from the vault, checking position/APY, or setting up wallet credentials for DeFi yield. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lyoungblood](https://clawhub.ai/user/lyoungblood) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent operators use this skill to manage USDC yield positions on Base through the Moonwell Flagship USDC vault, including setup, deposits, withdrawals, APY checks, reward claims, and compounding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a wallet key to sign real on-chain transactions. <br>
Mitigation: Use a dedicated low-balance hot wallet, never a main wallet, and inspect every claim, approval, swap, deposit, and withdrawal before relying on automation. <br>
Risk: Auto-compounding can trigger future agent-driven transactions. <br>
Mitigation: Disable auto-compound unless explicitly desired and review any HEARTBEAT.md changes after setup. <br>
Risk: Wallet credentials and gas balances are operationally sensitive. <br>
Mitigation: Store keys securely, keep only limited funds available, and maintain enough Base ETH for intended transactions. <br>


## Reference(s): <br>
- [Wallet Setup](references/setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/lyoungblood/skills/morpho-earn) <br>
- [Morpho](https://morpho.org) <br>
- [Moonwell Vault Documentation](https://docs.moonwell.fi/moonwell/moonwell-overview/vaults) <br>
- [Vault on Morpho](https://app.morpho.org/vault?vault=0xc1256Ae5FF1cf2719D4937adb3bbCCab2E00A2Ca&network=base) <br>
- [Merkl](https://merkl.xyz) <br>
- [Odos](https://odos.xyz) <br>
- [viem](https://viem.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, plain text, JSON reports, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agent-run TypeScript scripts that read wallet configuration and submit on-chain transactions after review.] <br>

## Skill Version(s): <br>
1.2.0 (source: SKILL.md frontmatter and server release metadata; package.json is 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
