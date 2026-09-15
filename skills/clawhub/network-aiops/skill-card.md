## Description:

Network AIops helps agents operate NAPALM-supported network devices by reading device state, running diagnostics, backing up configurations, previewing diffs, and performing governed configuration changes across Cisco IOS/IOS-XE, Nexus NX-OS, IOS-XR, Arista EOS, and Juniper Junos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Network operators, SREs, and infrastructure engineers use this skill to inspect device facts, interfaces, BGP and LLDP neighbors, routing tables, environmental health, and NetBox source-of-truth data. They can also generate backups, preview configuration diffs, and execute audited merge, replace, rollback, confirm, or undo workflows with human approval and appropriate device privileges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact write operations against production network devices.

Mitigation: Install it only in controlled environments, use read-only device and NetBox credentials by default, and allow write-capable credentials only for approved change workflows.

Risk: Configuration replace, merge, rollback, confirm, and undo actions can affect device reachability or network behavior.

Mitigation: Require operators to run config_diff first, review the exact diff, use dry-run paths where available, and verify reachability from a new session before confirming timed commits.

Risk: Credential exposure is possible if master passwords or raw configuration secrets are placed in prompts, static config, shell profiles, or hosted-model transcripts.

Mitigation: Keep device passwords and NetBox tokens in the encrypted store, avoid enable secrets in config.yaml, protect NETWORK_AIOPS_MASTER_PASSWORD, and avoid include_secrets=True in hosted-model conversations.

Risk: The package is installed or launched from external package resolution paths.

Mitigation: Pin or verify the network-aiops package before granting write access to production devices.

## Reference(s):

- [Network-AIops repository](https://github.com/AIops-tools/Network-AIops)
- [Network-AIops issues](https://github.com/AIops-tools/Network-AIops/issues)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured tool-result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include redacted configuration text, dry-run diffs, diagnostic findings, audit and undo identifiers, and warnings for unsupported drivers or missing safety nets.]

## Skill Version(s):

0.12.3 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
