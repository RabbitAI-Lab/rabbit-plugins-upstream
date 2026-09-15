## Description:

Identity AIops helps agents operate Keycloak and authentik identity providers, including users, sessions, events, clients, MFA coverage, root-cause analyses, and governed identity writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Identity, platform, and security engineers use this skill to inspect and operate Keycloak or authentik estates, triage login and access issues, audit OAuth client and MFA posture, and perform selected governed remediation tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact identity administration changes such as disabling users, revoking sessions, changing redirect URIs, and rotating client secrets.

Mitigation: Start with view-only Keycloak or authentik credentials, grant manage roles only for approved workflows, and use dry-run previews where available.

Risk: Server evidence reports unavailable provenance for this version and warns about use through an external package.

Mitigation: Review package provenance manually and pin the exact identity-aiops version intended for deployment.

Risk: Identity credentials, the master password, and local audit or undo state are sensitive operational data.

Mitigation: Protect IDENTITY_AIOPS_MASTER_PASSWORD and the ~/.identity-aiops directory, and migrate legacy plaintext secret environment variables before production use.

Risk: Approval metadata and risk labels are records, not enforcement gates.

Mitigation: Enforce authorization through least-privileged identity-provider accounts and agent policy rather than relying on the skill's recorded labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/identity-aiops)
- [Project homepage](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text guidance with inline shell commands, JSON-like tool results, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include normalized identity-provider data, truncation indicators, audit context, dry-run previews, undo references, and risk labels when supported by the tool.]

## Skill Version(s):

0.8.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
