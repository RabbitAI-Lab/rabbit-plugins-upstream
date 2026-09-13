## Description:

Operates Keycloak and authentik identity providers with inventory, event review, OAuth client analysis, MFA and access-risk checks, and governed account or client remediation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, identity administrators, and security operators use this skill to inspect Keycloak or authentik users, sessions, events, groups, OAuth clients, MFA posture, and access risks. When authorized, they can use it to perform governed containment and remediation such as disabling users, revoking sessions, requiring password resets, replacing redirect URIs, or rotating client secrets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The executable package is installed unpinned and could differ from the reviewed artifact.

Mitigation: Pin or verify the identity-aiops package before installation and use trusted package sources.

Risk: The skill can perform high-impact identity-provider changes, including disabling users, revoking sessions, changing OAuth redirect URIs, and rotating client secrets.

Mitigation: Start with a view-only Keycloak service account or authentik token, grant manage permissions only when needed, and use dry-run previews before write actions.

Risk: Approval-related environment variables are audit annotations rather than enforcement controls.

Mitigation: Enforce authorization through identity-provider permissions and agent policy; do not treat audit annotation variables as approval gates.

Risk: The artifact reports mock validation with no recorded end-to-end run against a live identity provider.

Mitigation: Run setup validation and a live lab check against Keycloak or authentik before using the skill in a production identity environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/identity-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/Identity-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and normalized JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, audit and undo guidance, truncation flags, null-field reporting, and risk-tier labels.]

## Skill Version(s):

0.8.2 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
