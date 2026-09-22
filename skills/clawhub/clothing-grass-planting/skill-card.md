## Description:

Creates social-commerce lifestyle clothing images by preserving an outfit while changing the model, pose, scene, lighting, and camera style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, merchants, and marketing operators use this skill to generate lifestyle social-commerce images from a reference outfit, optionally using a second image for model, scene, pose, and lighting guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images of real people may lead to preserved identity in generated social-commerce images.

Mitigation: Use only owned or authorized model references, avoid celebrity or private-person references, and review outputs for identity preservation before publication.

Risk: Generated images may imply a person endorsed, wore, or experienced a product when they did not.

Mitigation: Do not use the skill for fake endorsements or fabricated customer experiences; label or discard outputs that could mislead viewers.

Risk: Prompts and selected images are uploaded to cloud image-generation providers.

Mitigation: Avoid sensitive, confidential, or unauthorized images and review provider data handling expectations before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-grass-planting)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image-generation calls that can save generated JPEG assets through supported providers.]

## Skill Version(s):

1.0.11 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
