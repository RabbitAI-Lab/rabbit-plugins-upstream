## Description: <br>
Identity AIops helps agents operate Keycloak and authentik identity providers by reading realm, user, event, client, MFA, and RCA data and performing audited account or client changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Identity, SSO, and platform operators use this skill to inspect Keycloak or authentik environments, diagnose login failures, stale access, OAuth client misconfiguration, and MFA gaps, and carry out governed remediation when authorized. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact account and OAuth client changes without an enforced approval or read-only gate. <br>
Mitigation: Use a dedicated least-privileged Keycloak service account or authentik token, start with view-only roles, and grant manage-users or manage-clients only for sessions where writes are intended. <br>
Risk: Audit approval variables are labels rather than enforcement controls. <br>
Mitigation: Treat IDENTITY_AUDIT_APPROVED_BY and IDENTITY_AUDIT_RATIONALE as audit metadata, and rely on IdP permissions plus agent instructions to control whether writes are allowed. <br>
Risk: Local configuration, encrypted secrets, audit logs, and undo records are stored under ~/.identity-aiops by default. <br>
Mitigation: Protect ~/.identity-aiops permissions, use the encrypted secrets store, and migrate away from the legacy plaintext secret environment fallback. <br>
Risk: The artifact reports mock validation and no recorded live end-to-end run against a real IdP. <br>
Mitigation: Run identity-aiops doctor and validate read and write workflows in a lab Keycloak or authentik target before production use. <br>


## Reference(s): <br>
- [Identity AIops source homepage](https://github.com/AIops-tools/Identity-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured identity-operation results with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include normalized identity-provider records, analysis findings, dry-run previews, audit labels, undo references, and operator guidance.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
