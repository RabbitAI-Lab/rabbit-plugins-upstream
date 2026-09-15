## Description:

MinIO AIops helps agents diagnose and operate MinIO object storage, including capacity RCA, bucket exposure audits, lifecycle gaps, healing health, WORM retention, IAM exposure, and governed bucket writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and storage operators use this skill to triage MinIO health, capacity, exposure, lifecycle, retention, IAM, and healing issues, then perform audited maintenance changes when appropriate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change storage and IAM state and has no built-in read-only or approval gate for MCP writes.

Mitigation: Use read-only MinIO access keys by default and grant write or admin-capable credentials only for deliberate maintenance windows.

Risk: The skill runs through an external minio-aiops package that should not be installed implicitly without verification.

Mitigation: Pin and verify the exact minio-aiops package release before installing or running it.

Risk: Audit logs provide after-the-fact visibility rather than pre-execution approval.

Mitigation: Require operator approval before write workflows and review audit and undo records after maintenance.

Risk: The master password may be exposed if placed in broadly readable MCP client configuration.

Mitigation: Store MINIO_AIOPS_MASTER_PASSWORD through a protected secret mechanism.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/minio-aiops)
- [Project Homepage](https://github.com/AIops-tools/MinIO-AIops)
- [Capabilities Reference](references/capabilities.md)
- [Setup and Security Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with command examples and structured MinIO operations guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run steps, audit and undo guidance, and truncation notes for bounded listings.]

## Skill Version(s):

0.12.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
