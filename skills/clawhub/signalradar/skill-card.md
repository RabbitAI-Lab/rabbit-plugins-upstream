## Description: <br>
SignalRadar monitors Polymarket prediction markets for probability changes and sends alerts when thresholds are crossed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vahnxu](https://clawhub.ai/user/vahnxu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use SignalRadar to discover, add, monitor, and review Polymarket markets, manage alert thresholds and schedules, and route notifications through webhook, file, or OpenClaw delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes local SignalRadar state, including watchlists, baselines, event logs, and routing details. <br>
Mitigation: Review the configured data directory before installation and manage settings through the skill CLI rather than editing state files directly. <br>
Risk: Adding markets may create recurring cron or OpenClaw scheduled monitoring jobs. <br>
Mitigation: Check schedule status after setup and use the schedule disable command to stop background runs when monitoring is no longer wanted. <br>
Risk: Webhook alerts can reveal which prediction markets a user monitors. <br>
Mitigation: Configure only trusted webhook URLs and review delivery settings before enabling background push. <br>
Risk: The skill contacts Polymarket services to fetch market data. <br>
Mitigation: Install only in environments where external access to Polymarket is acceptable and expected. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vahnxu/skills/signalradar) <br>
- [Configuration Reference](references/config.md) <br>
- [Operations Reference](references/operations.md) <br>
- [Runtime Protocol Reference](references/protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local SignalRadar state, monitor schedules, baselines, and delivery metadata through the skill CLI.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
