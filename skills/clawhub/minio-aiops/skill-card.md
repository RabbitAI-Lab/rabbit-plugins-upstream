## Description:

MinIO AIops helps agents diagnose and operate MinIO object storage, including capacity root-cause analysis, bucket exposure audits, lifecycle and retention gap checks, healing health, IAM exposure review, and governed storage changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage operators, and site reliability engineers use this skill to inspect MinIO health, capacity, bucket exposure, lifecycle behavior, object-lock retention, IAM exposure, and safe remediation options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes powerful MinIO storage and IAM write operations without an enforceable built-in read-only or approval gate.

Mitigation: Start with a read-only MinIO access key, widen permissions only during deliberate maintenance windows, and review dry-run previews and audit records before making changes.

Risk: Operational credentials and the master password can grant broad access to MinIO targets if handled carelessly.

Mitigation: Avoid storing the master password in persistent client configuration when possible, protect the local MinIO AIops state directory, and keep write-capable credentials tightly scoped.

Risk: Unpinned package installation can pull a later release than the one reviewed in this card.

Mitigation: Pin the minio-aiops package version to 0.12.3 when installing for reviewed or production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/minio-aiops)
- [Project homepage](https://github.com/AIops-tools/MinIO-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool listings and analysis results may be bounded; when a result reports truncation, users should increase the limit or narrow the query before acting on it.]

## Skill Version(s):

0.12.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
