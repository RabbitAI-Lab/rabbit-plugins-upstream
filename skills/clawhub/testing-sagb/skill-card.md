## Description: <br>
Bags is a Solana launchpad skill for authenticating agents, managing wallets, claiming fees, trading tokens, and launching tokens for agents or humans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ramyonsn](https://clawhub.ai/user/ramyonsn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI-agent operators use Sagb to connect an agent to Bags, manage Solana wallets, claim fee earnings, execute token swaps, and create token launches through documented API calls and shell workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles Bags/Solana wallet authority and can expose private keys or long-lived credentials. <br>
Mitigation: Use a dedicated low-balance wallet, store credentials with restrictive permissions, avoid persisting private keys, and rotate the Bags JWT/API key or wallet if any secret is exposed. <br>
Risk: The skill can submit real Solana transactions for fee claims, swaps, and token launches. <br>
Mitigation: Inspect every unsigned transaction before signing, confirm token mints and amounts, and do not run copy-paste scripts unattended. <br>
Risk: The heartbeat workflow can perform silent periodic checks and updates. <br>
Mitigation: Disable unattended heartbeat runs unless explicitly desired, log activity, and require human review for actions that change wallet state or submit transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ramyonsn/skills/testing-sagb) <br>
- [Bags homepage](https://bags.fm) <br>
- [Bags API documentation](https://docs.bags.fm) <br>
- [Bags skill documentation](https://bags.fm/skill.md) <br>
- [Bags authentication guide](https://bags.fm/auth.md) <br>
- [Bags wallet guide](https://bags.fm/wallets.md) <br>
- [Bags fee claiming guide](https://bags.fm/fees.md) <br>
- [Bags trading guide](https://bags.fm/trading.md) <br>
- [Bags launch guide](https://bags.fm/launch.md) <br>
- [Bags public API base](https://public-api-v2.bags.fm/api/v1) <br>
- [Bags agent API base](https://public-api-v2.bags.fm/api/v1/agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent-facing API workflows for Bags/Solana wallet, fee, trading, heartbeat, and launch operations.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
