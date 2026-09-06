## Description:

Orchestrate policy-bounded DeFi sessions, OODA plans, intent state, circuit breakers, and recovery; execution stays status-gated and separately authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External DeFi operators and agent builders use this skill to coordinate supervised or policy-bounded autonomous sessions, maintain intent state, check delegation and grants, apply circuit breakers, and recover from interrupted control loops without giving the agent key custody.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated DeFi automation can create high-impact financial loss if authority is too broad or left active too long.

Mitigation: Use narrow, time-limited, revocable grants; verify grant scope and status before autonomous execution; revoke or narrow grants after the objective is complete.

Risk: A user may mistake configuration, a session token, or a chat instruction for execution authority.

Mitigation: Require separate user signing or an active scoped grant for wallet-changing actions, and verify every approval payload before signing.

Risk: Autonomous decisions can become unsafe when session state, event data, approvals, receipts, or grant status are stale or incomplete.

Mitigation: Refresh context and event snapshots before decisions, use heartbeat and recovery checks, halt on stale or unknown settlement states, and require manual review after interrupted sessions.

Risk: Secrets exposure would undermine the skill's zero-custody boundary.

Mitigation: Never provide seed phrases, private keys, mnemonics, or RPC credentials; treat session tokens as sensitive runtime capabilities.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-autonomous-operator)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical FarmDash Autonomous Operator Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-autonomous-operator/SKILL.md)
- [Agent Integration Documentation](https://www.farmdash.one/docs)
- [Live Agent Capability Status](https://www.farmdash.one/api/v1/agent/status)
- [OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Security and Authority Boundaries](https://www.farmdash.one/security)
- [Fees and Commercial Terms](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown guidance with structured tool-call responses and JSON status data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live status, freshness, policy, approval, and grant checks before state-changing actions.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
