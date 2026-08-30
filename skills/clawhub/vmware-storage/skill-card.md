## Description:

Manages VMware vSphere storage tasks for datastores, iSCSI targets, and vSAN clusters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware datastores, find deployable images, configure iSCSI storage, and check vSAN health and capacity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates in a high-impact VMware storage environment, and weakened connection checks can create false confidence.

Mitigation: Review before production installation, use least-privilege VMware service accounts, set verify_ssl: true with trusted certificates, and do not treat doctor --skip-auth as proof of safe authentication.

Risk: iSCSI changes can affect host storage configuration and may make LUNs unavailable if applied incorrectly.

Mitigation: Run write operations with dry-run first, require explicit human approval for iSCSI changes, and verify target reachability and LUN usage before changing targets.

Risk: Credentials stored in local environment files can be exposed if file permissions are too broad.

Mitigation: Keep ~/.vmware-storage/.env permissions at 600 or inject secrets from a dedicated secret manager.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](artifact/references/setup-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [VMware Storage Capabilities](artifact/references/capabilities.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, configuration snippets, and JSON-like tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include VMware storage observations, dry-run previews, audit-aware write guidance, and troubleshooting steps.]

## Skill Version(s):

1.8.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
