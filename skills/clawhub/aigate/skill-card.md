## Description: <br>
Self-hosted Docker Compose AI gateway that exposes one OpenAI-compatible endpoint for model routing, MCP tools, browser automation, media generation, code execution, storage, search, messaging, and a web UI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use aigate to stand up a self-hosted AI gateway that aggregates model providers and optional tools behind one endpoint instead of wiring each service individually. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AIGATE_TOKEN can grant broad access to enabled services, including code execution, browser automation, messaging, storage, and provider credentials. <br>
Mitigation: Use strong unique tokens, split per-service tokens where possible, give tokens only to trusted agents for explicit tasks, and never commit populated .env or credential files. <br>
Risk: Exposing the gateway directly can make a high-power local AI stack reachable through a bearer token alone. <br>
Mitigation: Keep port 4000 off the public internet unless protected by a real access gateway, VPN, Cloudflare Tunnel, Tailscale, or authenticated reverse proxy. <br>
Risk: Optional email, Telegram, browser, and storage integrations can act on the user's behalf and may hold plaintext secrets. <br>
Mitigation: Enable only the services needed for the task and guard .env, mailbox, Telethon, and other credential configuration files. <br>


## Reference(s): <br>
- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate) <br>
- [aigate setup](references/setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires docker, curl, and an operator-provided AIGATE_TOKEN; optional services are enabled through environment flags.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
