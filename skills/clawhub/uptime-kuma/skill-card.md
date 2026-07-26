## Description: <br>
Interact with Uptime Kuma monitoring server. Use for checking monitor status, adding/removing monitors, pausing/resuming checks, viewing heartbeat history. Triggers on mentions of Uptime Kuma, server monitoring, uptime checks, or service health monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[msarheed](https://clawhub.ai/user/msarheed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operations teams use this skill to inspect and manage Uptime Kuma monitors from an agent workflow, including status checks, monitor creation, pause/resume actions, deletion, heartbeat history, and notification listing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored Uptime Kuma credentials can be used to change monitoring configuration. <br>
Mitigation: Use a least-privilege Uptime Kuma account and scope access to the monitors the agent is expected to manage. <br>
Risk: Delete and pause actions can disrupt monitoring visibility. <br>
Mitigation: Require human confirmation before delete, pause, or bulk maintenance actions, and verify monitor IDs before execution. <br>
Risk: The skill depends on an external Python package for Uptime Kuma API access. <br>
Mitigation: Review and pin the external Python dependency before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/msarheed/skills/uptime-kuma) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled CLI can emit JSON for list, status, heartbeats, and notifications.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
