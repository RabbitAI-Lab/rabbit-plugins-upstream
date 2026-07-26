## Description: <br>
Read-only log search and aggregation for VMware Aria Operations for Logs (vRealize Log Insight), enabling agents to investigate centralized ESXi, vCenter, and VM logs without write actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, SREs, and VMware administrators use this skill to query centralized Log Insight data, inspect raw log lines behind incidents, detect log-volume spikes, and retrieve read-only alert history for troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queried appliance logs may contain sensitive production data. <br>
Mitigation: Use a read-only Log Insight service account, scope queries to the incident window, and avoid exposing raw log output beyond the authorized troubleshooting context. <br>
Risk: Local credential files can expose appliance credentials if filesystem permissions or secret handling are weak. <br>
Mitigation: Keep ~/.vmware-log-insight/.env chmod 600 or inject credentials from a secret manager at process start. <br>
Risk: Disabling TLS verification can expose credentials or log data outside controlled lab environments. <br>
Mitigation: Leave TLS verification enabled by default and disable it only for explicitly controlled self-signed lab appliances. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/vmware-log-insight) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Log Insight queries may return truncated result envelopes and completion flags that agents should surface to users.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
