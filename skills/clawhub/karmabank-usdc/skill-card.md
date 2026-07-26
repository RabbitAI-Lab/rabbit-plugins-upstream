## Description: <br>
KarmaBank lets AI agents borrow testnet USDC based on Moltbook karma, with credit tiers from Bronze (50 USDC) to Diamond (1000 USDC) and zero interest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abdhilabs](https://clawhub.ai/user/abdhilabs) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
External developers and AI agent operators use KarmaBank to register agents, check Moltbook-based credit tiers, create Circle wallets, and propose testnet USDC borrowing or repayment actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet creation, borrowing, repayment, or related financial actions could affect funds or obligations if run without controls. <br>
Mitigation: Use only sandbox or test credentials, require explicit human approval, and enforce strict limits for every wallet, borrowing, and repayment operation. <br>
Risk: The security review flags insufficient safety boundaries for a financial agent skill. <br>
Mitigation: Inspect the complete CLI implementation and Circle wallet dependency before installation or execution. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/abdhilabs/skills/karmabank-usdc) <br>
- [Moltbook](https://moltbook.com) <br>
- [Circle Console](https://console.circle.com) <br>
- [USDC Agentic Hackathon](https://moltbook.com/m/usdc) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with CLI commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Moltbook and Circle credentials for connected wallet workflows; use sandbox or test credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
