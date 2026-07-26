## Description: <br>
AI agents borrow USDC based on their Moltbook karma score. Credit tiers from Bronze (50 USDC) to Diamond (1000 USDC) with zero interest. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abdhilabs](https://clawhub.ai/user/abdhilabs) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
External developers and agent operators use KarmaBank to register agents, check Moltbook-based credit tiers, and run CLI-driven USDC borrow, repay, and history workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Wallet credentials and USDC borrow, repay, or wallet creation actions could affect external accounts if production credentials are used. <br>
Mitigation: Use mock or testnet credentials, avoid production Circle secrets, and require explicit operator confirmation before wallet, borrow, or repay actions. <br>
Risk: The security summary flags insufficient scoping and unreviewed implementation around financial wallet behavior. <br>
Mitigation: Review the full source and external Circle wallet dependency before installation, and update or pin vulnerable dependencies before real financial use. <br>
Risk: Demo or mock scoring and ledger behavior may not represent enforceable credit decisions or real repayment state. <br>
Mitigation: Treat mock-mode results as non-production guidance until Moltbook and wallet integrations are reviewed and tested with non-production funds. <br>


## Reference(s): <br>
- [KarmaBank ClawHub listing](https://clawhub.ai/abdhilabs/skills/karmabank-minimal) <br>
- [KarmaBank GitHub repository](https://github.com/abdhilabs/karmabank) <br>
- [Moltbook](https://moltbook.com) <br>
- [Circle Console](https://console.circle.com) <br>
- [USDC Agentic Hackathon](https://moltbook.com/m/usdc) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and CLI command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include wallet, borrow, repay, and environment-variable guidance; require operator confirmation before financial actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
