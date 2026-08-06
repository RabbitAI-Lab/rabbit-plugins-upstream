## Description:

aigate helps an agent guide setup and use of a self-hosted OpenAI-compatible AI gateway that aggregates model routing, MCP tools, browser automation, code execution, media generation, storage, search, messaging, forecasting, and a web UI behind one bearer-protected endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want a one-command, self-hosted AI platform that exposes many model providers and tools through a single OpenAI-compatible endpoint. It is best suited for trusted, single-operator deployments where the user understands the authority granted by the gateway token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single AIGATE_TOKEN can authorize broad capabilities including model access, code execution, browser automation, messaging, and storage.

Mitigation: Give the token only to fully trusted agents for explicit tasks, and split per-service tokens before granting narrower access.

Risk: Exposing the gateway directly can make high-impact tools and credentials reachable outside the trusted host.

Mitigation: Do not publish port 4000 directly; use a protected tunnel, private network, or authenticating reverse proxy.

Risk: Environment and service configuration files can contain plaintext provider keys, mailbox credentials, sessions, and service tokens.

Mitigation: Keep .env and service config files private, source secrets from the environment, and avoid committing tokens or generated credentials.

## Reference(s):

- [aigate setup](references/setup.md)
- [aigate GitHub repository](https://github.com/psyb0t/aigate)
- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, endpoint examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may reference Docker Compose, curl requests, environment variables, local gateway routes, and security precautions.]

## Skill Version(s):

3.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
