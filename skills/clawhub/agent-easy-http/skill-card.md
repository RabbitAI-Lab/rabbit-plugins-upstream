## Description: <br>
Deploys an HTTP(S) REST proxy that exposes OpenClaw agent capability over a network endpoint with API key authentication, optional TLS, deny-list filtering, prompt-injection hardening, and per-request hook session isolation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform operators use this skill to run an OpenClaw agent behind an internal HTTP(S) API so trusted services can submit agent tasks and poll returned transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The service exposes a remotely callable agent control surface. <br>
Mitigation: Install only on trusted hosts and networks, keep the port reachable only by trusted callers, and restrict exposed skills and allowed agents. <br>
Risk: Default HTTP mode can transmit API keys, prompts, and results in cleartext. <br>
Mitigation: Bind to 127.0.0.1 for local use or place the service behind HTTPS or reverse-proxy TLS before cross-host or production access. <br>
Risk: API-key holders can trigger broad agent actions and read returned transcripts. <br>
Mitigation: Protect the API key like a password, avoid logging or sharing it, rotate it when exposed, and use skill deny lists and agent allow lists. <br>
Risk: Initialization and watchdog behavior can modify and restore global OpenClaw hook configuration. <br>
Mitigation: Review the OpenClaw configuration changes before enabling the service and disable the watchdog when manual configuration reverts must persist. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/agent-easy-http) <br>
- [Deployment Guide](references/deployment.md) <br>
- [Design Document](references/design.md) <br>
- [TLS and Authentication Standard](references/tls-auth-standard.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, and REST API request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can start and maintain a persistent HTTP(S) gateway that returns run identifiers and result transcripts through API endpoints.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and changelog, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
