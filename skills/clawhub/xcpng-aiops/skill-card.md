## Description:

xcpng-aiops helps agents operate and triage XCP-ng virtualization fleets through Xen Orchestra, covering fleet health, VM, host, pool, storage, snapshot, backup, and task workflows with RCA analyses and governed writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and virtualization administrators use this skill to inspect, diagnose, and operate XCP-ng fleets managed by Xen Orchestra. It supports read workflows, RCA summaries, and guarded write actions such as VM lifecycle operations, migration, snapshots, and SR rescans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact infrastructure write actions can affect production VMs, snapshots, storage repositories, and migration workflows.

Mitigation: Use a dedicated least-privilege Xen Orchestra account, prefer read-only tokens for triage, run dry-run previews before write tools, and reserve production writes for reviewed maintenance windows.

Risk: Mutable package execution can change behavior if the installed executable is not pinned or verified.

Mitigation: Pin and verify the xcpng-aiops package version before using write tools on production infrastructure.

Risk: Weak built-in authorization controls mean the skill records actions but does not decide whether a write is allowed.

Mitigation: Enforce authorization through Xen Orchestra ACLs or scoped tokens, and protect local MCP configuration and ~/.xcpng-aiops permissions.

Risk: Credential exposure could allow unintended access to Xen Orchestra.

Mitigation: Avoid storing XCPNG_AIOPS_MASTER_PASSWORD in synced or version-controlled configuration, and protect the encrypted secret store and MCP client config.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [Project issues](https://github.com/AIops-tools/XCPng-AIops/issues)
- [Capabilities reference](artifact/references/capabilities.md)
- [CLI reference](artifact/references/cli-reference.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Xen Orchestra object identifiers, RCA findings, dry-run previews, and audit-oriented operational guidance.]

## Skill Version(s):

0.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
