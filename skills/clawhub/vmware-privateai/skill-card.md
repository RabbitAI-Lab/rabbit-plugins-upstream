## Description:

vmware-privateai helps agents inspect VMware Private AI Foundation with NVIDIA GPU infrastructure, vGPU usage, utilization, profile catalogs, one scoped vGPU assignment workflow, and Private AI Service models and knowledge bases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inventory and triage GPU-backed VMware Private AI environments, inspect PAIS resources, and prepare or apply a constrained vGPU profile change for a powered-off VM.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide a vGPU profile change for one powered-off VM.

Mitigation: Use the validation or dry-run path first, require confirmation before applying the change, and run with a least-privilege vCenter account scoped to the intended GPU clusters.

Risk: Configuration uses vCenter credentials and a PAIS bearer token.

Mitigation: Store secrets outside the YAML config, protect the .env file, prefer an external secret manager, and keep TLS verification enabled outside self-signed lab environments.

Risk: PAIS endpoint or field assumptions may not match every live deployment.

Mitigation: Treat 404 or authentication failures as configuration and scope checks, verify PAIS base URLs and tokens, and confirm results against the target environment before operational decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-privateai)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI or MCP usage guidance and operational cautions for VMware Private AI GPU workflows.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
