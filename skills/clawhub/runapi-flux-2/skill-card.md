## Description:

Generate and remix images with Flux 2 through RunAPI for one-off CLI tasks or SDK-based application integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or remix images with Flux 2 through RunAPI. It supports one-off CLI workflows and SDK guidance for application or backend integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runapi CLI may store imported tokens in saved configuration.

Mitigation: Review CLI token storage behavior before deployment and prefer RUNAPI_API_KEY for headless or temporary use.

Risk: Interactive browser login can block headless agent runs.

Mitigation: Use RUNAPI_API_KEY or import the token from the environment for non-interactive execution.

Risk: RunAPI-generated file URLs are temporary.

Mitigation: Download and move generated files to durable storage within 7 days.

Risk: Using the CLI as a production integration layer can create brittle application behavior.

Mitigation: Use the language-specific RunAPI SDK path for app, backend, worker, library, service, or webhook integrations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-flux-2)
- [RunAPI Flux 2 model overview](https://runapi.ai/models/flux-2.md)
- [RunAPI Flux 2 homepage](https://runapi.ai/models/flux-2)
- [Black Forest Labs provider page](https://runapi.ai/providers/black-forest-labs.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce or retrieve generated image files through RunAPI.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
