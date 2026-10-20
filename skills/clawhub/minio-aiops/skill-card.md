## Description:

Helps operators diagnose MinIO capacity, exposure, lifecycle, retention, and healing issues and manage bucket configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

MinIO operators and developers use this skill to investigate storage health, capacity, public exposure, lifecycle gaps, and healing, and to make targeted configuration changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can change MinIO storage and access settings without a built-in approval or read-only gate.

Mitigation: Start with a dedicated read-only or tightly scoped MinIO access key; authorize write-capable sessions deliberately.

Risk: Disabling TLS verification or sharing the master password can expose operational credentials.

Mitigation: Keep TLS verification enabled outside disposable labs and avoid storing the master password in shared or synced configuration.

Risk: Audit and undo records do not prevent an unauthorized or harmful change.

Mitigation: Review intended changes before execution and treat audit and undo as recovery aids, not permission controls.

## Reference(s):

- [MinIO AIops on ClawHub](https://clawhub.ai/zw008/skills/minio-aiops)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/AIops-tools/MinIO-AIops)
- [Capabilities](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Text and Markdown, with command examples and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can execute MinIO changes when connected with a write-capable access key; audit and undo are after-the-fact controls.]

## Skill Version(s):

0.14.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
