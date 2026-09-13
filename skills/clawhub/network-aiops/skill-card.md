## Description:

Network AIops helps agents inspect, diagnose, back up, diff, merge, replace, and roll back configurations on NAPALM-supported network devices, with optional NetBox lookups and governed audit/undo controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers and network engineers use this skill to query multi-vendor device state, run read-only RCA, compare intended changes, and perform governed configuration changes on Cisco IOS/IOS-XE, Nexus NX-OS, IOS-XR, Arista EOS, and Juniper Junos devices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants high-impact access to network devices and can affect production infrastructure.

Mitigation: Install only in a controlled network-operations environment, pin the package version, and use read-only device and NetBox accounts by default.

Risk: Credential and approval handling can be under-scoped when the master password or raw secret output is exposed to model-visible tools.

Mitigation: Avoid putting the master password in shell profiles or MCP config, do not use include_secrets=True through model-visible tools, and keep enable secrets out of config.yaml.

## Reference(s):

- [Network AIops source repository](https://github.com/AIops-tools/Network-AIops)
- [Network AIops ClawHub page](https://clawhub.ai/zw008/skills/network-aiops)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands, configuration snippets, diffs, and structured tool-result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include network state summaries, RCA findings, dry-run diffs, backup guidance, and explicit operator approval steps for writes.]

## Skill Version(s):

0.12.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
