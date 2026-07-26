## Description: <br>
Monitors the OpenClaw gateway every 3 hours, restarts it when unresponsive, diagnoses startup failures, and rotates logs with 7-day retention. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shirley6692026](https://clawhub.ai/user/shirley6692026) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to keep an OpenClaw gateway available by installing an unattended watchdog that checks health, restarts the gateway when needed, and records operational logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs an unattended recurring job that can restart local OpenClaw gateway services. <br>
Mitigation: Install only when automatic restarts are intended, and review the cron entry and gateway_monitor.sh before use. <br>
Risk: The monitor may terminate matching openclaw-gateway processes while diagnosing startup issues. <br>
Mitigation: Avoid shared or production machines unless broad process termination for the gateway is acceptable. <br>
Risk: Removing the artifact files does not necessarily remove the scheduled monitor. <br>
Mitigation: Be prepared to remove the crontab line manually if the watchdog is no longer wanted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/shirley6692026/skills/gateway-monitor-auto-restart) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and operation guidance for a cron-based OpenClaw gateway monitor.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
