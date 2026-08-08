## Description:

aigate is a self-hosted AI platform that exposes inference, tool use, browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI through one OpenAI-compatible endpoint with bearer-token access and fallback routing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate to deploy a self-hosted OpenAI-compatible gateway that aggregates model providers and optional tools behind one endpoint. Agents and clients can use it for routing, MCP tools, media services, browser automation, code execution, storage, search, messaging, forecasting, and a web UI without wiring each service separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AIGATE_TOKEN can grant broad access to enabled model providers, code execution, browser automation, messaging, storage, and other services.

Mitigation: Treat the token as an administrator secret, give it only to trusted agents for explicit tasks, and split per-service tokens where possible.

Risk: Exposing the gateway directly to the public internet can create a high-blast-radius entry point.

Mitigation: Do not expose port 4000 directly; use Cloudflare Tunnel, Tailscale, or an authenticating reverse proxy.

Risk: Secret-bearing configuration files can contain plaintext service credentials.

Mitigation: Keep .env, mailbox, Telethon, and similar config files out of repositories and source secrets from protected local configuration.

Risk: Optional services such as code execution, browser automation, email, and Telegram can act with significant authority when enabled.

Mitigation: Enable only the services needed for the deployment and review enabled service flags before granting agent access.

## Reference(s):

- [aigate setup guide](artifact/references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [Project homepage](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline shell commands and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Docker and curl; primary environment variable is AIGATE_TOKEN.]

## Skill Version(s):

3.19.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
