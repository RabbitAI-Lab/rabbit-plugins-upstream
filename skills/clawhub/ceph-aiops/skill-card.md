## Description:

Ceph AIops helps an agent diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, including health RCA, OSD/PG/pool/RBD/CephFS/RGW inspection, capacity forecasting, governed writes, and undo-aware workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, storage administrators, and operations engineers use this skill to investigate Ceph health warnings, inspect cluster resources, forecast capacity, and perform governed maintenance actions through Ceph Dashboard APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Ceph storage operations, including pool, RBD, and OSD deletes.

Mitigation: Start with a read-only Ceph Dashboard account, use separate credentials for destructive work, require dry-run review for high-risk actions, and treat delete operations as irreversible.

Risk: Broad Ceph Dashboard credentials could allow an agent to administer production cluster resources.

Mitigation: Grant the minimum Dashboard role needed for the task, verify account permissions before connecting the skill, and use write-enabled credentials only for planned maintenance.

Risk: Long-lived master-password environment variables can expose access to the encrypted credential store.

Mitigation: Avoid leaving CEPH_AIOPS_MASTER_PASSWORD set longer than needed and prefer interactive unlocks or tightly scoped non-interactive sessions.

Risk: Write operations and multi-node rebalance behavior have limited live-cluster validation evidence.

Mitigation: Run ceph-aiops doctor and validate maintenance workflows in a lab or staged cluster before relying on write operations in production.

## Reference(s):

- [Ceph AIops source homepage](https://github.com/AIops-tools/Ceph-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops)
- [ceph-aiops capabilities](references/capabilities.md)
- [ceph-aiops CLI reference](references/cli-reference.md)
- [ceph-aiops setup & security guide](references/setup-guide.md)
- [Agent guardrails - running ceph-aiops with a smaller / local model](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and structured tool-call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Ceph health explanations, operational recommendations, dry-run/write guidance, audit and undo references, and configuration steps.]

## Skill Version(s):

0.11.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
