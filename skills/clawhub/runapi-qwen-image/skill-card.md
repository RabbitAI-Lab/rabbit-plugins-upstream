## Description:

Generate and edit images with Qwen Image through RunAPI. Use when the user asks an agent to create, edit, or transform images with Qwen Image. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, remix, and edit images with Qwen Image through RunAPI, using the CLI for one-off tasks and language SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the third-party RunAPI CLI or service may require a RunAPI API key or saved authentication.

Mitigation: Confirm RunAPI use is acceptable before installing; prefer RUNAPI_API_KEY or saved CLI configuration, and use interactive browser login only when explicitly chosen.

Risk: RunAPI-generated file URLs are temporary and should not be treated as durable assets.

Mitigation: Download generated images into durable storage within 24 hours.

Risk: Shelling out to the CLI as a production runtime integration layer can create brittle application integrations.

Mitigation: Use the documented RunAPI SDK package for the target language when integrating Qwen Image into an app, backend, worker, or production workflow.

## Reference(s):

- [Qwen Image model overview, pricing, and rate limits](https://runapi.ai/models/qwen-image.md)
- [Qwen Image homepage](https://runapi.ai/models/qwen-image)
- [Alibaba provider comparison](https://runapi.ai/providers/alibaba.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [Text to image variant](https://runapi.ai/models/qwen-image/text-to-image.md)
- [Image remix variant](https://runapi.ai/models/qwen-image/remix-image.md)
- [Image edit variant](https://runapi.ai/models/qwen-image/edit-image.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to download generated image files because RunAPI-generated URLs are temporary.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
