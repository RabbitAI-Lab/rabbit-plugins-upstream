## Description:

aigate helps agents operate a self-hosted OpenAI-compatible AI gateway that aggregates model routing, MCP tools, browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI behind one Docker Compose deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate when they want a self-hosted OpenAI-compatible endpoint that can route across local and cloud models while exposing optional tools such as browser automation, code execution, object storage, search, messaging, and media generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single bearer token can grant access to high-impact capabilities including code execution, browser control, messaging, storage, and provider credentials.

Mitigation: Treat AIGATE_TOKEN as highly sensitive, split per-service tokens before giving agents access, and provide tokens only for the specific task requested.

Risk: Exposing the gateway directly can make the full stack reachable through the public network.

Mitigation: Do not expose port 4000 directly; keep it local or place it behind a trusted access layer such as Cloudflare Tunnel, Tailscale, or an authenticating reverse proxy.

Risk: Enabled optional services can expand the operational blast radius.

Mitigation: Enable only the services needed for the deployment and protect .env, mailbox, Telethon, and provider credential files as secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [Setup reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint paths, environment variable names, deployment steps, and security guidance for operating the gateway.]

## Skill Version(s):

5.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
