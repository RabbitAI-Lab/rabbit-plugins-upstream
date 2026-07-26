## Description: <br>
TrueNAS AIops helps an agent inspect, diagnose, and perform governed operations on a TrueNAS SCALE appliance through CLI and MCP tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and storage administrators use this skill to triage TrueNAS SCALE health, inspect pools, datasets, snapshots, disks, alerts, services, replication, and run guarded write actions when appropriate. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent operational access to a TrueNAS appliance, including write-capable actions. <br>
Mitigation: Use a limited-permission TrueNAS API key and grant write permissions only when the operating context requires them. <br>
Risk: MCP write tools include high-impact actions such as snapshot deletion and service restart without a built-in approval gate. <br>
Mitigation: Treat snapshot_delete and service_restart as high-impact, use dry-run where available, and require external operator approval before invoking destructive actions. <br>
Risk: The artifact states that endpoint behavior is mock-validated only and not yet verified against a live appliance. <br>
Mitigation: Run truenas-aiops doctor and verify behavior in a non-production or limited-permission environment before relying on it for production operations. <br>
Risk: The master password environment variable can be exposed through shells, CI logs, or process handling. <br>
Mitigation: Handle TRUENAS_AIOPS_MASTER_PASSWORD as a secret, avoid echoing it, and prefer secret-management facilities for non-interactive use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/truenas-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/TrueNAS-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration notes, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide calls to CLI or MCP tools that return structured operational data from the configured TrueNAS appliance.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
