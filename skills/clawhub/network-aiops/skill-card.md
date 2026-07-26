## Description: <br>
Network Aiops helps agents inspect and operate NAPALM-supported network devices, run read-only diagnostics, back up and diff configurations, and perform governed configuration changes across Cisco, Arista, Juniper, and optional NetBox environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network operators, SREs, and infrastructure engineers use this skill to query live network state, diagnose interface and BGP problems, compare proposed configuration changes, and execute audited device configuration workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform production-impacting network configuration writes and does not provide an internal read-only mode or approval gate. <br>
Mitigation: Use read-only device and NetBox credentials for routine work, grant write-capable credentials only when intended, and require an external approval process before MCP write tools are used. <br>
Risk: Configuration backups or diffs may contain sensitive network secrets, especially if raw output is requested. <br>
Mitigation: Avoid include_secrets=True in agent transcripts, prefer writing raw configs to operator-controlled files when needed, and keep ~/.network-aiops protected with chmod 700. <br>
Risk: Some device drivers may be unable to arm commit-confirm revert timers, leaving configuration changes permanent on commit. <br>
Mitigation: Check the returned commit warning and safetyNet fields, arrange out-of-band access for lockout-capable changes, and verify reachability from a new session before confirming changes. <br>


## Reference(s): <br>
- [Network-AIops homepage](https://github.com/AIops-tools/Network-AIops) <br>
- [network-aiops Capabilities](references/capabilities.md) <br>
- [network-aiops Setup Guide](references/setup-guide.md) <br>
- [network-aiops CLI Reference](references/cli-reference.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured tool-use recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to invoke CLI or MCP operations that return live device data, diffs, backups, audit records, and configuration-change results.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
