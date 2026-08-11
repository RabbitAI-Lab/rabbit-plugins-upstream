## Description:

Generate and edit images with Qwen 2 through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate, edit, or transform images with Qwen 2 through RunAPI, using the CLI for one-off tasks and SDKs for application integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses RunAPI as an external image-generation service and may require a RunAPI API key in the environment or CLI configuration.

Mitigation: Confirm external service use is acceptable before installation and keep any RunAPI API key in environment variables or saved CLI configuration rather than in prompts or source files.

Risk: Generated file URLs are temporary and may expire.

Mitigation: Download and store any generated outputs that need to be retained.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/runapi-ai/skills/runapi-qwen-2)
- [RunAPI Qwen 2 Model Page](https://runapi.ai/models/qwen-2)
- [RunAPI Qwen 2 Documentation](https://runapi.ai/models/qwen-2.md)
- [RunAPI Alibaba Provider Documentation](https://runapi.ai/providers/alibaba.md)
- [RunAPI Model Catalog](https://runapi.ai/models.md)
- [Qwen 2 Text-to-Image Documentation](https://runapi.ai/models/qwen-2/text-to-image.md)
- [Qwen 2 Image Edit Documentation](https://runapi.ai/models/qwen-2/edit-image.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline shell commands and SDK integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or reference generated image files; RunAPI-generated file URLs are temporary and should be downloaded within 7 days.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
