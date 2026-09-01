## Description:

aigate helps agents operate a self-hosted OpenAI-compatible AI gateway that bundles model routing, MCP tools, browser automation, media services, code execution, search, messaging, storage, and a web UI behind one authenticated endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate when they want one self-hosted OpenAI-compatible endpoint that aggregates model providers, local models, MCP-accessible tools, browser automation, media services, code execution, search, messaging, storage, and LibreChat. It is intended for trusted deployments where the operator controls the token, enabled services, secrets, and network exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The gateway exposes a broad set of capabilities through one bearer token, including code execution, browser automation, messaging, storage, and credential-backed services.

Mitigation: Give tokens only to trusted agents for explicit tasks, and set separate per-service tokens before delegating narrower access.

Risk: Public or multi-tenant exposure can turn the endpoint into a high-blast-radius control plane.

Mitigation: Keep the service local or behind a real authenticated tunnel or reverse proxy; do not expose port 4000 directly to the public internet.

Risk: Environment files, mailbox configuration, and Telethon configuration may contain sensitive secrets.

Mitigation: Protect .env, mailbox configuration, and Telethon configuration files as secrets and avoid committing tokens or credentials.

Risk: Optional browser, email, Telegram, and code-execution services can act on the user's behalf or modify host-visible state.

Mitigation: Enable only the services needed for the current deployment and review those actions before granting agent access.

## Reference(s):

- [aigate ClawHub release](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup](references/setup.md)
- [aigate project homepage](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration notes, endpoint examples, and operational safety guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires docker and curl; uses AIGATE_TOKEN as the primary environment variable.]

## Skill Version(s):

3.22.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
