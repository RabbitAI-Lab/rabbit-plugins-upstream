## Description:

Identity AIops helps agents operate Keycloak and authentik identity providers for user, event, client, MFA, root-cause analysis, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, identity administrators, and security operators use this skill to inspect and administer Keycloak or authentik estates, triage login and lockout incidents, audit stale access and OAuth clients, measure MFA coverage, and perform governed containment changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact identity-provider writes can disable or enable users, revoke sessions, require password resets, replace redirect URIs, or rotate client secrets without a tool-enforced approval gate.

Mitigation: Run the skill with a least-privilege Keycloak service account or authentik token, start with view-only roles, use dry-run where available, and grant manage-users or manage-clients only after operator approval.

Risk: Audit rows and risk labels record activity but do not block unsafe or unauthorized actions.

Mitigation: Enforce authorization through IdP permissions and agent operating procedures, and review the local audit log after sensitive workflows.

Risk: The artifact says live IdP validation has not been recorded and modeled REST paths remain verification debt.

Mitigation: Validate against a self-hosted Keycloak or authentik lab and run the doctor check before using the skill against production identity infrastructure.

Risk: Client secret rotation and session revocation are irreversible workflows.

Mitigation: Stage dependent service changes before rotating secrets and confirm session-revocation targets with read commands before executing writes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/identity-aiops)
- [Project Homepage](https://github.com/AIops-tools/Identity-AIops)
- [capabilities.md](references/capabilities.md)
- [cli-reference.md](references/cli-reference.md)
- [setup-guide.md](references/setup-guide.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands return normalized JSON; write workflows expose dry-run support, risk labels, and audit records.]

## Skill Version(s):

0.8.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
