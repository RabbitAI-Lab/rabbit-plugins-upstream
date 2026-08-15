## Description:

minio-aiops helps agents diagnose and operate MinIO object storage, including capacity RCA, exposure audits, lifecycle gaps, healing health, WORM retention, IAM, and governed bucket changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and storage operators use this skill to inspect MinIO health, capacity, exposure, lifecycle, WORM retention, IAM, and healing status, then apply governed maintenance changes through CLI or MCP tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes high-impact write tools without a built-in read-only mode or approval gate.

Mitigation: Use read-only MinIO IAM credentials for audits and diagnosis; reserve admin or write credentials for deliberate maintenance windows.

Risk: The MCP server is write-capable whenever configured MinIO credentials allow writes.

Mitigation: Store MINIO_AIOPS_MASTER_PASSWORD through the MCP host's secret mechanism and scope MinIO credentials to the session's intended permissions.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/MinIO-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/minio-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with CLI commands, MCP tool guidance, JSON-shaped tool results, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool results may include bounded listings with returned, limit, and truncated fields.]

## Skill Version(s):

0.11.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
