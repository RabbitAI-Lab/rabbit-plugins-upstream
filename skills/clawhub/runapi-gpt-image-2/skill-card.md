## Description:

Generate and edit images with GPT Image 2 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with GPT Image 2 through RunAPI, using the CLI for one-off tasks and SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image inputs may be submitted to RunAPI/OpenAI-backed services.

Mitigation: Review provider terms and avoid sending sensitive prompts or images unless the deployment requirements allow it.

Risk: The skill may use a RunAPI API key or saved CLI login.

Mitigation: Prefer environment-based or saved CLI authentication, keep credentials out of prompts and files, and rotate credentials if exposed.

Risk: Generated file URLs are temporary and may not serve as durable storage.

Mitigation: Download generated outputs and store them in approved durable storage within the retention window.

Risk: Image generation and editing can incur provider costs.

Mitigation: Review pricing, rate limits, and usage controls before running high-volume tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gpt-image-2)
- [RunAPI GPT Image 2 model overview](https://runapi.ai/models/gpt-image-2.md)
- [RunAPI GPT Image 2 homepage](https://runapi.ai/models/gpt-image-2)
- [RunAPI OpenAI provider comparison](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and SDK package guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to generate or edit image files through RunAPI and to download temporary generated file URLs into durable storage.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
