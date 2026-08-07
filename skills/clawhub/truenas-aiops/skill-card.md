## Description: <br>
TrueNAS AIops helps agents inspect and administer TrueNAS SCALE storage, including health diagnostics, ZFS pools, datasets, snapshots, disks, alerts, services, replication, and cloud-sync tasks with audit and risk-tiered governance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, storage administrators, and operations teams use this skill to triage TrueNAS SCALE appliances, collect root-cause analysis, inspect storage resources, and perform governed operational actions such as scrubs, dataset creation, snapshots, and service restarts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can invoke high-impact TrueNAS storage write actions, and the security evidence reports no in-tool read-only mode or approval gate. <br>
Mitigation: Install only for TrueNAS systems the agent is allowed to administer; use a least-privilege or read-only TrueNAS API key by default and grant write permissions only for approved workflows. <br>
Risk: Snapshot deletion is irreversible and service restarts can disrupt access to the appliance. <br>
Mitigation: Prefer dry-run previews and explicit user workflow controls before write actions; rely on account permissions for enforcement and review the local audit trail after execution. <br>
Risk: TrueNAS API credentials and the TRUENAS_AIOPS_MASTER_PASSWORD unlock sensitive appliance access. <br>
Mitigation: Treat the master password and any legacy environment API keys as secrets, migrate plaintext credentials into the encrypted store, and clean up migrated plaintext files after validation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/truenas-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/TrueNAS-AIops) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include TrueNAS operational findings, command recommendations, dry-run guidance, and configuration or credential setup steps.] <br>

## Skill Version(s): <br>
0.9.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
