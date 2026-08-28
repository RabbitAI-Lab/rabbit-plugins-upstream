## Description:

Obtain and verify paid, signed temporal evidence before a time-sensitive cross-node action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[violetclaire](https://clawhub.ai/user/violetclaire)

### License/Terms of Use:

MIT-0

## Use Case:

Wallet-enabled agents and their operators use this skill to obtain independently verifiable temporal receipts before acting within time-sensitive execution windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a paid external time-verification call.

Mitigation: Confirm the task needs external signed time evidence, enforce local payment approval, and apply spending limits before use.

Risk: Private task details could be exposed if sent to the external service.

Mitigation: Keep task payloads, schedules, trust state, callbacks, and outcomes participant-local.

Risk: An invalid, stale, redirected, or unverified receipt could support the wrong time-sensitive decision.

Mitigation: Require the exact challenged resource URL, verify the ES256 signature and service identity, validate timing relationships, and fail closed when verification or local policy checks cannot be completed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/violetclaire/skills/popcorn-temporal-anchor)
- [POPCORN agent homepage](https://767-2676.com/agents)
- [Current service offer](https://767-2676.com/agent/offer)
- [Canonical execution contract](https://767-2676.com/SKILL.md)
- [POPCORN signing keys](https://767-2676.com/.well-known/popcorn-keys.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown instructions with URLs and protocol checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to verify signed temporal receipts and apply local execution-window policy.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
