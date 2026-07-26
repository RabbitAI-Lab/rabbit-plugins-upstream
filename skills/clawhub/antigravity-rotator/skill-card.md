## Description: <br>
Manages Google Antigravity account rotation for OpenClaw by monitoring quotas, switching accounts and models, hot-updating sessions, and providing a local dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chocomintx](https://clawhub.ai/user/chocomintx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users with multiple Antigravity accounts use this skill to automate quota-aware account rotation, update active sessions without restarting, and monitor rotation status from a local dashboard. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes account and session controls through an unauthenticated local dashboard. <br>
Mitigation: Keep the dashboard bound to localhost and do not expose port 18090 to a LAN or the internet unless authentication is added first. <br>
Risk: The skill handles OpenClaw auth profiles, OAuth tokens, and local configuration that may contain sensitive secrets. <br>
Mitigation: Treat config.json and auth profile files as secrets, back up profiles before use, and prefer dedicated low-risk accounts. <br>
Risk: Automated cron rotation can change live account or model state without interactive review. <br>
Mitigation: Review the cron entry before enabling it and monitor rotation logs after deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chocomintx/skills/antigravity-rotator) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local setup, dashboard, cron, and rotation guidance for OpenClaw account management.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release metadata; package.json reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
