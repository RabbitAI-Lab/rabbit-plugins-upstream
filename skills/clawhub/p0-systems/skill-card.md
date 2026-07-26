## Description: <br>
Deploy tokens on Solana, trade on pump.fun and Jupiter, and earn creator fees. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[serpepe](https://clawhub.ai/user/serpepe) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agent builders use this skill to connect an agent to P0 APIs for Solana token deployment, trading, creator-fee claiming, positions, alerts, credits, and account management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent live crypto trading, token deployment, purchasing, and account-management capabilities. <br>
Mitigation: Install only when this behavior is intended, require manual approval for deploys, trades, fee claims, purchases, upgrades, batch actions, and key revocation, and monitor all executed actions. <br>
Risk: The required P0 API key can authorize sensitive account and trading operations. <br>
Mitigation: Store P0_API_KEY only in environment or secret storage, rotate it when access changes, and use a dedicated low-balance wallet and API key for agent use. <br>
Risk: The artifact describes live financial actions without clear built-in approval or spending limits. <br>
Mitigation: Apply external spending, balance, and rate controls before use, and keep human approval in the workflow for every financially material action. <br>


## Reference(s): <br>
- [P0 Agents Homepage](https://agents.p0.systems) <br>
- [P0 Agents Skill Documentation](https://agents.p0.systems/skill.md) <br>
- [P0 Website](https://p0.systems) <br>
- [ClawHub Skill Page](https://clawhub.ai/serpepe/skills/p0-systems) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON examples] <br>
**Output Format:** [Markdown with curl commands and JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires P0_API_KEY and describes authenticated P0 API calls for token deployment, trading, fee claiming, alerts, credits, and account management.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
