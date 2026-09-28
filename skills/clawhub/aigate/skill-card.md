## Description:

Guides developers in deploying and using a self-hosted, OpenAI-compatible gateway for model inference and optional AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy a self-hosted AI gateway and configure model routing and optional tools through a single endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared bearer token can grant code execution, browser actions, storage access, and messaging capabilities.

Mitigation: Enable only needed services, assign separate per-service tokens, and share the master token only with trusted agents for explicitly requested actions.

Risk: Exposing the gateway directly to the internet can put its powerful tools and credentials at risk.

Mitigation: Use a trusted, preferably dedicated host; do not publish port 4000 directly, and use a protected tunnel or authenticating gateway for remote access.

Risk: Gateway, email, and Telegram configuration files contain sensitive credentials.

Mitigation: Protect .env and mailbox/Telethon configuration files, and keep secrets out of committed scripts.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [Setup guide](references/setup.md)
- [Project homepage listed in skill documentation](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

6.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
