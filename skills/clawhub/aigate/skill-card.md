## Description:

aigate helps agents and developers operate a Docker Compose self-hosted OpenAI-compatible gateway that aggregates model routing, MCP tools, browser automation, media services, code execution, storage, search, messaging, forecasting, and a web UI behind one bearer-protected endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they want one self-hosted endpoint that can route OpenAI-compatible model calls across local and cloud providers while exposing optional tools for browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single default bearer token can grant broad access to code execution, browser control, messaging, storage, and external accounts.

Mitigation: Give tokens only to trusted agents for explicit tasks and override per-service tokens before granting access.

Risk: Exposing the gateway port directly can make high-capability services reachable outside the trusted environment.

Mitigation: Keep port 4000 off the public internet unless it is protected by a real authentication gateway or private tunnel.

Risk: Local configuration can contain provider keys, mailbox credentials, Telethon sessions, and storage secrets.

Mitigation: Protect and rotate .env, mailbox, Telethon, provider, and storage credentials.

Risk: Optional services expand the blast radius when enabled together.

Mitigation: Enable only the services needed for the current deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate homepage](https://github.com/psyb0t/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Docker Compose commands, environment variables, endpoint examples, and security guidance.]

## Skill Version(s):

5.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
