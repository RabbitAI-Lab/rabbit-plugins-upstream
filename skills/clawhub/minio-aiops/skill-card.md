## Description:

MinIO AIops helps agents diagnose and operate MinIO object storage, including capacity root-cause analysis, bucket exposure audits, lifecycle gap analysis, healing health checks, and governed bucket configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage operators, and SREs use this skill to inspect MinIO health, capacity, exposure, lifecycle, and healing state, then prepare or execute governed remediation steps when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete MinIO storage resources when supplied credentials permit write operations.

Mitigation: Install and run it with a dedicated least-privilege MinIO key, preferably read-only for diagnostic sessions; use write-capable or admin credentials only for intended remediation.

Risk: The security evidence says the skill has no built-in MCP approval gate.

Mitigation: Rely on host-side approvals, IAM boundaries, dry-run previews, and operator review before policy, lifecycle, quota, upload purge, or bucket delete actions.

Risk: A master password is used to unlock stored MinIO secrets for non-interactive operation.

Mitigation: Treat MINIO_AIOPS_MASTER_PASSWORD as a real secret and provide it through the MCP client's protected environment configuration.

## Reference(s):

- [Capabilities Reference](references/capabilities.md)
- [Setup and Security Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [MinIO AIops Source Homepage](https://github.com/AIops-tools/MinIO-AIops)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/minio-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MinIO findings, risk-ranked recommendations, dry-run previews, audit/undo notes, and bounded listing truncation notices.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
