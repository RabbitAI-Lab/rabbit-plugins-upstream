## Description:

aigate helps agents operate a self-hosted OpenAI-compatible AI gateway that aggregates inference, tool use, browser automation, media generation, storage, messaging, code execution, search, and fallback routing behind one endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when they want agent guidance for bringing up and using a self-hosted OpenAI-compatible gateway that combines many model providers, local services, and tools behind one endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single AIGATE_TOKEN can grant broad access to code execution, browser automation, messaging, storage, and model-provider credentials when services are enabled.

Mitigation: Give the token only to fully trusted agents for specific requested actions, and override per-service tokens so each enabled service has narrower credentials.

Risk: The gateway can expose a high-trust local AI stack through port 4000.

Mitigation: Do not expose port 4000 directly to the internet; use a trusted tunnel, private network, or authenticating reverse proxy.

Risk: Setup depends on upstream project code and make targets that should be reviewed before execution.

Mitigation: Pin and review the upstream repository before running setup commands or enabling optional services.

Risk: Environment, mailbox, and Telethon configuration can contain plaintext secrets.

Mitigation: Keep .env and service configuration files out of source control and restrict local filesystem access to them.

## Reference(s):

- [aigate setup](references/setup.md)
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/aigate)
- [Project homepage](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint paths, environment variable names, Docker Compose commands, and operational safety guidance.]

## Skill Version(s):

3.24.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
