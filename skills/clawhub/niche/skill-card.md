## Description: <br>
Trading card marketplace with partial USDC deposits. Browse cards, deposit partial amounts, and complete purchases with secure on-chain escrow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementsutjiatma](https://clawhub.ai/user/clementsutjiatma) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to browse, list, watch, and transact trading cards with partial USDC deposits and in-person inspection before completion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill schedules an uninspected external `niche check-matches` command every 15 minutes. <br>
Mitigation: Review the installed CLI and verify how to disable or remove the scheduled match-check job before enabling it. <br>
Risk: The skill guides agents through wallet, authentication, escrow, deposit, confirmation, cancellation, dispute, and browser transaction flows. <br>
Mitigation: Require explicit user approval before login, listing changes, deposits, confirmations, cancellations, disputes, funding, or browser transaction steps; prefer testnet or disposable accounts. <br>
Risk: The hosted CLI/backend trust boundary has limited containment detail in the security evidence. <br>
Mitigation: Install and use the skill only when the `niche` CLI and hosted backend are trusted, and review behavior before relying on wallet or escrow operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementsutjiatma/skills/niche) <br>
- [Hosted browser UI](https://niche-ddq89ltdk-clement-sutjiatmas-projects.vercel.app) <br>
- [Circle faucet for testnet USDC](https://faucet.circle.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and browser-flow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires node and may open browser flows for login, deposits, confirmations, funding, and card browsing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
