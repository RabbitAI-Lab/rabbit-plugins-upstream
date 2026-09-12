## Description:

aigate helps agents operate a self-hosted OpenAI-compatible AI gateway that routes model calls and optional tools through a single bearer-protected endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to bring up and work with aigate, a Docker Compose stack that aggregates model providers, local inference, MCP tools, browser automation, code execution, storage, search, messaging, and media services behind one endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single master bearer token can grant access to high-impact capabilities including code execution, browser automation, messaging, and storage.

Mitigation: Set separate per-service tokens where possible and give AIGATE_TOKEN only to fully trusted clients for explicitly requested actions.

Risk: Exposing the gateway directly can make a broad local automation stack reachable from untrusted networks.

Mitigation: Run on a trusted, isolated host and avoid exposing port 4000 directly; use a protected tunnel or authenticating gateway when remote access is needed.

Risk: Local configuration can contain provider keys, mailbox credentials, Telegram session data, and other plaintext secrets.

Mitigation: Protect .env and service configuration files, keep them out of source control, and review the pinned upstream repository revision before installation.

## Reference(s):

- [aigate ClawHub release](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate GitHub repository](https://github.com/psyb0t/aigate)
- [aigate setup](references/setup.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration notes, and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference docker, curl, environment variables, and bearer-token configuration for a local aigate deployment.]

## Skill Version(s):

5.1.0 (source: server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
