## Description: <br>
Run policy-bounded autonomous DeFi agents with session keys, OODA control loops, intent state, circuit breakers, recovery, and zero-custody execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and DeFi operators use this skill to coordinate policy-bounded autonomous DeFi sessions, intent lifecycle checks, approvals, circuit breakers, and recovery without giving private keys to the agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Autonomous DeFi execution can create high-impact financial losses if grants, budgets, or approvals are too broad. <br>
Mitigation: Keep session-key grants narrow, scoped, time-limited, and revocable; verify expiry and revocation paths; review every EIP-712 approval before signing. <br>
Risk: Users could misunderstand a session token, context patch, or chat message as execution authority. <br>
Mitigation: Treat execution authority as a separate signed grant or approval step, and never equate session state or natural-language configuration with permission to execute. <br>
Risk: Private keys, seed phrases, or sensitive session tokens could be exposed during operation. <br>
Mitigation: Never provide private keys or seed phrases to the skill, keep session tokens out of normal user-facing prose, and store runtime credentials securely. <br>
Risk: Receipts or event snapshots may be misread as proof of fills, finality, realized profit and loss, or external settlement. <br>
Mitigation: Use only returned, source-labeled evidence; require policy, simulation, approval, and observation gates; halt dependent actions when settlement is pending, partial, unknown, or unsupported. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-autonomous-operator) <br>
- [FarmDash Autonomous DeFi Agent Platform](https://www.farmdash.one/agents) <br>
- [FarmDash DeFi Intelligence Homepage](https://www.farmdash.one/) <br>
- [Canonical Autonomous Operator Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-autonomous-operator/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, JSON, API Calls] <br>
**Output Format:** [Markdown guidance with structured JSON tool responses and EIP-712 approval payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use FARMDASH_API_KEY for higher tiers; workflows require explicit policy, simulation, and approval gates before state-changing execution.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
