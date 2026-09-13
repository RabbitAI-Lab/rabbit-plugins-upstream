## Description:

Helps agents manage VMware vSphere storage tasks including datastore browsing, deployable image discovery, iSCSI target configuration, and vSAN health and capacity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect datastores, locate deployable images, manage iSCSI targets, and check vSAN health and capacity from an agent through the local vmware-storage CLI or MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privileged VMware storage changes can affect host storage configuration or make LUN-backed VMs inaccessible.

Mitigation: Use least-privilege VMware service accounts, preview iSCSI writes with dry-run, require explicit approval or double confirmation, and enforce environment-scoped deny rules before production writes.

Risk: Runtime installation and local configuration can expose infrastructure credentials or weakened TLS settings.

Mitigation: Use a verified vmware-storage runtime, enable TLS certificate verification, prefer a secret manager over plaintext .env passwords, and keep .env permissions owner-only.

Risk: doctor --skip-auth can bypass authentication and connectivity checks, giving incomplete diagnostic confidence.

Mitigation: Treat --skip-auth only as a partial diagnostic and verify authentication and connectivity before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, configuration snippets, and JSON-shaped tool result expectations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP storage tools return structured results or list envelopes; write workflows should preview changes with dry-run and require explicit confirmation.]

## Skill Version(s):

1.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
