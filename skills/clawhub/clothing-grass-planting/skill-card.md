## Description:

Transforms an existing outfit image into social-commerce lifestyle images by preserving garments and accessories while changing the model, pose, scene, lighting, and camera style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and developers use this skill to generate lifestyle social-commerce clothing images from a source outfit image, including street, cafe, home, travel, and commute scenes. It is intended for repeated content variants where clothing details remain fixed while scene, pose, model, and lighting change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided images and prompts are sent to dLazy cloud services for generation.

Mitigation: Use only images the user has rights to process and make the cloud upload behavior clear before execution.

Risk: Generated lifestyle images could be misused to imply a real person, endorsement, or product experience.

Mitigation: Avoid impersonating real people and review outputs for misleading identity or endorsement claims before publication.

Risk: The workflow depends on a third-party CLI and hosted API.

Mitigation: Review the pinned dLazy CLI package and service terms when third-party cloud tooling is a concern.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [Related one-shot skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/one-shot/skill.md)
- [Related remove-watermark skill](https://github.com/dlazyai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save generated JPEG, PNG, or WebP image assets through the dLazy CLI.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
