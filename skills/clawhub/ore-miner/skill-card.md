## Description: <br>
Autonomous ORE mining on Solana via refinORE. Onboard humans, start/stop sessions, optimize tile strategies, track P&L, manage risk, auto-restart, multi-coin mining (SOL/USDC/stablecoins), DCA/limit orders, staking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jusscubs](https://clawhub.ai/user/jusscubs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to configure a refinORE API key, check wallet status, start and monitor ORE mining sessions, adjust mining strategy, and review mining performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to deploy and manage user funds through persistent refinORE mining automation. <br>
Mitigation: Use only with a deliberately funded refinORE account, keep balances small, and require explicit confirmation before starting mining or enabling auto-restart. <br>
Risk: A long-lived API key could permit ongoing account actions if exposed or misused. <br>
Mitigation: Store REFINORE_API_KEY only as an environment variable, prefer revocable or scoped keys if available, and know how to revoke the key before use. <br>
Risk: Live strategy changes and DCA or limit-order actions can alter financial exposure. <br>
Mitigation: Require confirmation before changing live strategies or creating, updating, or canceling DCA and limit orders. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jusscubs/skills/ore-miner) <br>
- [refinORE App](https://automine.refinore.com) <br>
- [refinORE API Base URL](https://automine.refinore.com/api) <br>
- [API Endpoints](references/api-endpoints.md) <br>
- [Mining Rules](references/mining-rules.md) <br>
- [Strategies](references/strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands, API examples, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REFINORE_API_URL and REFINORE_API_KEY, plus bash, curl, and python3 for bundled helper scripts.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
