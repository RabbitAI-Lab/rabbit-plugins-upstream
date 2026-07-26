## Description: <br>
Deploy an HTTP(S) proxy that exposes OpenClaw agent capability as a REST API over a network IP, with API key authentication, optional HTTPS, skill exposure controls, prompt-injection hardening, and per-request session isolation through OpenClaw hooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to expose an OpenClaw agent as an internal HTTP(S) API so other services can trigger agent tasks and poll for results. It is intended for controlled network deployments where authentication, skill exposure, agent routing, and hook configuration are reviewed before use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes OpenClaw agent control over a network API. <br>
Mitigation: Install only when that exposure is intended; prefer binding to 127.0.0.1 behind a TLS reverse proxy or enabling HTTPS before cross-host use. <br>
Risk: A leaked API key or broad exposure settings could allow unwanted agent or skill access. <br>
Mitigation: Protect and rotate the API key, set expose_skills and allowed_agent_ids narrowly, and review deny_skills before deployment. <br>
Risk: Initialization and watchdog behavior can make persistent global OpenClaw configuration changes. <br>
Mitigation: Back up ~/.openclaw/openclaw.json, avoid OPENCLAW_CONFIG_SYNC_PATHS unless needed, and disable the watchdog if automatic restart or hook-config repair is not desired. <br>


## Reference(s): <br>
- [Agent Easy Http on ClawHub](https://clawhub.ai/songhonglei/skills/agent-easy-http) <br>
- [README](README.md) <br>
- [Skill Instructions](SKILL.md) <br>
- [Deployment Guide](references/deployment.md) <br>
- [TLS and Authentication Standard](references/tls-auth-standard.md) <br>
- [Architecture Design Reference](references/design.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration fields, and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The deployed service returns JSON run metadata and text agent transcripts through HTTP endpoints.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
