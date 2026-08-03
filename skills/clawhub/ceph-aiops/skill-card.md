## Description: <br>
ceph-aiops helps agents diagnose and operate Ceph clusters through the ceph-mgr Dashboard REST API, including health root-cause analysis, storage inspection, governed writes, and undo-aware maintenance guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and storage operators use this skill to triage Ceph HEALTH_WARN/ERR states, inspect OSD, PG, pool, RBD, CephFS, and RGW status, and plan or execute governed maintenance through CLI and MCP workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes destructive Ceph storage-cluster write actions such as pool_delete, osd_purge, and RBD deletion. <br>
Mitigation: Start with a read-only ceph-mgr Dashboard account, verify audit logging, and grant write credentials only for deliberate maintenance sessions where those destructive calls are acceptable. <br>
Risk: Security evidence reports inconsistent governance and approval claims around write operations. <br>
Mitigation: Treat Ceph Dashboard roles and the calling agent's policy as the authorization boundary; use dry runs, audit review, and explicit maintenance approvals before high-risk writes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/ceph-aiops) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>
- [Project homepage from metadata](https://github.com/AIops-tools/Ceph-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Ceph operational findings, suggested actions, dry-run guidance, and write-risk notes.] <br>

## Skill Version(s): <br>
0.9.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
