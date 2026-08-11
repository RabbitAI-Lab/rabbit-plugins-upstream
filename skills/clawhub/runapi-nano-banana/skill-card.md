## Description:

Generate and edit images with Nano Banana through RunAPI, using the RunAPI CLI for one-off tasks and SDKs for application or backend integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to create, edit, or transform images with RunAPI's Nano Banana model. It guides agents to choose the CLI for one-off work and SDKs for production application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses RunAPI as a third-party image service and may rely on a RUNAPI_API_KEY or saved CLI login.

Mitigation: Treat RunAPI credentials as service credentials, prefer environment-based authentication for agents, and avoid exposing tokens in logs or generated files.

Risk: RunAPI-generated file URLs are temporary and should not be treated as long-term storage.

Mitigation: Download generated assets and move them to durable user-controlled storage within 7 days.

Risk: Using the CLI as a production runtime integration layer can create brittle application behavior.

Mitigation: Use RunAPI SDK packages for application, backend, worker, webhook, or production integrations, and reserve the CLI for one-off generation, editing, testing, and debugging.

## Reference(s):

- [RunAPI Nano Banana model page](https://runapi.ai/models/nano-banana)
- [Nano Banana model overview, pricing, and rate limits](https://runapi.ai/models/nano-banana.md)
- [Google provider comparison](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RunAPI CLI commands, SDK package choices, request JSON guidance, and credential handling guidance.]

## Skill Version(s):

0.2.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
