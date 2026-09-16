## Description:

Generate or edit images from text and local files, image URLs, or data URLs through image API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qorzj](https://clawhub.ai/user/qorzj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, combine, or locally edit images through an agent workflow that gathers visual requirements, confirms aspect ratio and resolution, estimates credit cost, and runs image generation after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are uploaded to Deep Code Plus for cost estimation and generation.

Mitigation: Review prompts and images for sensitive content before use, and only proceed after explicit cost and generation confirmation.

Risk: The security evidence reports a hidden persistent machine identifier stored under ~/.deepcode/machine-id and sent to the service.

Mitigation: Review before installing and use only if device tracking is acceptable or can be removed or disabled in the local environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qorzj/skills/image-generator)
- [Deep Code Plus API Keys](https://deepcode.vegamo.cn/plus/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a saved PNG file path and temporary image URL after successful generation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
