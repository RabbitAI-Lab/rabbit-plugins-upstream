## Description: <br>
macOS-native web dashboard for monitoring and controlling your OpenClaw agent, including live chat, cron management, task workshop, scout engine, cost tracking, and related controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jzineldin](https://clawhub.ai/user/jzineldin) <br>

### License/Terms of Use: <br>
BSL 1.1 (converts to MIT 2030) <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to install and operate a local Mission Control dashboard for monitoring sessions, managing scheduled jobs, reviewing costs, and configuring agent settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to run an unpinned external web application and install npm dependencies. <br>
Mitigation: Review the linked project and dependency tree before installation, and pin the repository to a known commit before running or updating it. <br>
Risk: The dashboard uses local OpenClaw gateway access and a gateway token with broad agent-control impact. <br>
Mitigation: Keep the dashboard bound to localhost, avoid network exposure without strong authentication, and handle the gateway token as a sensitive credential. <br>
Risk: The optional systemd setup can make the dashboard persistently available on the host. <br>
Mitigation: Inspect and edit the service file paths and permissions before enabling the service. <br>


## Reference(s): <br>
- [Mission Control ClawHub page](https://clawhub.ai/jzineldin/skills/openclaw-mission-control) <br>
- [Mission Control GitHub project](https://github.com/Jzineldin/mission-control) <br>
- [Brave Search API](https://brave.com/search/api/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces installation and operational guidance for a local OpenClaw dashboard; the skill itself does not generate application source files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
