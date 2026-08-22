## Description:

aigate helps agents guide users through running a self-hosted OpenAI-compatible AI gateway that aggregates model routing, MCP tools, browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI behind one Docker Compose endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate to deploy and operate a local AI gateway that presents one OpenAI-compatible endpoint for multiple providers and opt-in tools. It is most useful when a trusted operator wants Docker-based model routing, tool access, and service orchestration without wiring each backend separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token can unlock code execution, browser automation, messaging, storage, and provider credentials.

Mitigation: Share AIGATE_TOKEN only with trusted agents for explicit user-requested actions, and split per-service tokens before enabling high-risk tools.

Risk: Exposing port 4000 directly can make a broad local AI gateway reachable by unintended users.

Mitigation: Keep port 4000 off the public internet; use Cloudflare Tunnel, Tailscale, or an authenticating gateway when remote access is needed.

Risk: Enabled services may hold sensitive provider, mailbox, Telegram, storage, and database credentials.

Mitigation: Guard .env and service configuration files as secrets, avoid committing tokens, and enable only the services required for the task.

Risk: Agentic code execution and browser automation create a high blast radius on trusted hosts.

Mitigation: Run aigate only on trusted infrastructure, review requested actions before execution, and avoid multi-tenant or untrusted exposure without additional authorization controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [Publisher profile](https://clawhub.ai/user/psyb0t)
- [aigate setup reference](references/setup.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown with inline shell commands, configuration notes, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker Compose operations, environment variable guidance, endpoint routes, and token handling instructions.]

## Skill Version(s):

3.21.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
