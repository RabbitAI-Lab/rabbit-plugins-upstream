## Description:

Helps operators inspect and manage Keycloak and authentik users, sign-in events, OAuth clients, and MFA coverage, including account containment and client changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Identity administrators and security teams use this skill to investigate login failures, review dormant accounts and MFA coverage, audit OAuth clients, and carry out approved account or client changes in Keycloak or authentik.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Identity administration actions can disable accounts, terminate sessions, change redirects, or rotate secrets without a built-in approval gate.

Mitigation: Start with read-only credentials; require independent human approval before changes and grant write permissions only when needed.

Risk: Session revocation and client-secret rotation are irreversible and can disrupt access or connected applications.

Mitigation: Confirm the target and impact, stage dependent services before rotation, and use dry runs where available.

Risk: Broadly exposed master-password environment variables can disclose the identity-provider credential store.

Mitigation: Keep IDENTITY_AIOPS_MASTER_PASSWORD out of broad shell environments and use narrowly scoped secret delivery.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities and platform support](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Text and Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports Keycloak and authentik, not cloud identity providers; live identity-provider verification is not documented.]

## Skill Version(s):

0.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
