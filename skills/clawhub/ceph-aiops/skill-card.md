## Description:

ceph-aiops helps agents diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, including HEALTH_WARN and HEALTH_ERR root-cause analysis, OSD, PG, pool, RBD, CephFS, and RGW inspection, capacity forecasting, and governed write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Storage operators, SREs, and infrastructure engineers use this skill to inspect Ceph cluster health, diagnose active warnings and errors, and carry out governed maintenance actions such as OSD drains, pool changes, RBD operations, recovery throttling, and capacity checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP tools can perform irreversible Ceph cluster changes without an enforced confirmation or read-only gate.

Mitigation: Use a dedicated read-only Ceph Dashboard account by default, enable write privileges only for controlled sessions, and require explicit operator approval before destructive MCP calls.

Risk: Destructive operations such as pool deletion, RBD deletion, snapshot deletion, and pool size changes can cause data loss or cluster-wide data movement.

Mitigation: Run dry-run previews first, review the planned change with the operator, and prefer reversible actions with undo records before irreversible changes.

Risk: Write operations and multi-node rebalance behavior have not been fully verified against a live multi-node cluster in the provided artifact evidence.

Mitigation: Validate behavior in a lab Ceph environment before production use and start with low-risk read-only diagnostics such as doctor, overview, and health detail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops)
- [Project homepage](https://github.com/AIops-tools/Ceph-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured Ceph operation summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk-tier labels, dry-run recommendations, undo guidance, and references to Ceph Dashboard API-derived results.]

## Skill Version(s):

0.11.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
