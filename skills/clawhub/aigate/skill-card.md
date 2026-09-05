## Description:

aigate helps agents operate a one-command, self-hosted OpenAI-compatible gateway that can route inference, tools, browser automation, media generation, code execution, storage, search, messaging, forecasting, and a web UI through a single endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use aigate when they want a self-hosted OpenAI-compatible endpoint that aggregates local and cloud models plus optional AI tools without wiring each service separately. It is intended for trusted deployments where the operator controls enabled services, tokens, and network exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single aigate token can provide broad access to code execution, browser automation, messaging, storage, and provider credentials.

Mitigation: Use strong unique tokens, split per-service tokens before granting agent access, and provide the master token only to fully trusted agents for explicit tasks.

Risk: Exposing the gateway publicly can widen access to high-authority services behind port 4000.

Mitigation: Do not publish port 4000 directly; use a protected tunnel, private network, or authenticating reverse proxy.

Risk: Enabled cloud providers, browser routes, email, or Telegram services may send sensitive data outside the local machine.

Mitigation: Keep risky services disabled unless needed, review enabled routes before use, and protect .env plus mailbox or Telegram session files.

## Reference(s):

- [aigate ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate GitHub repository](https://github.com/psyb0t/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint calls, Docker Compose operations, environment variable guidance, and security cautions for enabled aigate services.]

## Skill Version(s):

3.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
