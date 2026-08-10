## Description:

ceph-aiops helps agents diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, covering health RCA, OSD/PG/pool/RBD/CephFS/RGW inspection, capacity forecasting, and governed write operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage SREs, and Ceph operators use this skill to investigate cluster health and capacity issues, then perform audited maintenance tasks through a configured Ceph Dashboard account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose destructive Ceph storage operations when connected with an account that has write privileges.

Mitigation: Start with a read-only Ceph Dashboard account for observation or triage, and grant write privileges only when the operator accepts the resulting operational risk.

Risk: The evidence reports no enforceable built-in approval or read-only control for destructive operations.

Mitigation: Use Ceph Dashboard RBAC as the primary control and require human review of high-risk operations before allowing an agent to invoke them.

Risk: The artifact says multi-node rebalance behavior and write operations still need live verification.

Mitigation: Validate workflows in MicroCeph or staging, run doctor and dry-run checks first, and avoid first use against a production-admin account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops)
- [ceph-aiops homepage](https://github.com/AIops-tools/Ceph-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured tool-use recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Ceph Dashboard observations, risk-tiered operation guidance, dry-run steps, and audit or undo instructions.]

## Skill Version(s):

0.10.0 (source: evidence.release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
