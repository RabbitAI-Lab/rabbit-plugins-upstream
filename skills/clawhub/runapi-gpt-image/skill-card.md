## Description:

Generate and edit images with GPT Image through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or edit images with GPT Image through RunAPI, choosing the CLI for one-off tasks and SDKs for application integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input images for edits may be sent to RunAPI for image generation or transformation.

Mitigation: Install and use the skill only when sending those inputs to RunAPI is acceptable for the user, data, and task.

Risk: API keys or saved CLI credentials may grant access to RunAPI resources.

Mitigation: Prefer environment-based RUNAPI_API_KEY authentication for agent and headless runs, and use saved CLI config or browser login only when intentional.

Risk: Generated file URLs returned by RunAPI are temporary.

Mitigation: Download and store generated assets in durable storage within the retention window described by the skill.

## Reference(s):

- [RunAPI GPT Image model overview](https://runapi.ai/models/gpt-image.md)
- [RunAPI OpenAI provider comparison](https://runapi.ai/providers/openai.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI GPT Image homepage](https://runapi.ai/models/gpt-image)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-gpt-image)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands, package names, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce or retrieve generated image files through RunAPI.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
