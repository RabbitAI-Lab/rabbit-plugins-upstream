## Description:

将服装平铺图和姿势参考图合成为模特上身商拍图，并尽量保持服装款式、颜色、织法和版型不变。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams use this skill to create on-model product photography from flat-lay garment images and pose or scene references, including single garments and separated top/bottom looks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and garment or reference images to external image-generation providers.

Mitigation: Install and run it only with trusted provider credentials, and avoid using sensitive or rights-restricted images unless the data-sharing path is approved.

Risk: Server security guidance identifies unsafe remote image URL handling, including lack of private-network blocking, file-size limits, and image validation.

Mitigation: Prefer trusted local image files and avoid arbitrary third-party remote URLs until those controls are added.

Risk: The bundled generator includes broad provider execution capabilities beyond the flat-lay workflow.

Mitigation: Review the bundled generator before broad agent execution and scope credentials, network access, and writable output locations to the intended workflow.

Risk: On-model image generation can be misused to imply unauthorized likeness use or commercial endorsement.

Mitigation: Use only reference/model images with appropriate rights and consent, and follow the skill's stated boundary against fabricated commercial endorsements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [gpt-image-2 参数清单](references/model-flags.md)
- [后端调用参考](references/provider-cli.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Files]

**Output Format:** [Markdown guidance with shell commands; generated assets are typically saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default flat-lay output is a 1024x1536 high-quality JPEG when using the bundled task profile.]

## Skill Version(s):

1.0.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
