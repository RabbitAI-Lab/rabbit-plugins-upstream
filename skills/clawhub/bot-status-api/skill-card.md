## Description: <br>
Bot Status API deploys a lightweight Node.js status service for OpenClaw bots that reports runtime health, service connectivity, cron jobs, skills, and system metrics as JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[suspect80](https://clawhub.ai/user/suspect80) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to deploy a local status API for OpenClaw agents, monitoring dashboards, health endpoints, or status pages. It helps aggregate bot vitals, configured service checks, cron status, Docker health, installed skills, and host metrics into a cached JSON endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The status API can expose detailed local runtime, service, skill, and system information. <br>
Mitigation: Install it only as a private monitoring service, keep it on localhost or behind strong authentication, and do not expose /status publicly. <br>
Risk: Configured command checks can execute shell commands during status collection. <br>
Mitigation: Use only administrator-controlled config, avoid command checks where possible, and run the service under a low-privilege account. <br>
Risk: The service weakens HTTPS verification by default for local integrations. <br>
Mitigation: Remove or narrow the global TLS verification bypass before production use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/suspect80/skills/bot-status-api) <br>
- [Publisher Profile](https://clawhub.ai/user/suspect80) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with JavaScript, JSON, shell, and systemd configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When deployed, the service exposes JSON status data from /status and a simple JSON health response from /health.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; package.json reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
