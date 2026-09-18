## Description:

TrueNAS AIops lets agents inspect and administer TrueNAS SCALE storage through CLI and MCP tools for health checks, diagnostics, pools, datasets, snapshots, disks, alerts, services, replication, and cloud-sync tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Storage administrators, operators, and agent developers use this skill to triage and perform governed operations on TrueNAS SCALE appliances. It supports read-only diagnostics as well as audited write actions such as dataset creation, snapshot operations, pool scrub starts, service restarts, and undo application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact TrueNAS storage writes and does not provide its own read-only mode or approval gate.

Mitigation: Install only for intended TrueNAS administration, use a least-privilege or read-only TrueNAS API key unless writes are required, and require explicit human oversight for write actions.

Risk: Snapshot deletion and service restart can disrupt storage availability or remove recovery points.

Mitigation: Use dry-run previews, confirm current dataset, snapshot, pool, and service identifiers from live tool output, and treat these actions as requiring explicit operator approval.

Risk: Long-lived exported master passwords or legacy plaintext environment keys can weaken credential handling.

Mitigation: Prefer the encrypted secret store, avoid shared-system exported master passwords, and migrate away from legacy plaintext environment keys.

## Reference(s):

- [TrueNAS AIops ClawHub page](https://clawhub.ai/zw008/skills/truenas-aiops)
- [TrueNAS AIops homepage](https://github.com/AIops-tools/TrueNAS-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured tool-call results with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include TrueNAS API-derived status values, diagnostics, audit context, dry-run previews, and operator guidance.]

## Skill Version(s):

0.11.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
