## Description:

Self-hosted AI platform that lets an agent use a single OpenAI-compatible endpoint for model routing, MCP tool use, browser automation, media generation, transcription, storage, code execution, search, messaging, forecasting, job queueing, and a web UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when they want an agent to help operate a self-hosted AI gateway that aggregates model providers and tool services behind one endpoint. It is suited for trusted single-operator or controlled deployments where broad endpoint capability is intentional.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A single bearer token can provide broad access to code execution, browsing, messaging, storage, and provider-backed model services.

Mitigation: Split per-service tokens before giving credentials to an agent, enable only the required services, and provide credentials only for the specific user-approved task.

Risk: Exposing the gateway directly can make a high-capability endpoint reachable outside the trusted host.

Mitigation: Run on an isolated trusted host or VM and avoid direct public exposure of port 4000; use a protected tunnel or authenticating gateway when remote access is required.

Risk: Local environment and service configuration files can contain plaintext secrets.

Mitigation: Protect .env, mailbox, and Telethon files, keep them out of source control, and review file permissions before deployment.

## Reference(s):

- [aigate ClawHub release](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup](references/setup.md)
- [Publisher profile](https://clawhub.ai/user/psyb0t)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration steps, and endpoint examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local environment variables, Docker Compose services, HTTP endpoints, and bearer tokens supplied by the operator.]

## Skill Version(s):

5.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
