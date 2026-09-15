## Description:

ceph-aiops helps agents diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, including HEALTH_WARN/ERR root-cause analysis, read-only inspection, governed write operations, and undo-aware maintenance workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and storage operators use this skill to inspect Ceph health, capacity, OSDs, placement groups, pools, RBD, CephFS, RGW, monitors, managers, and slow operations. For supervised maintenance, it can propose and execute governed Ceph changes such as OSD drain or purge, pool changes, recovery throttling, and RBD actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable Ceph Dashboard credentials can allow destructive cluster actions such as OSD purge, pool deletion, replica changes, and RBD deletion.

Mitigation: Start with a dedicated read-only Dashboard account, expose write-capable credentials only during supervised maintenance, and use dry-run and double-confirmation workflows where available.

Risk: The skill relies on Ceph Dashboard account permissions rather than a skill-side approval gate.

Mitigation: Use Ceph Dashboard roles as the authorization boundary and configure the connected account with the minimum role needed for the session.

Risk: Secrets may be exposed if operators pass passwords directly on command lines or use broad environment scopes.

Mitigation: Use the encrypted secret store and interactive prompts when possible, avoid passing passwords with --value, and keep CEPH_AIOPS_MASTER_PASSWORD scoped to the active session.

Risk: Multi-node rebalance behavior and write operations have limited live-cluster verification in the artifact evidence.

Mitigation: Validate workflows in a non-production Ceph environment before enabling write-capable use against production clusters.

## Reference(s):

- [ceph-aiops project homepage](https://github.com/AIops-tools/Ceph-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and structured tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Ceph health explanations, operational recommendations, dry-run guidance, and audit or undo context from tool results.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
