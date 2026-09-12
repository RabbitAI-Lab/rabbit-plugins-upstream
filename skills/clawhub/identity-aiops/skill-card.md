## Description:

Identity AIops helps agents operate Keycloak or authentik identity providers for user, event, client, MFA, root-cause-analysis, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, identity administrators, and operations engineers use this skill to inspect Keycloak or authentik identity environments, triage login and access issues, audit OAuth clients and MFA coverage, and carry out audited identity changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with Keycloak service-account or authentik API-token authority.

Mitigation: Start with view-only roles or a least-privileged token, and grant manage-users or manage-clients permissions only for sessions where writes are intended.

Risk: Some identity writes can disable users, revoke sessions, replace redirect URIs, or rotate client secrets.

Mitigation: Use dry-run previews and double confirmation where available, review audit annotations, and stage dependent deployments before rotating client secrets.

Risk: The MCP process can fetch the package through uvx, which may run external code if not pinned and verified.

Mitigation: Pin and verify the identity-aiops package before use and avoid exposing broad environment variables to the MCP process.

Risk: Legacy plaintext secret environment variables are still accepted as a fallback.

Mitigation: Migrate legacy secrets into the encrypted store and provide only the required runtime environment variables to the MCP server.

## Reference(s):

- [Identity-AIops GitHub repository](https://github.com/AIops-tools/Identity-AIops)
- [identity-aiops ClawHub page](https://clawhub.ai/zw008/skills/identity-aiops)
- [identity-aiops capabilities](references/capabilities.md)
- [identity-aiops CLI reference](references/cli-reference.md)
- [identity-aiops setup and security guide](references/setup-guide.md)
- [identity-aiops agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON tool results, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces identity-provider observations, analysis guidance, command guidance, and governed-operation recommendations for an agent.]

## Skill Version(s):

0.8.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
