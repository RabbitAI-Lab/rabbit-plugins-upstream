## Description:

Generate and remix images with Flux through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or remix Flux images through RunAPI, using the CLI for one-off work and SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts or input images are sent to RunAPI for Flux generation.

Mitigation: Use this skill only when that service use is acceptable, and review RunAPI pricing and retention expectations before using it for sensitive images.

Risk: API credentials may be exposed during agent or headless runs.

Mitigation: Prefer environment-based API key handling with RUNAPI_API_KEY or saved CLI configuration, and avoid interactive browser login unless explicitly requested.

Risk: RunAPI-generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download and store generated files in durable storage within 7 days.

Risk: Using the CLI as a production runtime integration layer can create brittle application behavior.

Mitigation: Use the relevant RunAPI SDK for app, backend, worker, library, webhook, or production workflow integration.

## Reference(s):

- [RunAPI Flux homepage](https://runapi.ai/models/flux)
- [Flux model overview, pricing, and rate limits](https://runapi.ai/models/flux.md)
- [Black Forest Labs provider comparison](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)
- [Flux Dev variant](https://runapi.ai/models/flux/dev.md)
- [Flux Pro variant](https://runapi.ai/models/flux/pro.md)
- [Flux 2 Klein variant](https://runapi.ai/models/flux/2-klein.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and SDK integration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include RunAPI CLI commands, SDK package names, request-field guidance, and generated-file handling guidance.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
