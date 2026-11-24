## Description:

已有模特图换模特、换背景。一张模特图 → 多人群多场景版本，商品本身不变。当用户说「换模特」「换背景」「换人种」「一图多版」「同一件衣服换个人」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams use this skill to create alternate catalog images from an existing model or mannequin photo, changing the model, background, or both while aiming to keep the featured product consistent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and face references may be sent to an external image provider.

Mitigation: Before sending images, confirm you are authorized to use them and share them with the selected provider.

Risk: Security inspection was incomplete, so it does not establish that every component was reviewed.

Mitigation: Review the image-processing and face-reference examples and the remaining skill files before deployment.

## Reference(s):

- [Model flags reference](artifact/references/model-flags.md)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [dLazy website](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Images, Prompts, Shell commands]

**Output Format:** [Image files (typically JPEG) with prompt text and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image size, quality, format, and batch count can be specified; generated images need visual review.]

## Skill Version(s):

1.0.34 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
