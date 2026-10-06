## Description:

Coordinates supervised DeFi agent sessions, policy checks, approvals, and receipts while keeping execution preview-gated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi agent operators use this skill to coordinate supervised intent planning, policy checks, user approvals, and receipt tracking across persistent sessions. Wallet-changing actions require separate signing and an enabled execution mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DeFi automation can cause financial loss if grant scopes or budgets are too broad.

Mitigation: Limit allowlists, spending caps, and expiry; verify grant state and revoke access when no longer needed.

Risk: A proposed or prepared action may be mistaken for an executed and settled transaction.

Mitigation: Use USER_SIGNED execution unless a bounded grant and operational execution gate are deliberately approved; check authoritative receipts before dependent actions.

Risk: Exposing wallet secrets would compromise signing authority.

Mitigation: Never provide private keys, seed phrases, or RPC credentials to the skill.

## Reference(s):

- [FarmDash Autonomous Operator on ClawHub](https://clawhub.ai/parmasanandgarlic/skills/farmdash-autonomous-operator)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash live capability status](https://www.farmdash.one/api/v1/agent/status)
- [FarmDash security and authority boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [Guidance, Text, API calls]

**Output Format:** [Text and structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intent, approval, session, and receipt status; a cycle result is not proof of settlement.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
