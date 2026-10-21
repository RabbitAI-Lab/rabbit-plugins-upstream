## Description:

Helps agents generate illustrations, comics, and posters from Chinese-language prompts using DashScope image models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bjbook](https://clawhub.ai/user/bjbook)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can create images from Chinese-language descriptions, optionally using reference images with supported models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to DashScope or a configured compatible service.

Mitigation: Use only content approved for external processing; avoid sensitive prompts and private images unless authorized.

Risk: An untrusted custom endpoint can receive prompts, images, and API credentials.

Mitigation: Use the default DashScope endpoint or verify and approve any custom endpoint before setting DASHSCOPE_BASE_URL.

Risk: Prompts are saved locally in llm_interaction.log by default.

Mitigation: Avoid sensitive prompts and control access, retention, and cleanup of the local log.

## Reference(s):

- [zhz-image-gen on ClawHub](https://clawhub.ai/bjbook/skills/zhz-image-gen)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Plain text with command-line examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands saves generated image files to the requested path.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; skill frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
