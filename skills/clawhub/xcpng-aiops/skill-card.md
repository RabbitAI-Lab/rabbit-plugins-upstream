## Description:

XCP-ng AIops helps agents triage and operate XCP-ng virtualization fleets through Xen Orchestra, including fleet health, VM, host, pool, storage, snapshot, backup, task, RCA, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect XCP-ng fleets managed by Xen Orchestra, diagnose VM, storage, backup, pool, and HA issues, and prepare or execute governed operational changes such as VM lifecycle actions, migration, snapshots, and SR rescans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an agent real VM and snapshot control through the connected Xen Orchestra account, and the security evidence notes there is no in-tool read-only mode or approval gate.

Mitigation: Install it only for trusted Xen Orchestra environments and prefer a dedicated least-privilege or read-only XO user before allowing write-capable workflows.

Risk: Secrets and local operational history are concentrated under ~/.xcpng-aiops, including encrypted credentials, audit data, and undo history.

Mitigation: Protect ~/.xcpng-aiops, avoid putting XCPNG_AIOPS_MASTER_PASSWORD in shared plaintext MCP configuration when possible, and restrict filesystem access to the operator account.

Risk: High-impact actions such as snapshot delete, snapshot revert, VM stop, reboot, and migration can affect live workloads.

Mitigation: Use dry-run previews, verify object UUIDs from list tools, keep destructive operations behind operator approval, and rely on XO account permissions as the primary enforcement point.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/xcpng-aiops)
- [Project homepage](https://github.com/AIops-tools/XCPng-AIops)
- [Setup & security guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands, MCP tool recommendations, and JSON-shaped operational results from the underlying tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, RCA findings, truncation notices, audit/undo identifiers, and setup configuration guidance.]

## Skill Version(s):

0.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
