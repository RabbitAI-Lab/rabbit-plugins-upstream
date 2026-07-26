## Description: <br>
Quick diagnosis and repair for Discord bot, Gateway, OAuth token, and legacy config issues. Checks connectivity, token expiration, and cleans up old Clawdis artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jhillock](https://clawhub.ai/user/jhillock) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to diagnose Discord bot, Clawdbot gateway, OAuth token, and legacy Clawdis configuration issues, and to get repair guidance or controlled auto-fix commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-fix mode can change local system state, including gateway process state, npm packages, LaunchAgents, and legacy Clawdis configuration. <br>
Mitigation: Run diagnostics first, review each proposed --fix action, and keep backups before allowing changes to LaunchAgents or configuration directories. <br>
Risk: OAuth or session repair guidance may require local re-authentication and can affect Discord or Clawdbot availability during restart. <br>
Mitigation: Perform repairs in a maintenance window when service interruption is acceptable, then rerun health checks to confirm Discord and gateway connectivity. <br>


## Reference(s): <br>
- [Discord Doctor on ClawHub](https://clawhub.ai/jhillock/skills/discord-doctor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration guidance] <br>
**Output Format:** [Markdown with diagnostic summaries and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed --fix actions that start or restart services, install npm packages, remove legacy launchd services, or back up legacy configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
