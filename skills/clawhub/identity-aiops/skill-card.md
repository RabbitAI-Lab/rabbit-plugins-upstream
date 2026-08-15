## Description:

Identity AIops helps agents operate Keycloak and authentik identity providers for realm, user, session, event, OAuth client, MFA, and access-risk analysis, with governed identity write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, identity administrators, and operations teams use this skill to inspect Keycloak or authentik environments, triage login and access issues, audit OAuth clients and MFA coverage, and perform controlled account or client remediation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected identity account with write permissions can allow immediate account, session, or client changes without a tool-enforced approval gate.

Mitigation: Use a least-privilege Keycloak service account or authentik token, preferably view-only for observation workflows, and grant write permissions only when remediation is intentionally required.

Risk: Client secret rotation, redirect URI replacement, session revocation, and user enable or disable actions can disrupt authentication flows or user access.

Mitigation: Use dry-run previews where available, review audit and undo behavior before execution, and stage dependent application changes before rotating secrets or replacing redirect URIs.

Risk: Local identity configuration, encrypted secrets, audit logs, and undo data under ~/.identity-aiops can expose sensitive operational context if poorly protected.

Mitigation: Protect ~/.identity-aiops, keep the encrypted secret store and master password secure, and review audit and undo retention according to local policy.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/identity-aiops)
- [Project homepage](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline shell commands, configuration examples, and normalized JSON from tool or CLI operations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include identity-provider observations, heuristic analyses, dry-run previews, audit context, undo guidance, and truncation indicators.]

## Skill Version(s):

0.7.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
