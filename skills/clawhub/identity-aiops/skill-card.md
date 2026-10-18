## Description:

Helps agents investigate Keycloak and authentik identity activity, audit accounts and OAuth clients, assess MFA coverage, and perform identity changes when authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Identity administrators and security teams use this skill to investigate login failures, review stale access and MFA coverage, audit OAuth clients, and manage Keycloak or authentik users and sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identity changes can disable accounts, revoke sessions, alter redirect URIs, or rotate client secrets without an enforced tool-side approval gate.

Mitigation: Start with a least-privileged read-only service account or token; grant write permissions only when needed and review each proposed change before execution.

Risk: The master password and legacy environment secrets could expose identity-provider access if disclosed.

Mitigation: Protect IDENTITY_AIOPS_MASTER_PASSWORD and legacy secrets as sensitive credentials; avoid exposing them in logs or shared environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/identity-aiops)
- [Project homepage listed in skill metadata](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance and commands; JSON identity-operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers Keycloak and authentik; some changes are irreversible.]

## Skill Version(s):

0.11.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
