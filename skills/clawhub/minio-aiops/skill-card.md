## Description:

MinIO AIops helps agents operate and diagnose MinIO object storage, including capacity root-cause analysis, bucket exposure audits, lifecycle and retention checks, healing health, service status, per-bucket configuration, and governed storage changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and storage operators use this skill to triage MinIO health, capacity, exposure, lifecycle, WORM retention, IAM, and healing questions, then produce cautious operational guidance or governed CLI/MCP actions for approved maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run an unpinned external package while using MinIO storage credentials.

Mitigation: Pin minio-aiops to a reviewed exact version or otherwise verify package integrity before installation.

Risk: Write and administrative operations can affect bucket policy, lifecycle, quota, retention, users, and bucket deletion.

Mitigation: Use a dedicated read-only MinIO access key by default, grant write or admin permissions only for an approved maintenance window, and review proposed changes before execution.

Risk: A master password or MinIO credentials in committed configuration could expose storage access.

Mitigation: Keep MINIO_AIOPS_MASTER_PASSWORD and MinIO secrets out of committed files; use the encrypted secret store and client environment configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/minio-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/MinIO-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MinIO CLI or MCP operations; write operations should be reviewed and run with least-privilege credentials.]

## Skill Version(s):

0.12.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
