## Description:

identity-aiops helps agents operate Keycloak and authentik identity providers for user, event, client, MFA, RCA, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and identity operations teams use this skill to inspect and triage Keycloak or authentik estates, audit users and OAuth clients, assess MFA coverage, and perform governed containment or remediation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact identity-provider changes without tool-enforced approval or a built-in read-only switch.

Mitigation: Use a dedicated least-privileged Keycloak service account or authentik token, start with read-only permissions at the identity provider, and require external human change control for high-risk writes.

Risk: The skill handles sensitive identity-provider credentials and a local master password.

Mitigation: Use the encrypted secrets store, avoid placing the master password in plaintext MCP configuration where possible, and migrate legacy environment-variable secrets into the encrypted store.

Risk: The artifact states it is mock-validated and has no recorded live identity-provider verification.

Mitigation: Verify the exact reviewed version in a self-hosted Keycloak or authentik lab before production use, and pin MCP startup to that trusted package version.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/identity-aiops)
- [Identity AIops homepage](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and normalized JSON from identity-provider read operations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operator-facing analysis and remediation guidance; write workflows should be reviewed through the user's normal identity change-control process.]

## Skill Version(s):

0.8.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
