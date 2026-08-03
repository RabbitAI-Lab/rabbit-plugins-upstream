## Description: <br>
network-aiops helps agents inspect, diagnose, back up, diff, and change NAPALM-supported network devices, with optional NetBox lookups and governance controls for audit, undo, and risk-tiered operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Network engineers and operations teams use this skill to collect live device state, diagnose interface or BGP issues, compare candidate configs, back up configs, and perform reviewed merge, replace, rollback, or undo workflows on supported Cisco, Arista, and Juniper devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact network device write actions, including merge, replace, rollback, confirm, and undo workflows. <br>
Mitigation: Install in a controlled network-operations environment, begin with read-only device and NetBox credentials, and require human review of diffs before any write or confirmation action. <br>
Risk: Network configurations and backups can contain sensitive values even when masking is applied. <br>
Mitigation: Protect ~/.network-aiops with strict permissions, avoid include_secrets=True in agent transcripts, and write raw backups only to operator-chosen files. <br>
Risk: Driver support and rollback safety vary by network platform, and some devices may not support a commit-confirm timer. <br>
Mitigation: Check tool warnings and unsupported-driver errors, verify reachability from a new session before confirming changes, and arrange out-of-band access before lockout-capable changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/network-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Network-AIops) <br>
- [network-aiops Capabilities](references/capabilities.md) <br>
- [network-aiops Setup Guide](references/setup-guide.md) <br>
- [network-aiops CLI Reference](references/cli-reference.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, diffs, and structured tool-result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include masked network configuration excerpts, diffs, diagnostics, and risk or undo notes; raw secrets should be kept out of agent transcripts.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
