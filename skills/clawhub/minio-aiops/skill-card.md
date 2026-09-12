## Description:

MinIO AIops helps agents diagnose and operate MinIO object storage through health checks, capacity and lifecycle analysis, exposure audits, healing status, bucket configuration reads, and governed storage administration actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and storage administrators use this skill to investigate MinIO health, capacity, exposure, lifecycle, WORM retention, IAM, and healing issues, then apply scoped bucket or account changes when appropriate. It is intended for MinIO deployments and explicitly routes non-MinIO storage tasks to other skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact MinIO administration actions and does not provide a built-in read-only or approval gate.

Mitigation: Start with a read-only MinIO IAM key, grant write or admin credentials only for sessions where changes are intended, and use dry-run previews before state-changing operations.

Risk: The skill relies on an external minio-aiops package that can change outside the skill text.

Mitigation: Review the package source or pin installation to an exact trusted release before use in sensitive environments.

Risk: Credential handling is sensitive because the MCP server needs access to a master password for non-interactive use.

Mitigation: Avoid storing the real master password in ordinary MCP configuration when possible and prefer environment or secret-management controls appropriate to the deployment.

Risk: Disabling TLS certificate verification can hide endpoint impersonation or misconfiguration outside lab environments.

Mitigation: Keep TLS verification enabled for production and shared environments; disable it only for self-signed lab certificates.

Risk: The artifact reports mocked validation but no recorded end-to-end run against a live MinIO server.

Mitigation: Run minio-aiops doctor and a non-production overview check against the target deployment before relying on live operational findings.

## Reference(s):

- [MinIO AIops homepage](https://github.com/AIops-tools/MinIO-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/minio-aiops)
- [capabilities.md](references/capabilities.md)
- [setup-guide.md](references/setup-guide.md)
- [cli-reference.md](references/cli-reference.md)
- [agent-guardrails.md](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and structured MinIO operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded listings, ranked findings, dry-run previews, audit context, and undo guidance depending on the requested MinIO task.]

## Skill Version(s):

0.12.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
