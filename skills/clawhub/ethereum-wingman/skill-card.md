## Description: <br>
Ethereum development tutor and builder for Scaffold-ETH 2 projects that guides agents through Solidity, DeFi, Scaffold-ETH 2, security practices, and fork-mode testing against real protocol state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jp4g](https://clawhub.ai/user/jp4g) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering agents use this skill to build, test, and review Ethereum dApps with Scaffold-ETH 2, Solidity, DeFi protocol patterns, and local fork workflows. It also provides security checklists, common gotchas, and historical exploit lessons for smart contract development. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can prompt agents to run npx, yarn, Anvil, and cast commands for Ethereum development workflows. <br>
Mitigation: Run commands in a development directory, review third-party package installs, and keep Anvil and cast pointed at a local fork unless intentionally moving beyond local testing. <br>
Risk: Fork-mode workflows and wallet testing can be confused with production blockchain operations. <br>
Mitigation: Use local burner wallets and avoid real wallets or production RPC credentials unless the operator explicitly chooses a production workflow. <br>
Risk: Broad activation terms may cause Ethereum-specific guidance to be applied outside the intended Scaffold-ETH or smart contract context. <br>
Mitigation: Install and activate this skill only when Ethereum, Solidity, DeFi, web3, or Scaffold-ETH development guidance is desired. <br>


## Reference(s): <br>
- [Critical Ethereum Development Gotchas](references/critical-gotchas.md) <br>
- [Automation, Incentives & Keepers](references/automation-and-incentives.md) <br>
- [Historical Hacks: Teachable Moments](references/historical-hacks.md) <br>
- [SpeedRun Ethereum](https://speedrunethereum.com/) <br>
- [Scaffold-ETH](https://scaffoldeth.io/) <br>
- [Scaffold-ETH Documentation](https://docs.scaffoldeth.io/) <br>
- [OpenZeppelin Documentation](https://docs.openzeppelin.com/) <br>
- [Uniswap Documentation](https://docs.uniswap.org/) <br>
- [Aave Documentation](https://docs.aave.com/) <br>
- [Chainlink Documentation](https://docs.chain.link/) <br>
- [Rekt News Leaderboard](https://rekt.news/leaderboard/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline Solidity, TypeScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include project setup commands, local fork testing steps, smart contract review notes, and configuration changes for Scaffold-ETH 2 or Cursor.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
