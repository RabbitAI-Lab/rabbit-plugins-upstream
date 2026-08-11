## Description:

Generate FUZZ music from exact lyrics or instrumental briefs with Producer through RunAPI. Use the RunAPI CLI for one-off work and the language SDKs for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to generate FUZZ music from exact lyrics or instrumental briefs through RunAPI, using the CLI for one-off work and SDKs for application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, lyrics, and generated media requests are sent to an external RunAPI service.

Mitigation: Confirm RunAPI is trusted and send only work intended for that provider; use environment or CLI authentication for API keys.

Risk: The CLI path is intended for one-off generation, smoke tests, debugging, and manual verification, not as an application runtime layer.

Mitigation: Use the official language SDKs for apps, workers, services, libraries, webhook pipelines, and production workflows.

Risk: Generated media URLs may be temporary.

Mitigation: Download and store required audio or cover image outputs in durable storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-producer)
- [RunAPI Producer homepage](https://runapi.ai/models/producer)
- [Producer model overview](https://runapi.ai/models/producer.md)
- [Producer model details and pricing](https://runapi.ai/models/producer/fuzz-2.0.md)
- [Producer provider page](https://runapi.ai/providers/producer.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown guidance with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide asynchronous music-generation jobs; generated media URLs should be downloaded for durable storage.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
