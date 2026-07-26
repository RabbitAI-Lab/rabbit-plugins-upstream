## Description: <br>
Monitoring Aiops helps agents operate SolarWinds Orion, Paessler PRTG, and Zabbix monitoring environments with NOC overviews, read-only queries, alert triage, health checks, maintenance actions, and audited guarded writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and NOC teams use this skill to inspect monitoring state, triage alerts, run SolarWinds SWQL checks, and coordinate controlled maintenance actions across SolarWinds Orion, PRTG, and Zabbix. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured credentials can make real production monitoring changes without a built-in read-only or approval gate. <br>
Mitigation: Install with least-privilege monitoring accounts, preferably read-only by default, and grant write permissions only to operators who intentionally need suppression, maintenance, unmanage, remove, or delete-maintenance actions. <br>
Risk: Audit annotations and risk-tier labels record activity but do not authorize or block actions. <br>
Mitigation: Treat audit records as accountability evidence and enforce authorization through monitoring-platform permissions and agent operating policy. <br>


## Reference(s): <br>
- [Monitoring AIops homepage](https://github.com/AIops-tools/Monitoring-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured monitoring summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include monitoring observations, tool-call guidance, setup steps, and operational cautions.] <br>

## Skill Version(s): <br>
0.6.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
